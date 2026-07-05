# Changelog

All notable changes to `d361` are recorded here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow git
tags (`vX.Y.Z`) via `hatch-vcs`.

## [2.2.10] - 2026-07-05

### Fixed
- Config hot-reload crashed with `TypeError: 'NoneType' object is not callable`
  when `watchdog` was absent. `watchdog` is now a declared dependency, and
  `EnvironmentLoader.start_hot_reload` degrades to a logged no-op if it is still
  missing instead of blowing up.
- `parse_sitemap` was called with a `sitemap_url=` keyword the function never
  accepted; the offline `prep` phase now passes the map URL positionally.
- Config unit tests exercised real behaviour incorrectly: a missing `asyncio`
  import, a hot-reload test that never created a file for the watcher, and a
  secrets-list test that leaked state through the session-scoped temp dir. Each
  now sets up isolated, correct fixtures.
- A batch of integration, mkdocs, SEO, metrics, performance, and plugin tests
  were failing against the refactored API and mkdocs layers. Root causes fixed
  in `api/metrics.py` (str/int coercion), `api/client.py` (real endpoint names,
  error status propagation), `api/token_manager.py`, `api/circuit_breaker.py`,
  `mkdocs/processors/{asset_manager,seo_optimizer,plugin_manager}.py`, and the
  mkdocs config/template generators.

### Added
- Declared test dependencies `psutil` and `pytest-benchmark` (used by the
  performance suite).
- GitHub Actions CI: `push.yml` (ruff + matrix pytest + build) and `release.yml`
  (tag-triggered test → build → PyPI + GitHub release).
- `docs/assets/icon.png` project icon.
- `CHANGELOG.md`.

### Changed
- `d361api` dependency pinned to `>=2.2.8` — the version whose nested package
  layout `d361` imports. Earlier published `d361api` (flat layout) is incompatible.
