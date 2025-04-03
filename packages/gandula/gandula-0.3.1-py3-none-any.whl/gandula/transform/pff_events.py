"""Transform raw PFF event data into flattened structures for DataFrames.

This module provides functionality to transform PFF event data into flat structures
suitable for analysis in pandas DataFrames. It handles both game-level events and
nested event data like possessions, ball carries, challenges, etc.
"""

from enum import Enum
from typing import Any

from ..core.logging import get_logger
from .pff_events_mappings import EVENTS_FIELD_MAP

logger = get_logger(__name__)


POSSESSION_EVENT_TYPES = [
    'ballCarryEvent',
    'challengeEvent',
    'clearanceEvent',
    'crossEvent',
    'reboundEvent',
    'shootingEvent',
    'passingEvent',
]


class TransformFormat(str, Enum):
    """Format options for the transformed output."""

    WIDE = 'wide'  # One row per event with nested data as columns
    LONG = 'long'  # Multiple rows per event (one per possession/sub-event)


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
            elif isinstance(v, list):
                # For lists, add a count and flatten each item with an index
                result[f'{key}_count'] = len(v)
                for i, item in enumerate(v):
                    if isinstance(item, dict):
                        result.update(_flatten_dict(item, f'{key}_{i}'))
                    else:
                        result[f'{key}_{i}'] = item
            else:
                result[key] = v
    except AttributeError:
        logger.error(f'Error flattening dictionary: {d}')
        raise

    return result


def transform_match_metadata(match: dict[str, Any]) -> dict[str, Any]:
    """Extract match metadata into a flat dictionary."""
    metadata_field_map = {
        # Match identification
        'id': 'match_id',
        'date': 'match_date',
        'week': 'match_week',
        'venue': 'match_venue',
        'season': 'season',
        # Competition
        'competition_id': 'competition_id',
        'competition_name': 'competition_name',
        # Stadium
        'stadium_id': 'stadium_id',
        'stadium_name': 'stadium_name',
        'stadium_pitch_length': 'pitch_length',
        'stadium_pitch_width': 'pitch_width',
        'stadium_pitch_grass_type': 'pitch_grass_type',
        # Video
        'video_fps': 'video_fps',
        # Match timing
        'startPeriod1': 'period_1_start',
        'endPeriod1': 'period_1_end',
        'startPeriod2': 'period_2_start',
        'endPeriod2': 'period_2_end',
        # Helps with conversions and maybe tracking
        'homeTeamStartLeft': 'home_start_left',
        'homeTeamStartLeftExtraTime': 'home_start_left_extra',
        'homeTeam_id': 'home_team_id',
        'homeTeam_name': 'home_team_name',
        'homeTeamKit_primaryColor': 'home_kit_primary_color',
        'homeTeamKit_primaryTextColor': 'home_kit_primary_text_color',
        'homeTeamKit_secondaryColor': 'home_kit_secondary_color',
        'homeTeamKit_secondaryTextColor': 'home_kit_secondary_text_color',
        'awayTeam_id': 'away_team_id',
        'awayTeam_name': 'away_team_name',
        'awayTeamKit_primaryColor': 'away_kit_primary_color',
        'awayTeamKit_primaryTextColor': 'away_kit_primary_text_color',
        'awayTeamKit_secondaryColor': 'away_kit_secondary_color',
        'awayTeamKit_secondaryTextColor': 'away_kit_secondary_text_color',
    }

    skip_keys = [
        'complete',
        'gameEvents',
        'stadium',
        'videos',
        'period1',
        'period2',
        'rosters',
    ]
    metadata = {k: v for k, v in match.items() if k not in skip_keys}

    # Select which pitch to keep...
    if match.get('stadium'):
        metadata['stadium_name'] = match['stadium']['name']
        metadata['stadium_id'] = match['stadium']['id']

        # if match['stadium'].get('pitches'):
        #     for pitch in match['stadium']['pitches']:
        #         if pitch['startDate'] <= match['date'] <= pitch['endDate']:
        #             metadata.update({
        #                 'pitch_length': pitch['length'],
        #                 'pitch_width': pitch['width'],
        #             })
        #             break

    if match.get('videos'):
        video = match['videos'][0]
        metadata.update(
            {
                'video_fps': video['fps'],
            }
        )

    flat_metadata = _flatten_dict(metadata)

    return {
        new_name: flat_metadata.get(original_name)
        for original_name, new_name in metadata_field_map.items()
    }


def transform_player_metadata(rosters: list[dict[str, Any]]) -> list[dict[str, Any]]:
    player_field_map = {
        # Match context
        'game_id': 'match_id',
        'team_id': 'team_id',
        'team_name': 'team_name',
        'started': 'started',
        'shirtNumber': 'shirt_number',
        'positionGroupType': 'position_group_type',
        # Basic player info
        'player_id': 'player_id',
        'player_firstName': 'first_name',
        'player_lastName': 'last_name',
        'player_nickname': 'nickname',
        'player_dob': 'dob',
        'player_preferredFoot': 'preferred_foot',
        # Nationality
        'player_nationality_country': 'nationality',
        'player_secondNationality_country': 'second_nationality_country',
    }

    players = []

    for roster in rosters:
        all_fields = _flatten_dict(roster)

        player_data = {
            new_name: all_fields.get(original_name)
            for original_name, new_name in player_field_map.items()
        }

        players.append(player_data)

    return players


def _transform_game_event(event: dict[str, Any]) -> dict[str, Any]:
    """Process a game event, excluding specified fields and flattening the rest."""
    game_event_exclude_fields = {
        'advantageType',
        'defenderLocations',
        'offenderLocations',
        'videoMissing',
        'video',
        'videoAngleType',
        'subType',
        'heightType',
        'endType',
        'possessionEvents',
        'scoreValue',
    }

    filtered_event = {
        k: v for k, v in event.items() if k not in game_event_exclude_fields
    }

    return _flatten_dict(filtered_event, 'game_event')


def _transform_possession_event(event: dict[str, Any]) -> dict[str, Any]:
    """Process a possession event, excluding specified fields and flattening."""
    possession_event_exclude_fields = {
        'lastInGameEvent',
        'game',
        'defenders',
        'video',
        'period',
        'fouls',
    }

    filtered_event = {
        k: v
        for k, v in event.items()
        if k not in possession_event_exclude_fields and k not in POSSESSION_EVENT_TYPES
    }

    return _flatten_dict(filtered_event, 'possession_event')


def _transform_event_type(
    event_type: str, event_data: dict[str, Any]
) -> dict[str, Any]:
    """Process a specific event type (pass, shot, etc.) into flattened fields."""
    prefix = event_type.replace('Event', '')
    return _flatten_dict(event_data, prefix)


def _transform_foul(foul: dict[str, Any]) -> dict[str, Any]:
    """Process a foul inside a possession event into flattened fields."""
    return _flatten_dict(foul, 'foul')


def transform_events(game_events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Transform PFF game events into flattened rows.

    Args:
        game_events: List of game event dictionaries

    Returns:
        List of dictionaries, each representing a flattened event row
    """
    transformed_rows = []

    for game_event in game_events:
        base_event_data = _transform_game_event(game_event)

        possession_events = game_event.get('possessionEvents', [])

        if not possession_events:
            transformed_rows.append(base_event_data)

        for possession_event in possession_events:
            possession_data = _transform_possession_event(possession_event)

            base_row_data = {**base_event_data, **possession_data}

            for event_type in POSSESSION_EVENT_TYPES:
                if event_data := possession_event.get(event_type):
                    event_row = base_row_data.copy()
                    event_row.update(_transform_event_type(event_type, event_data))
                    transformed_rows.append(event_row)

            for foul in possession_event.get('fouls', []):
                foul_row = base_row_data.copy()
                foul_row.update(_transform_foul(foul))
                transformed_rows.append(foul_row)

    mapped_rows = []

    for row in transformed_rows:
        mapped_row = {}

        for key, value in row.items():
            mapped_key = EVENTS_FIELD_MAP.get(key, key)
            mapped_row[mapped_key] = value

        mapped_rows.append(mapped_row)

    return mapped_rows
