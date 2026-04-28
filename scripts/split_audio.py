#!/usr/bin/env python3
"""Skeleton for splitting long recordings into segment audio files.

Future implementation:
- Read data/segments.csv.
- Locate each source recording from recordings.csv or a configured raw audio dir.
- Export clips to processed_audio/{segment_id}.wav.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def iter_segments(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        yield from csv.DictReader(file)


def split_audio(segments_csv: Path, raw_audio_dir: Path, output_dir: Path, dry_run: bool) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    for row in iter_segments(segments_csv):
        segment_id = row["segment_id"]
        recording_id = row["recording_id"]
        start_sec = row["start_sec"]
        end_sec = row["end_sec"]
        source_hint = raw_audio_dir / f"{recording_id}.wav"
        output_path = output_dir / f"{segment_id}.wav"

        print(f"{segment_id}: {source_hint} [{start_sec}, {end_sec}] -> {output_path}")
        if dry_run:
            continue

        # TODO: Use pydub, ffmpeg, or soundfile to slice audio.
        # Keep this explicit until the project chooses a preferred dependency.


def main() -> int:
    parser = argparse.ArgumentParser(description="Split raw recordings according to data/segments.csv.")
    parser.add_argument("--segments", default="data/segments.csv", type=Path)
    parser.add_argument("--raw-audio-dir", default="raw_audio", type=Path)
    parser.add_argument("--output-dir", default="processed_audio", type=Path)
    parser.add_argument("--dry-run", action="store_true", help="Print planned cuts without writing audio.")
    args = parser.parse_args()

    split_audio(args.segments, args.raw_audio_dir, args.output_dir, args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

