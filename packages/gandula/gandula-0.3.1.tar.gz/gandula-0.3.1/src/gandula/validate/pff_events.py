"""PFF Event Validator.

This module provides functionality to validate PFF event data.
"""

from typing import Any

from gandula.schemas.pff_events import PFFEventGame


def validate_match(match: dict[str, Any]):
    """
    Validate a single PFF match dictionary.

    Args:
        match: Dictionary containing PFF match data

    Returns:
        Validated PFF match dictionary

    Raises:
        ValidationError: If validation fails
    """
    PFFEventGame.model_validate(match)
