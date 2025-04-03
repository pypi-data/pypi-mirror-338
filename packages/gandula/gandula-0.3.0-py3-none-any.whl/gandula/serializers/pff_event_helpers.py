from datetime import timedelta

from kloppy.domain import (
    Period,
    Point,
    Point3D,
    Team,
)
from kloppy.exceptions import DeserializationError


def get_team_by_id(team_id: int, teams: list[Team]) -> Team:
    """Get a team by its id."""
    if str(team_id) == teams[0].team_id:
        return teams[0]
    elif str(team_id) == teams[1].team_id:
        return teams[1]
    else:
        raise DeserializationError(f'Unknown team_id {team_id}')


def get_team_by_player_id(player_id: int | str, teams: list[Team]) -> Team:
    """Get a team by a player's id."""
    for team in teams:
        for player in team.players:
            if player.player_id == str(player_id):
                return team
    raise DeserializationError(f'Unknown player_id {player_id}')


def get_period_by_id(period_id: int | str, periods: list[Period]) -> Period:
    """Get a period by its id."""
    for period in periods:
        if period.id == int(period_id):
            return period
    raise DeserializationError(f'Unknown period_id {period_id}')


from ..core.logging import get_logger

logger = get_logger(__name__)


def get_period_by_timestamp(timestamp: timedelta, periods: list[Period]) -> Period:
    """Get a period by its timestamp."""
    for period in periods:
        if period.start_timestamp <= timestamp <= period.end_timestamp:
            return period
    return 2
    # logger.error(evt_timestamp=timestamp, period=[(period.start_timestamp, period.end_timestamp) for period in periods])
    raise DeserializationError(f'Unknown timestamp {timestamp}')


def parse_coordinates(coordinates: list[float], fidelity_version: int) -> Point:
    """Parse coordinates into a kloppy Point.

    Coordinates are cell-based, so 1,1 (low-granularity) or 0.1,0.1
    (high-granularity) is the top-left square 'yard' of the field (in
    landscape), even though 0,0 is the true coordinate of the corner flag.

    [1, 120] x [1, 80]
    +-----+-----+
    | 1,1 | 2,1 |
    +-----+-----+
    | 1,2 | 2,2 |
    +-----+-----+
    """
    cell_side = 0.1 if fidelity_version == 2 else 1.0
    cell_relative_center = cell_side / 2
    if len(coordinates) == 2:
        return Point(
            x=coordinates[0] - cell_relative_center,
            y=coordinates[1] - cell_relative_center,
        )
    elif len(coordinates) == 3:
        # A coordinate in the goal frame, only used for the end location of
        # Shot events. The y-coordinates and z-coordinates are always detailed
        # to a tenth of a yard.
        return Point3D(
            x=coordinates[0] - cell_relative_center,
            y=coordinates[1] - 0.05,
            z=coordinates[2] - 0.05,
        )
    else:
        raise DeserializationError(f'Unknown coordinates format: {coordinates}')
