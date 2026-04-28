#!/usr/bin/env python3
"""Skeleton for anonymizing sensitive corpus metadata.

Do not publish real names, phone numbers, ID numbers, detailed addresses, or
private family information. This script keeps only fields intended for release.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


PUBLIC_SPEAKER_FIELDS = [
    "speaker_id",
    "birth_year",
    "age_group",
    "gender_optional",
    "birth_place",
    "township",
    "years_in_zhuji",
    "home_language",
    "self_dialect_level",
    "consent_level",
    "notes",
]


def anonymize_csv(input_path: Path, output_path: Path, fields: list[str]) -> None:
    with input_path.open("r", encoding="utf-8-sig", newline="") as infile:
        reader = csv.DictReader(infile)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fields)
            writer.writeheader()
            for row in reader:
                writer.writerow({field: row.get(field, "") for field in fields})


def main() -> int:
    parser = argparse.ArgumentParser(description="Create anonymized public CSV files.")
    parser.add_argument("--speakers", default="data/speakers.csv", type=Path)
    parser.add_argument("--output-dir", default="exports/anonymized", type=Path)
    args = parser.parse_args()

    anonymize_csv(args.speakers, args.output_dir / "speakers.csv", PUBLIC_SPEAKER_FIELDS)
    print("anonymized export created")
    print("Reminder: review notes manually before publishing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

