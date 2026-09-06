from __future__ import annotations

import argparse
import sys
from pathlib import Path

from papertray.config import load_settings
from papertray.s3 import upload_file


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="papertray", description="Upload invoices to S3")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sync = sub.add_parser("sync", help="upload files from a folder")
    sync.add_argument("folder", type=Path)

    args = parser.parse_args(argv)
    settings = load_settings()
    folder: Path = args.folder

    if not folder.is_dir():
        print(f"not a folder: {folder}", file=sys.stderr)
        return 2

    uploaded = 0
    for path in sorted(folder.iterdir()):
        if path.suffix.lower() not in {".pdf", ".png", ".jpg", ".jpeg"}:
            continue
        key = upload_file(settings, path)
        print(key)
        uploaded += 1

    if uploaded == 0:
        print("no invoice files found", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
