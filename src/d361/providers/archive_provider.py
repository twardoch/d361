# this_file: external/int_folders/d361/src/d361/providers/archive_provider.py
"""
Archive provider for processing offline Document360 exports.

This module provides functionality for parsing and indexing Document360 archive
files, with full-text search capabilities and efficient SQLite storage.
"""

from __future__ import annotations

import json
import zipfile
from collections.abc import AsyncIterator
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import aiosqlite

from ..core.models import Article, Category, PublishStatus


class ArchiveProvider:
    """Provider for offline Document360 archive processing.

    This provider implements the DataProvider protocol for offline archive files.
    Articles are persisted in a local SQLite database for fast querying and
    full-text search.

    Usage::

        provider = ArchiveProvider(db_path="/tmp/archive.db")
        await provider.initialize()
        await provider.load_archive("export.zip")
        articles = await provider.list_articles()
    """

    _TABLE = "provider_articles"

    def __init__(
        self,
        db_path: str | Path | None = None,
        archive_path: str | Path | None = None,
        enable_fts: bool = True,
        **kwargs: Any,
    ) -> None:
        """Initialize the archive provider.

        Args:
            db_path: Path to the SQLite database file.  Defaults to an
                in-memory database when *None*.
            archive_path: Path to an archive file to load on demand.
            enable_fts: Enable full-text search indexing (FTS5).
            **kwargs: Additional configuration options
        """
        self.db_path: Path | None = Path(db_path) if db_path else None
        self.archive_path: Path | None = Path(archive_path) if archive_path else None
        self.enable_fts = enable_fts
        self._db: aiosqlite.Connection | None = None
        self._is_initialized: bool = False

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    @property
    def is_initialized(self) -> bool:
        """True once :meth:`initialize` has been called successfully."""
        return self._is_initialized

    async def initialize(self) -> None:
        """Open the database and create the provider schema if needed.

        This must be called before any other async method.
        """
        db_uri = str(self.db_path) if self.db_path else ":memory:"
        self._db = await aiosqlite.connect(db_uri)
        self._db.row_factory = aiosqlite.Row

        await self._db.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self._TABLE} (
                article_id   TEXT PRIMARY KEY,
                title        TEXT NOT NULL DEFAULT '',
                slug         TEXT DEFAULT '',
                content      TEXT DEFAULT '',
                content_markdown TEXT DEFAULT '',
                excerpt      TEXT DEFAULT '',
                category_id  TEXT,
                status       TEXT DEFAULT 'published',
                author_name  TEXT DEFAULT '',
                author_email TEXT DEFAULT '',
                tags         TEXT DEFAULT '[]',
                created_at   TEXT,
                updated_at   TEXT
            )
            """
        )

        if self.enable_fts:
            # FTS5 virtual table for full-text search
            await self._db.execute(
                f"""
                CREATE VIRTUAL TABLE IF NOT EXISTS {self._TABLE}_fts
                USING fts5(title, content, content='{self._TABLE}', content_rowid='rowid')
                """
            )
            # Keep FTS in sync via triggers
            await self._db.executescript(
                f"""
                CREATE TRIGGER IF NOT EXISTS {self._TABLE}_ai
                AFTER INSERT ON {self._TABLE} BEGIN
                    INSERT INTO {self._TABLE}_fts(rowid, title, content)
                    VALUES (new.rowid, new.title, new.content);
                END;

                CREATE TRIGGER IF NOT EXISTS {self._TABLE}_ad
                AFTER DELETE ON {self._TABLE} BEGIN
                    INSERT INTO {self._TABLE}_fts({self._TABLE}_fts, rowid, title, content)
                    VALUES('delete', old.rowid, old.title, old.content);
                END;

                CREATE TRIGGER IF NOT EXISTS {self._TABLE}_au
                AFTER UPDATE ON {self._TABLE} BEGIN
                    INSERT INTO {self._TABLE}_fts({self._TABLE}_fts, rowid, title, content)
                    VALUES('delete', old.rowid, old.title, old.content);
                    INSERT INTO {self._TABLE}_fts(rowid, title, content)
                    VALUES (new.rowid, new.title, new.content);
                END;
                """
            )

        await self._db.commit()
        self._is_initialized = True

    async def close(self) -> None:
        """Close the database connection."""
        if self._db is not None:
            await self._db.close()
            self._db = None
            self._is_initialized = False

    # ------------------------------------------------------------------
    # Archive loading
    # ------------------------------------------------------------------

    async def load_archive(self, archive_path: str | Path) -> dict[str, Any]:
        """Load articles and categories from a Document360 ZIP export.

        Args:
            archive_path: Path to the ``.zip`` archive file.

        Returns:
            dict with keys ``"articles"`` and ``"categories"`` listing
            the number of items imported.
        """
        if self._db is None:
            await self.initialize()

        archive_path = Path(archive_path)
        loaded: dict[str, int] = {"articles": 0, "categories": 0}

        if not archive_path.exists():
            return loaded

        with zipfile.ZipFile(archive_path, "r") as zf:
            # Try to load a JSON manifest first
            for name in zf.namelist():
                if name.endswith(".json"):
                    try:
                        raw = json.loads(zf.read(name))
                    except (json.JSONDecodeError, KeyError):
                        continue

                    if isinstance(raw, dict):
                        items = raw.get("articles", [])
                        loaded["categories"] = len(raw.get("categories", []))
                    elif isinstance(raw, list):
                        items = raw
                    else:
                        items = []

                    for raw_art in items:
                        # Only process dicts that look like articles
                        if isinstance(raw_art, dict) and raw_art.get("title"):
                            article = self._raw_to_article(raw_art)
                            await self._store_article(article)
                            loaded["articles"] += 1

        return loaded

    def _raw_to_article(self, data: dict[str, Any]) -> Article:
        """Convert a raw dict to an Article, tolerating missing fields."""
        now = datetime.now(timezone.utc)
        return Article(
            id=str(data.get("id", "")),
            title=data.get("title", ""),
            slug=data.get("slug", ""),
            content=data.get("content", ""),
            content_markdown=data.get("content_markdown", ""),
            excerpt=data.get("excerpt", ""),
            category_id=data.get("category_id"),
            status=data.get("status", PublishStatus.PUBLISHED),
            author_name=data.get("author_name", ""),
            author_email=data.get("author_email", ""),
            tags=data.get("tags", []),
            created_at=now,
            updated_at=now,
        )

    # ------------------------------------------------------------------
    # CRUD helpers
    # ------------------------------------------------------------------

    async def _store_article(self, article: Article) -> None:
        """Upsert a single article into the local database.

        Args:
            article: The :class:`~d361.core.models.Article` to store.
        """
        if self._db is None:
            await self.initialize()

        tags_json = json.dumps(
            article.tags if isinstance(article.tags, list) else list(article.tags)
        )
        await self._db.execute(
            f"""
            INSERT OR REPLACE INTO {self._TABLE}
                (article_id, title, slug, content, content_markdown, excerpt,
                 category_id, status, author_name, author_email, tags,
                 created_at, updated_at)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                str(article.id),
                article.title or "",
                article.slug or "",
                article.content or "",
                article.content_markdown or "",
                article.excerpt or "",
                str(article.category_id) if article.category_id else None,
                article.status.value
                if hasattr(article.status, "value")
                else str(article.status),
                article.author_name or "",
                article.author_email or "",
                tags_json,
                article.created_at.isoformat() if article.created_at else None,
                article.updated_at.isoformat() if article.updated_at else None,
            ),
        )
        await self._db.commit()

    def _row_to_article(self, row: aiosqlite.Row) -> Article:
        """Convert a DB row to an Article model."""
        now = datetime.now(timezone.utc)

        def _parse_dt(val: str | None) -> datetime:
            if not val:
                return now
            try:
                return datetime.fromisoformat(val)
            except ValueError:
                return now

        tags = json.loads(row["tags"] or "[]")
        return Article(
            id=row["article_id"],
            title=row["title"] or "",
            slug=row["slug"] or "",
            content=row["content"] or "",
            content_markdown=row["content_markdown"] or "",
            excerpt=row["excerpt"] or "",
            category_id=row["category_id"],
            status=row["status"] or "published",
            author_name=row["author_name"] or "",
            author_email=row["author_email"] or "",
            tags=tags,
            created_at=_parse_dt(row["created_at"]),
            updated_at=_parse_dt(row["updated_at"]),
        )

    # ------------------------------------------------------------------
    # DataProvider protocol
    # ------------------------------------------------------------------

    async def get_article(self, article_id: Any, **kwargs: Any) -> Article:
        """Fetch a single article by ID.

        Args:
            article_id: Article identifier
            **kwargs: Additional parameters

        Returns:
            Article: The requested article

        Raises:
            KeyError: If the article is not found.
        """
        if self._db is None:
            await self.initialize()

        async with self._db.execute(
            f"SELECT * FROM {self._TABLE} WHERE article_id = ?",
            (str(article_id),),
        ) as cur:
            row = await cur.fetchone()

        if row is None:
            raise KeyError(f"Article '{article_id}' not found")
        return self._row_to_article(row)

    async def list_articles(
        self,
        category_id: Any = None,
        status: str | None = None,
        **kwargs: Any,
    ) -> list[Article]:
        """List articles with optional filtering.

        Args:
            category_id: Filter by category ID
            status: Filter by status string
            **kwargs: Additional parameters

        Returns:
            list[Article]: Matching articles
        """
        if self._db is None:
            await self.initialize()

        clauses = []
        params: list[Any] = []
        if category_id is not None:
            clauses.append("category_id = ?")
            params.append(str(category_id))
        if status is not None:
            clauses.append("status = ?")
            params.append(status)

        where = f" WHERE {' AND '.join(clauses)}" if clauses else ""
        async with self._db.execute(
            f"SELECT * FROM {self._TABLE}{where}", params
        ) as cur:
            rows = await cur.fetchall()

        return [self._row_to_article(r) for r in rows]

    async def search_articles(self, query: str, **kwargs: Any) -> list[Article]:
        """Full-text search over stored articles.

        Args:
            query: Search query string
            **kwargs: Additional parameters

        Returns:
            list[Article]: Matching articles ordered by rank
        """
        if self._db is None:
            await self.initialize()

        # Try FTS first, fall back to LIKE search
        if self.enable_fts:
            try:
                async with self._db.execute(
                    f"""
                    SELECT a.* FROM {self._TABLE} a
                    INNER JOIN {self._TABLE}_fts fts ON a.rowid = fts.rowid
                    WHERE {self._TABLE}_fts MATCH ?
                    ORDER BY rank
                    """,
                    (query,),
                ) as cur:
                    rows = await cur.fetchall()
                return [self._row_to_article(r) for r in rows]
            except Exception:
                pass  # fall back to LIKE

        q = f"%{query}%"
        async with self._db.execute(
            f"SELECT * FROM {self._TABLE} WHERE title LIKE ? OR content LIKE ?",
            (q, q),
        ) as cur:
            rows = await cur.fetchall()
        return [self._row_to_article(r) for r in rows]

    async def get_articles(self, **kwargs: Any) -> list[Article]:
        """Get all articles (MkDocsExporter interface alias)."""
        return await self.list_articles(**kwargs)

    async def list_categories(self, **kwargs: Any) -> list[Category]:
        """Return an empty list (no category storage implemented yet)."""
        return []

    async def get_categories(self, **kwargs: Any) -> list[Category]:
        """Get all categories (MkDocsExporter interface alias)."""
        return await self.list_categories(**kwargs)

    async def stream_articles(self, **kwargs: Any) -> AsyncIterator[Article]:
        """Stream articles from the archive.

        Yields:
            Article: Individual articles
        """
        for article in await self.list_articles(**kwargs):
            yield article
