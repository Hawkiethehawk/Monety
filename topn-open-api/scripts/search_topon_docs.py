#!/usr/bin/env python3
"""Search the local TopOn help-center mirror and return source URLs."""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from pathlib import Path


def query_terms(query: str) -> list[str]:
    lowered = query.lower().strip()
    terms = set(re.findall(r"[a-z0-9][a-z0-9_.+-]*", lowered))
    for run in re.findall(r"[\u3400-\u9fff]+", lowered):
        if len(run) == 1:
            terms.add(run)
        else:
            terms.update(run[i : i + 2] for i in range(len(run) - 1))
    return sorted(terms, key=lambda item: (-len(item), item))[:24]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    default_index = Path(__file__).resolve().parents[1] / "references" / "topon-help" / "index.sqlite3"
    parser.add_argument("query")
    parser.add_argument("--index", type=Path, default=default_index)
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if not args.index.exists():
        raise SystemExit(f"Index not found: {args.index}. Run crawl_topon_docs.py first.")
    terms = query_terms(args.query)
    if not terms:
        raise SystemExit("The query contains no searchable terms")
    match = " OR ".join(f'"{term.replace(chr(34), chr(34) * 2)}"' for term in terms)
    connection = sqlite3.connect(args.index)
    connection.row_factory = sqlite3.Row
    rows = connection.execute(
        """
        SELECT p.title, p.url, p.category_path, p.file,
               snippet(pages_fts, 3, '', '', ' … ', 24) AS snippet,
               bm25(pages_fts, 8.0, 3.0, 1.0, 0.25) AS score
        FROM pages_fts JOIN pages p ON p.slug = pages_fts.slug
        WHERE pages_fts MATCH ?
        ORDER BY score
        LIMIT ?
        """,
        (match, max(1, min(args.limit, 30))),
    ).fetchall()
    connection.close()
    results = [dict(row) for row in rows]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for index, row in enumerate(results, 1):
            printable = f"{index}. {row['title']}\n   {row['category_path']}\n   {row['url']}\n   {row['snippet']}"
            print(printable.replace("\u00a0", " "))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
