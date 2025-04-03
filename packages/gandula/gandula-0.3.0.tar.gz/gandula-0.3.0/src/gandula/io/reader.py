"""Tracking file operations.

Provides functionality to find and read JSONL and bz2-compressed track files
across local and remote (S3) storage systems.
"""

from collections.abc import Iterator
from pathlib import Path

import fsspec
from orjson import loads


def find_track_files(directory: str | Path) -> list[str]:
    """Find all track files in a directory.

    Works with local paths, S3.
    """
    fs, path = fsspec.url_to_fs(directory)

    jsonl_files = fs.glob(path + '/**/*.jsonl')
    bz2_files = fs.glob(path + '/**/*.jsonl.bz2')

    return [fs.unstrip_protocol(f) for f in (jsonl_files + bz2_files)]


def read_line(path: str | Path, bz2=False) -> Iterator[str]:
    """Read non-empty lines from a track file.

    Works with local paths and S3. Automatically handles compression.
    """
    path = Path(path)

    compression = 'bz2' if path.suffix == '.bz2' or bz2 else None

    with fsspec.open(path, 'rb', compression=compression, encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                yield line


def read_file(path: str | Path, bz2=False) -> bytes:
    """Read file contents as bytes.

    Works with local paths and S3. Automatically handles compression.
    """
    path = Path(path)

    compression = 'bz2' if path.suffix == '.bz2' or bz2 else None

    with fsspec.open(path, 'rb', compression=compression) as file:
        return file.read()


def read_match(path: str | Path) -> list[dict]:
    """Read a single match from a track file.

    Works with local paths and S3. Automatically handles compression.
    """
    # call read_file and load the file using orjson
    match_json_lines = [loads(line) for line in read_line(path)]
    return match_json_lines
