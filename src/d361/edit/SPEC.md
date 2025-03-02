```markdown
# A Human-Friendly Python Package for Document360: `d361util`

This document outlines the design and specification for a Python package, `d361util`, built on top of the auto-generated `d361api` package.  The goal of `d361util` is to provide a simplified, user-friendly interface for interacting with a Document360 knowledge base, abstracting away the complexities of the raw API and presenting a filesystem-like structure for managing articles and categories. This will allow users to easily synchronize local Markdown files with their Document360 cloud storage.

## Key Concepts and Design Principles

1.  **Filesystem Analogy:**  The package will mimic a filesystem, where categories are analogous to directories and articles are analogous to files.  This familiar structure will make it easier for users to intuitively understand and interact with the knowledge base content.

2.  **Abstraction:** The `d361util` package will wrap the `d361api` package, handling API authentication, pagination, error handling, and data conversion internally.  Users will interact with Python objects representing articles and categories, not raw API responses.

3.  **Synchronization:** A core feature will be two-way synchronization between a local directory and the remote Document360 knowledge base.  Changes made locally (creating, updating, deleting files) should be reflected in the cloud, and vice versa.

4.  **Markdown Focus:** The primary content format will be Markdown, given its prevalence in documentation writing and ease of use. The package will handle the conversion between Markdown and the formats supported by the `d361api`.

5.  **Error Handling:** Robust error handling will be built-in, providing user-friendly messages for common issues (e.g., API rate limits, authentication failures, network errors).

6. **Versioning (Stretch Goal):** Ideally, the package would support interacting with Document360's versioning system, allowing users to specify which version they are working with. This is marked as a stretch goal due to the potential complexity.

7. **Caching (Stretch Goal):**  Local caching of fetched data (article lists, content) could significantly improve performance, especially for read-heavy operations.  This is a stretch goal due to the complexities of cache invalidation and synchronization.

## Proposed Package Structure

```
d361util/
├── __init__.py
├── client.py      # Main client class for interacting with Document360
├── category.py    # Class representing a Document360 category
├── article.py     # Class representing a Document360 article
├── exceptions.py  # Custom exception classes
├── utils.py       # Utility functions (authentication, API calls, etc.)
├── sync.py        # Functions for synchronizing local and remote content
```

## Class Definitions

### `D361Client` (in `client.py`)

This class will be the main entry point for interacting with the Document360 knowledge base.

```python
import d361api
from d361api import exceptions as api_exceptions
from .category import Category
from .article import Article
from .exceptions import D361Error, AuthenticationError, NotFoundError, ConflictError


class D361Client:
    """
    A client for interacting with a Document360 knowledge base,
    providing a filesystem-like interface.
    """

    def __init__(self, api_token: str, project_version_id: str, api_url: str = "https://apihub.document360.io"):
        """
        Initializes the D361Client.

        Args:
            api_token: Your Document360 API token.
            project_version_id: The ID of the project version to work with.
            api_url: Base URL for Document360 API
        """
        self.configuration = d361api.Configuration(
            host=api_url
        )
        self.configuration.api_key['api_token'] = api_token
        self.api_client = d361api.ApiClient(self.configuration)
        self.articles_api = d361api.ArticlesApi(self.api_client)
        self.categories_api = d361api.CategoriesApi(self.api_client)
        self.project_version_id = project_version_id
        self.default_language = "en"


    def get_category(self, category_id: str, language: Optional[str] = None) -> "Category":
        """Retrieves a Category object by its ID.

        Args:
            category_id: The ID of the category.
            language: Optional language code.  Defaults to self.default_language.

        Returns:
            A Category object.

        Raises:
            NotFoundError: If the category is not found.
            D361Error: For other API errors.
        """
        try:
            lang = language or self.default_language
            response = self.categories_api.v2_categories_category_id_get(category_id, lang_code=lang)
            return Category._from_api_response(self, response.data)
        except api_exceptions.NotFoundException:
            raise NotFoundError(f"Category with ID '{category_id}' not found.")
        except api_exceptions.ApiException as e:
            raise D361Error(f"API Error: {e}")


    def create_category(self, name: str, parent_id: Optional[str] = None,
                       order: int = 0, is_page = False) -> "Category":
        """Creates a new category.

        Args:
            name: The name of the category.
            parent_id: The ID of the parent category. If None, creates a top-level category.
            order: position of the category inside the parent
            is_page: whether the category is of type Page

        Returns:
            The newly created Category object.

        Raises:
            D361Error: For API errors.
        """
        try:
            category_type = 1 if is_page else 0
            request = d361api.AddCategoryRequest(
                name=name,
                project_version_id=self.project_version_id,
                order=order,
                parent_category_id=parent_id,
                category_type=category_type,
            )
            response = self.categories_api.v2_categories_post(add_category_request=request)
            return self.get_category(response.data.id)
        except api_exceptions.ApiException as e:
            raise D361Error(f"API Error: {e}")


    def get_article(self, article_id: str, version_number: int = 1, language: Optional[str] = None) -> "Article":
         """Retrieves an Article object by its ID.

         Args:
             article_id: The ID of the article.
             version_number: The version number of the article.
             language: Optional language code.  Defaults to self.default_language.

         Returns:
             An Article object.

         Raises:
             NotFoundError: If the article is not found.
             D361Error: For other API errors.
         """
         try:
             lang = language or self.default_language
             response = self.articles_api.v2_articles_article_id_lang_code_versions_version_number_get(
                 article_id, version_number, lang_code=lang
             )
             return Article._from_api_response(self, response.data)
         except api_exceptions.NotFoundException:
             raise NotFoundError(f"Article with ID '{article_id}' and version '{version_number}' not found.")
         except api_exceptions.ApiException as e:
             raise D361Error(f"API Error: {e}")
         
         

    def create_article(self, title: str, content: str, category_id: str,
                      order: int = 0, content_type: int = 0) -> "Article":
        """Creates a new article.

        Args:
            title: The title of the article.
            content: The Markdown content of the article.
            category_id: The ID of the parent category.
            order: (Optional) The order/position of the article.
            content_type: The type of article content. 0 for Markdown, 1 for HTML. Defaults to Markdown.
        Returns:
            The newly created Article object.

        Raises:
            D361Error: For API errors.
        """
        try:
            request = d361api.CreateArticleRequest(
                title=title,
                content=content,
                category_id=category_id,
                project_version_id=self.project_version_id,
                order=order,
                content_type=content_type,
            )
            response = self.articles_api.v2_articles_post(create_article_request=request)
            return self.get_article(response.data.id)

        except api_exceptions.ApiException as e:
            raise D361Error(f"API Error: {e}")

    # --- Additional utility methods ---
    
    async def close(self):
        """
        Closes the API client and its underlying connections.
        """    
        await self.api_client.close()

    async def __aenter__(self):
         return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()        


```

### `Category` (in `category.py`)

```python
from d361api.d361api.models import category_data_customer
from .article import Article
from typing import List, Optional

class Category:
    """Represents a category in Document360."""

    def __init__(self, client, category_id: str, name: str, parent_id: Optional[str] = None,
                 order: int = 0):
        self.client = client
        self.id = category_id
        self.name = name
        self.parent_id = parent_id
        self.order = order

    @classmethod
    def _from_api_response(cls, client, data: category_data_customer.CategoryDataCustomer):
        """Creates a Category instance from the API response data."""
        return cls(
            client=client,
            category_id=data.id,
            name=data.name,
            parent_id=data.parent_category_id,
            order=data.order,
        )

    def articles(self) -> List["Article"]:
        """Retrieves a list of articles within this category."""
        # TODO - this API call need a lang_code, but there isn't on in this class
        #response = self.client.articles_api.v2_project_versions_project_version_id_articles_get(
        #    self.client.project_version_id, 
        #    #lang_code=self.client.default_language # how to pass this if the object doesn't hold the data
        #)
        #return [Article._from_api_response(self.client, article_data) for article_data in response.data]
        raise NotImplementedError("TODO")
    
    def subcategories(self) -> List["Category"]:
        """Retrieves a list of subcategories within this category."""
        raise NotImplementedError("TODO")

    def create_article(self, title: str, content: str, order: int = 0) -> "Article":
        """Creates a new article within this category."""
        return self.client.create_article(title, content, self.id, order)

    def create_subcategory(self, name: str, order: int = 0) -> "Category":
        """Creates a new subcategory within this category."""
        return self.client.create_category(name, self.id, order)

    def delete(self) -> None:
        """Deletes this category."""
        raise NotImplementedError("TODO")
        #self.client.categories_api.v2_categories_category_id_delete(self.id)

    def update(self, name: Optional[str] = None, order: Optional[int] = None) -> "Category":
        """Updates this category's name or order."""
        raise NotImplementedError("TODO")
        #request = d361api.UpdateCategoryRequest(name=name, order=order)
        #response = self.client.categories_api.v2_categories_category_id_put(self.id, update_category_request=request)
        #return Category._from_api_response(self.client, response.data)

    def __str__(self):
        return f"Category(id={self.id}, name={self.name})"
```

### `Article` (in `article.py`)

```python
from d361api.d361api.models import article_version_data_customer_response
from typing import Optional

class Article:
    """Represents an article in Document360."""

    def __init__(self, client, article_id: str, title: str, content: str,
                 category_id: str, version_number: int = 1,
                 language: str = "en"):
        self.client = client
        self.id = article_id
        self.title = title
        self.content = content
        self.category_id = category_id
        self.version_number = version_number
        self.language = language

    @classmethod
    def _from_api_response(cls, client, data: article_version_data_customer_response.ArticleVersionDataCustomerResponse):
        """Creates an Article instance from the API response data."""
        return cls(
            client=client,
            article_id=data.id,
            title=data.title,
            content=data.content, # or data.html_content ??
            category_id=data.category_id,
            version_number = data.version_number,
            # language = data.language_code # Is there lang_code here?            
        )
    
    def update(self, title: Optional[str] = None, content: Optional[str] = None) -> "Article":
        """Updates the article's title or content.
           If content_type is not specified, use the content field.
        """
        raise NotImplementedError("TODO")
        # request = d361api.UpdateArticleRequest(title=title, content=content)
        # response = self.client.articles_api.v2_articles_article_id_lang_code_put(
        #    self.id, self.language, update_article_request=request
        #)
        #return Article._from_api_response(self.client, response.data)
        

    def delete(self) -> None:
        """Deletes the article."""
        raise NotImplementedError("TODO")        
        # self.client.articles_api.v2_articles_article_id_delete(self.id)

    def publish(self) -> "Article":
        """Publishes the current version of the article."""
        raise NotImplementedError("TODO")        
        #response = self.client.articles_api.v2_articles_article_id_lang_code_publish_post(self.id, self.language)
        #return Article._from_api_response(self.client, response.data)

    def __str__(self):
        return f"Article(id={self.id}, title={self.title})"
```

### `exceptions.py`

```python
class D361Error(Exception):
    """Base exception for d361util errors."""
    pass

class AuthenticationError(D361Error):
    """Raised when authentication fails."""
    pass

class NotFoundError(D361Error):
    """Raised when a resource is not found."""
    pass
class ConflictError(D361Error):
    """Conflict error"""

```

### `utils.py`

```python
# d361util/utils.py
# This can hold helper functions, if needed. For now,
# it's just a placeholder.

def convert_to_d361_format(markdown_content: str) -> str:
    """Converts standard Markdown to Document360's expected format.

    (Placeholder -  actual conversion logic would go here, based on
     Document360's API requirements. This may include handling of images,
     code blocks, etc. differently from standard Markdown.)
    """
    # For now we support basic markdown
    return markdown_content


def convert_from_d361_format(d361_content: str) -> str:
    """Converts Document360's content format to standard Markdown."""

    return d361_content

```

## Example Usage

```python
from d361util import D361Client

async def main():
    async with D361Client(api_token="YOUR_API_TOKEN", project_version_id="YOUR_PROJECT_VERSION_ID") as client:
        try:
            # Get a category
            category = await client.get_category("category_id")
            print(category)

            # Get articles from a category
            articles = await category.articles()
            for article in articles:
                print(article)

            # Create a new article
            new_article = await client.create_article(title="My New Article",
                                                content="# My New Article\n\nThis is the content.",
                                                category_id="category_id")
            print(f"Created article: {new_article}")

            # Update the new article
            updated_article = await new_article.update(title="My Updated Article", content="# Updated\nContent")
            print(f"Updated article: {updated_article}")

            # Get specific version of an article
            v1_article = await client.get_article("article_id", version_number=1)
            print(f"Version 1 article: {v1_article}")
            

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## Synchronization Logic (Conceptual)

The `sync.py` file would contain the logic for synchronizing a local directory with the Document360 knowledge base. This is a high-level conceptual outline:

```python
# d361util/sync.py

import os
import asyncio
from typing import List
from .client import D361Client
from .category import Category
from .article import Article
from .utils import convert_to_d361_format, convert_from_d361_format

async def sync_local_to_remote(client: D361Client, local_path: str, remote_category_id: str):
    """Synchronizes a local directory with a remote Document360 category.

    Args:
        client: The D361Client instance.
        local_path: The path to the local directory.
        remote_category_id: The ID of the remote category.
    """

    remote_category = await client.get_category(remote_category_id)

    # 1. Get remote articles/categories
    remote_articles = await remote_category.articles()
    # TODO Add ability to get subcategories
    remote_articles_by_title = {article.title: article for article in remote_articles}

    # 2. Iterate through local files
    for filename in os.listdir(local_path):
        if not filename.endswith(".md"):
            continue  # Skip non-Markdown files

        local_file_path = os.path.join(local_path, filename)
        title = os.path.splitext(filename)[0]  # Use filename as title (without extension)

        with open(local_file_path, "r", encoding="utf-8") as f:
            local_content = f.read()

        d361_content = convert_to_d361_format(local_content)

        # 3. Check if article exists remotely
        if title in remote_articles_by_title:
            # 4. Update existing article
            remote_article = remote_articles_by_title[title]
            print(f"Updating article: {title}")
            await remote_article.update(title=title, content=d361_content)
            
        else:
            # 5. Create new article
            print(f"Creating article: {title}")
            await client.create_article(title=title, content=d361_content, category_id=remote_category_id)

    # 6. (Optional) Handle deletions:  Compare local files with remote articles
    # and delete remote articles that don't exist locally.
    local_titles = {os.path.splitext(filename)[0] for filename in os.listdir(local_path) if filename.endswith(".md")}
    for title, article in remote_articles_by_title.items():
        if title not in local_titles:
            print(f"Deleting remote article: {title}")
            await article.delete()




async def sync_remote_to_local(client: D361Client, local_path: str, remote_category_id: str):
    """Synchronizes a remote Document360 category with a local directory.
       This function will download the articles.
    """

    remote_category = await client.get_category(category_id)
    remote_articles  = await remote_category.articles()
    
    for article in remote_articles:
        local_file_path = os.path.join(local_path, f"{article.title}.md")
        markdown_content = convert_from_d361_format(article.content)
        with open(local_file_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
            print(f"Downloaded: {article.title} to {local_file_path}")

async def main():
    # Example usage
    async with D361Client(api_token="YOUR_API_TOKEN", project_version_id="YOUR_PROJECT_ID") as client:
        #Sync from Markdown files into Document360
        await sync_local_to_remote(client, "path/to/local/docs", "remote_category_id")

        # Sync from Document360 to Markdown files
        await sync_remote_to_local(client, "path/to/local/docs", "remote_category_id") # same category
        
        await client.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

```

## Further Considerations and Enhancements

*   **Configuration:** Use a configuration file (e.g., YAML, JSON) to store API keys, project IDs, default categories, and synchronization settings. This makes the tool more user-friendly and avoids hardcoding sensitive information.

*   **Command-Line Interface (CLI):** Develop a CLI using libraries like `click` or `argparse` to provide a user-friendly command-line interface for interacting with the package.  This would allow for commands like:
    ```bash
    d361util sync --local-path /path/to/docs --remote-category my-category
    d361util pull --remote-category my-category --local-path /path/to/docs
    d361util push --local-path /path/to/docs --remote-category my-category
    d361util create-category --name "New Category" --parent-id "parent_category_id"
    d361util get-article --id "article_id"
    d361util list-categories
    ```

*   **More Robust File Handling:**
    *   Handle different file encodings (not just UTF-8).
    *   Implement more sophisticated conflict resolution strategies during synchronization (e.g., prompting the user, using timestamps, or implementing a three-way merge).
    *   Support for non-Markdown files (e.g., uploading images to Drive, handling HTML files).

*   **Asynchronous Operations:** The provided code already utilizes `asyncio` for concurrent operations, which is crucial for performance. Ensure all API calls are made asynchronously.

*   **Testing:**  Thorough unit and integration tests are essential.  The `tests` directory already includes a structure for tests; these need to be implemented comprehensively.

*   **Documentation:**  Write comprehensive documentation (using Sphinx, MkDocs, or similar) for the package, including usage examples, API reference, and troubleshooting guides.

*   **Rate Limiting Handling:** The `d361api` likely has rate limits. Implement robust retry mechanisms with exponential backoff in `d361util` to handle rate limiting gracefully. `aiohttp-retry` is already being used, which is a good start.

*   **Progress Indicators:** For long-running operations (like syncing a large documentation set), provide progress indicators (e.g., using `tqdm`) to give users feedback.

*   **Support for Attachments:**  Implement methods for uploading and downloading file attachments associated with articles. This will involve using the `DriveApi` of the `d361api`.

*   **Category Hierarchy:** Implement methods for creating nested categories (subcategories) and navigating the category tree. This would involve recursively calling `get_category` and `create_category`.

*   **Search Functionality:** Add a `search_articles` method to the `D361Client` that utilizes the search capabilities of the Document360 API.

*   **User and Group Management (Stretch Goal):**  If the underlying API supports it, consider adding classes and methods for managing users, groups, and their permissions.

* **Package Distribution**: Package the utility for distribution on PyPI, making it easy for others to install and use.

This enhanced design document provides a solid foundation for a user-friendly and robust Python package for managing Document360 knowledge bases. The filesystem-like abstraction, synchronization capabilities, and comprehensive error handling will significantly simplify the process of interacting with the Document360 API. The use of `asyncio` and attention to best practices ensure that the package is efficient and scalable.  The inclusion of stretch goals and clear TODOs sets a roadmap for future development.
