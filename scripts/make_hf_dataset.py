#!/usr/bin/env python3
"""Create a local Hugging Face-style dataset folder from data/metadata.csv.

This script does not upload anything. It prepares a simple local structure that
can later be adapted for datasets.Dataset, Parquet, or dataset card publishing.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def load_rows(metadata_csv: Path) -> list[dict[str, str]]:
    with metadata_csv.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def write_jsonl(rows: list[dict[str, str]], output_path: Path) -> None:
    with output_path.open("w", encoding="utf-8") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_dataset_card(output_dir: Path) -> None:
    card = """# Zhuji Dialect Corpus

This is a local Hugging Face-style export generated from `data/metadata.csv`.

Licensing and consent must be checked before publishing any audio or metadata.
Audio use is governed by speaker consent.
"""
    (output_dir / "README.md").write_text(card, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a local HF-style dataset export.")
    parser.add_argument("--metadata", default="data/metadata.csv", type=Path)
    parser.add_argument("--output-dir", default="hf_dataset", type=Path)
    args = parser.parse_args()

    rows = load_rows(args.metadata)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(rows, args.output_dir / "metadata.jsonl")
    write_dataset_card(args.output_dir)
    print(f"wrote {len(rows)} records to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

