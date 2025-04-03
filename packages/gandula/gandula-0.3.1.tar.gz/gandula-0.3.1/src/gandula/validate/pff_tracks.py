"""PFF Track Validator.

This module provides functionality to validate PFF tracking data stored in both regular
and compressed JSONL files.
"""

from collections.abc import Iterator
from pathlib import Path
from time import sleep

from tqdm import tqdm

from ..core.logging import get_logger
from ..io.reader import find_track_files, read_file
from ..schemas.pff_tracks import PFFFrame

logger = get_logger(__name__)


def validate_records(records: Iterator[str]):
    """
    Validate PFF track records against the PFFFrame schema.

    Args:
        records: Iterator of JSON strings to validate

    Returns:
        List of validated PFFFrame objects

    Raises:
        ValidationError: If validation fails for any record
    """
    [PFFFrame.model_validate_json(record) for record in records]


def validate_file(file_path: Path):
    """
    Validate a single PFF track file.

    Args:
        file_path: Path to the jsonl or jsonl.bz2 file

    Returns:
        List of validated PFFFrame objects

    Raises:
        ValueError: If the file cannot be read or processed
    """
    if not file_path.exists():
        raise ValueError(f'File does not exist: {file_path}')
    records = read_file(file_path)
    validate_records(records)


def validate_directory(path: Path):
    """
    Validate all PFF track files in a directory.

    Args:
        path: Path to the directory containing JSONL and JSONL.BZ2 files

    Returns:
        Dictionary mapping filenames to either lists of validated PFFFrame objects
        or exceptions if processing the file failed

    Raises:
        ValueError: If the path does not exist or is not a directory
    """
    if not path.exists():
        raise ValueError(f'Directory does not exist: {path}')
    if not path.is_dir():
        raise ValueError(f'Path is not a directory: {path}')

    files = find_track_files(path)

    with tqdm(files, total=len(files), desc='Validating tracks') as pbar:
        for file_path in files:
            records = read_file(file_path)
            validate_records(records)
            sleep(0.1)
            pbar.update(1)
