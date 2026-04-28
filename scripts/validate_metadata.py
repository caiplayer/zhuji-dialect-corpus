#!/usr/bin/env python3
"""Validate required CSV columns for the Zhuji dialect corpus."""

from __future__ import annotations

import csv
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

REQUIRED_FIELDS = {
    "speakers.csv": [
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
    ],
    "recordings.csv": [
        "recording_id",
        "speaker_id",
        "date",
        "location_type",
        "device",
        "format",
        "duration_sec",
        "genre",
        "consent_level",
        "license",
        "notes",
    ],
    "segments.csv": [
        "segment_id",
        "recording_id",
        "start_sec",
        "end_sec",
        "speaker_id",
        "dialect_text",
        "mandarin_translation",
        "normalized_text",
        "topic",
        "quality",
        "review_status",
    ],
    "metadata.csv": [
        "segment_id",
        "audio_path",
        "dialect_text",
        "mandarin_translation",
        "speaker_id",
        "township",
        "age_group",
        "gender_optional",
        "topic",
        "license",
    ],
}


def read_header(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)
        return next(reader, [])


def validate_file(filename: str, required: list[str]) -> list[str]:
    path = DATA_DIR / filename
    errors: list[str] = []

    if not path.exists():
        return [f"{filename}: file not found"]

    header = read_header(path)
    missing = [field for field in required if field not in header]
    if missing:
        errors.append(f"{filename}: missing fields: {', '.join(missing)}")

    return errors


def main() -> int:
    all_errors: list[str] = []
    for filename, required in REQUIRED_FIELDS.items():
        all_errors.extend(validate_file(filename, required))

    if all_errors:
        for error in all_errors:
            print(f"ERROR: {error}")
        return 1

    print("validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

