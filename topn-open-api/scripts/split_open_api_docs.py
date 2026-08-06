#!/usr/bin/env python3
"""Extract Open API help pages and optionally remove them from the source mirror."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sqlite3
import tempfile
from pathlib import Path


def is_open_api(page: dict) -> bool:
    category = page.get("category_path") or []
    return bool(category and str(category[0]).startswith("Open API"))


def build_sqlite(path: Path, pages: list[dict], docs_dir: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix="topn-docs-", suffix=".sqlite3", dir=path.parent)
    os.close(fd)
    temp_path = Path(temporary)
    connection = sqlite3.connect(temp_path)
    connection.executescript("""
        CREATE TABLE pages (
            slug TEXT PRIMARY KEY, url TEXT NOT NULL, title TEXT NOT NULL,
            category_path TEXT NOT NULL, parent_slug TEXT, file TEXT NOT NULL,
            captured_at TEXT, site_modified TEXT, content_sha256 TEXT NOT NULL
        );
        CREATE VIRTUAL TABLE pages_fts USING fts5(
            slug UNINDEXED, title, category_path, body, search_terms
        );
    """)
    for page in pages:
        body = (docs_dir / Path(page["file"]).name).read_text(encoding="utf-8").replace("\u00a0", " ")
        category = " > ".join(page.get("category_path") or [])
        terms = re.sub(r"\s+", " ", f"{page['title']} {category} {body}")
        connection.execute("INSERT INTO pages VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (
            page["slug"], page["url"], page["title"], category, page.get("parent_slug"),
            page["file"], page.get("captured_at"), page.get("site_modified"), page["content_sha256"],
        ))
        connection.execute("INSERT INTO pages_fts VALUES (?, ?, ?, ?, ?)", (
            page["slug"], page["title"], category, body, terms,
        ))
    connection.commit()
    connection.close()
    os.replace(temp_path, path)


def write_manifest(path: Path, source: dict, pages: list[dict]) -> None:
    slugs = {page["slug"] for page in pages}
    payload = {
        **source,
        "discovered_pages": len(pages), "saved_pages": len(pages),
        "failed_pages": 0, "failures": [],
        "roots": [page["slug"] for page in pages if not page.get("parent_slug") or page.get("parent_slug") not in slugs],
        "pages": pages,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--remove-from-source", action="store_true")
    args = parser.parse_args()
    source, output = args.source.resolve(), args.output.resolve()
    if source == output or source in output.parents:
        raise SystemExit("Output must be outside the source mirror")
    manifest = json.loads((source / "index.json").read_text(encoding="utf-8"))
    api_pages = [page for page in manifest["pages"] if is_open_api(page)]
    other_pages = [page for page in manifest["pages"] if not is_open_api(page)]
    if not api_pages:
        raise SystemExit("No Open API pages found")
    output_docs = output / "docs"
    output_docs.mkdir(parents=True, exist_ok=True)
    for page in api_pages:
        shutil.copy2(source / page["file"], output_docs / Path(page["file"]).name)
    write_manifest(output / "index.json", manifest, api_pages)
    build_sqlite(output / "index.sqlite3", api_pages, output_docs)

    if args.remove_from_source:
        staging = source.parent / f"{source.name}-non-api-staging"
        if staging.exists():
            shutil.rmtree(staging)
        staging_docs = staging / "docs"
        staging_docs.mkdir(parents=True)
        for page in other_pages:
            shutil.copy2(source / page["file"], staging_docs / Path(page["file"]).name)
        write_manifest(staging / "index.json", manifest, other_pages)
        build_sqlite(staging / "index.sqlite3", other_pages, staging_docs)
        backup = source.parent / f"{source.name}-pre-split"
        if backup.exists():
            shutil.rmtree(backup)
        source.rename(backup)
        staging.rename(source)
        shutil.rmtree(backup)
    print(json.dumps({"open_api_pages": len(api_pages), "main_pages": len(other_pages), "output": str(output)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
