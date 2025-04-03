"""Transform raw PFF tracking data into flattened structures for DataFrames."""

from enum import Enum
from itertools import chain
from typing import Any

from ..core.logging import get_logger

logger = get_logger(__name__)


class TransformFormat(str, Enum):
    """Format options for the transformed output."""

    WIDE = 'wide'  # One row per frame with player data as columns
    LONG = 'long'  # Multiple rows per frame (one per player)


def _flatten_dict(d: dict[str, Any], prefix: str = '') -> dict[str, Any]:
    """
    Recursively flatten a nested dictionary with prefixed keys.

    Args:
        d: Dictionary to flatten
        prefix: Prefix to add to keys (with trailing underscore if non-empty)

    Returns:
        Flattened dictionary where nested keys are combined with their parent keys
    """
    result = {}

    try:
        for k, v in d.items():
            key = f'{prefix}_{k}' if prefix else k

            if isinstance(v, dict):
                result.update(_flatten_dict(v, key))
            else:
                result[key] = v
    except AttributeError:
        logger.error(f'Error flattening dictionary: {d}')
        raise

    return result


def _transform_wide(frame: dict[str, Any]) -> dict[str, Any]:
    """
    Transform a single frame dictionary to a flat structure.

    Args:
        frame: A dictionary containing PFF tracking data for one frame

    Returns:
        A flat dictionary containing all frame data
    """
    # fmt: off
    skip_keys = [
        'homePlayers', 'awayPlayers', 'balls',
        'homePlayersSmoothed', 'awayPlayersSmoothed', 'ballsSmoothed' # kalman filtered,
        'team'
    ]
    # fmt: on

    result = {
        k: v
        for k, v in frame.items()
        if k not in skip_keys and not isinstance(v, dict) and not isinstance(v, list)
    }

    for key in ['game_event', 'possession_event']:
        if frame.get(key):
            result.update(_flatten_dict(frame[key], key))

    player_lists = [
        # ('home', 'homePlayers'),
        # ('away', 'awayPlayers'),
        ('home', 'homePlayersSmoothed'),
        ('away', 'awayPlayersSmoothed'),
    ]

    for team, key in player_lists:
        result[f'{team}_count'] = 0
        if key in frame and frame[key] is not None:
            players = frame[key]
            result[f'{team}_count'] = len(players)

            for player in players:
                if 'jerseyNum' in player:
                    jersey_num = player['jerseyNum']
                    for attr, value in player.items():
                        result[f'{team}_{jersey_num}_{attr}'] = value
                else:
                    logger.warning(f'Found player without jerseyNum in {key}')

    # ballsSmoothed doesn't need to be smoothed, just ball, we'll drop ballsSmoothed
    if 'balls' in frame and frame.get('balls'):
        ball = frame['balls'][0]
        result.update(_flatten_dict(ball, 'ball'))

    return result


def _transform_long(frame: dict[str, Any]) -> list[dict[str, Any]]:
    """
    Transform a single frame dictionary to a long format structure with one row per
    player.

    In this format, each player becomes a separate row with common frame data repeated.
    Ball data and events are included in each row.

    Args:
        frame: A dictionary containing PFF tracking data for one frame

    Returns:
        A list of dictionaries, one per player
    """
    # fmt: off
    skip_keys = [
        'homePlayers', 'awayPlayers', 'balls',
        'homePlayersSmoothed', 'awayPlayersSmoothed', 'ballsSmoothed'
    ]
    # fmt: on

    common_fields = {}
    for k, v in frame.items():
        if k not in skip_keys and not isinstance(v, dict) and not isinstance(v, list):
            common_fields[k] = v

    if 'balls' in frame and frame.get('balls'):
        ball = frame['balls'][0]
        common_fields.update(_flatten_dict(ball, 'ball'))

    for key in ['game_event', 'possession_event']:
        if frame.get(key):
            common_fields.update(_flatten_dict(frame[key], key))

    results = []

    player_lists = [
        # ('home', 'homePlayers'),
        # ('away', 'awayPlayers'),
        ('home', 'homePlayersSmoothed'),
        ('away', 'awayPlayersSmoothed'),
    ]

    for team, key in player_lists:
        if key in frame and frame[key] is not None:
            players = frame[key]
            for player in players:
                player_row = common_fields.copy()
                player_row['team'] = team

                for attr, value in player.items():
                    player_row[f'player_{attr}'] = value

                results.append(player_row)

    return results


def transform_pff_tracks(
    frames: list[dict[str, Any]],
    transform_format: TransformFormat = TransformFormat.WIDE,
) -> list[dict[str, Any]]:
    """
    Transform a list of frame dictionaries into flat structures.

    Args:
        frames: A list of dictionaries containing PFF tracking data
        transform_format: Format for the output data (wide or long)

    Returns:
        In WIDE format: A list of flattened dictionaries (one per frame)
        In LONG format: A list of lists of dictionaries (multiple rows per frame)
    """
    if transform_format not in TransformFormat:
        raise ValueError(f'Invalid transform format: {transform_format}')

    if transform_format == TransformFormat.WIDE:
        return [_transform_wide(frame) for frame in frames]
    else:
        return list(chain.from_iterable(_transform_long(frame) for frame in frames))
