from datetime import timedelta
from itertools import chain, zip_longest
from typing import NamedTuple

from kloppy.domain import (
    DatasetFlag,
    EventDataset,
    Ground,
    Metadata,
    Orientation,
    Period,
    Player,
    Provider,
    Team,
)
from kloppy.exceptions import DeserializationError
from kloppy.infra.serializers.event.deserializer import EventDataDeserializer
from kloppy.utils import performance_logging

from ..core.logging import get_logger
from . import pff_event_specification as PFF
from .pff_event_specification import position_types_mapping

logger = get_logger(__name__)


class PFFInputs(NamedTuple):
    event_data: dict


# TODO: Move all fixes (periods, teams, etc) BEFORE deserializing
class PFFDeserializer(EventDataDeserializer[PFFInputs]):
    def provider(self):
        return Provider.OTHER

    def deserialize(self, inputs: PFFInputs, additional_metadata) -> EventDataset:
        self.transformer = self.get_transformer(
            pitch_length=105.0, pitch_width=68.0, provider=Provider.KLOPPY
        )

        with performance_logging('load data', logger=logger):
            raw_game, raw_events, data_version = self.load_data(inputs)
        logger.info(f'determined version {data_version} from event data')

        with performance_logging('parse teams and players', logger=logger):
            teams = self.create_teams_and_players(raw_game)

        with performance_logging('parse periods', logger=logger):
            periods = self.create_periods(raw_events)

        with performance_logging('parse events', logger=logger):
            events = []
            for raw_event in chain.from_iterable(raw_events.values()):
                new_events = (
                    raw_event.set_version(data_version)
                    .set_refs(periods, teams, raw_events)
                    .deserialize(self.event_factory)
                )
                for event in new_events:
                    if self.should_include_event(event):
                        # event = self.transformer.transform_event(event)
                        events.append(event)

        metadata = Metadata(
            teams=teams,
            periods=periods,
            pitch_dimensions=self.transformer.get_to_coordinate_system().pitch_dimensions,
            frame_rate=None,
            orientation=Orientation.ACTION_EXECUTING_TEAM,
            flags=DatasetFlag.BALL_OWNING_TEAM | DatasetFlag.BALL_STATE,
            score=None,
            provider=Provider.OTHER,
            coordinate_system=self.transformer.get_to_coordinate_system(),
            **additional_metadata,
        )

        return EventDataset(metadata=metadata, records=events)

    def load_data(self, inputs: PFFInputs):
        raw_events = {}
        version = ''

        raw_game = inputs.event_data

        with performance_logging('sort events', logger=logger):
            raw_game['gameEvents'] = sorted(
                raw_game['gameEvents'], key=lambda x: x['startTime']
            )

        for event in raw_game['gameEvents']:
            raw_events[event['id']] = PFF.event_decoder(event)
            if not version:
                version = event.get('version')

        version = PFF.Version(version=version)

        return raw_game, raw_events, version

    def create_teams_and_players(self, raw_game):
        rosters = raw_game.get('rosters')

        home_team = raw_game['homeTeam']
        away_team = raw_game['awayTeam']

        home_team['players'] = [
            player for player in rosters if player['team']['id'] == home_team.get('id')
        ]
        away_team['players'] = [
            player for player in rosters if player['team']['id'] == away_team.get('id')
        ]

        player_positions = {
            player['player']['id']: position_types_mapping[player['positionGroupType']]
            for player in rosters
        }

        def create_team(team_players, ground_type):
            team = Team(
                team_id=team_players['id'],
                name=team_players['name'],
                ground=ground_type,
            )
            team.players = [
                Player(
                    player_id=str(player['player']['id']),
                    team=team,
                    first_name=player['player']['firstName'],
                    last_name=player['player']['lastName'],
                    name=player['player']['nickname'],
                    jersey_no=int(player['shirtNumber']),
                    starting=player['started'],
                    starting_position=player_positions.get(player['player']['id']),
                )
                for player in team_players['players']
            ]
            return team

        home_team = create_team(home_team, Ground.HOME)
        away_team = create_team(away_team, Ground.AWAY)

        return [home_team, away_team]

    def create_periods(self, raw_events) -> list[Period]:
        half_start_events = {}
        half_end_events = {}

        for event in chain.from_iterable(raw_events.values()):
            event_type = PFF.EVENT_TYPE(event.raw_event['gameEventType'])
            period = event.raw_event['period']

            # There is a bug where SECOND_HALF_KICKOFF period is 1
            # easier to control directly and fix this
            fix_kickoff_period = {
                PFF.EVENT_TYPE.FIRST_HALF_KICKOFF: 1,
                PFF.EVENT_TYPE.SECOND_HALF_KICKOFF: 2,
                PFF.EVENT_TYPE.EXTRA_1_KICKOFF: 3,
                PFF.EVENT_TYPE.EXTRA_2_KICKOFF: 4,
            }

            if event_type in [
                PFF.EVENT_TYPE.FIRST_HALF_KICKOFF,
                PFF.EVENT_TYPE.SECOND_HALF_KICKOFF,
                PFF.EVENT_TYPE.EXTRA_1_KICKOFF,
                PFF.EVENT_TYPE.EXTRA_2_KICKOFF,
            ]:
                period = fix_kickoff_period[event_type]
                event.raw_event['period'] = period
                half_start_events[int(period)] = event.raw_event
            elif event_type == PFF.EVENT_TYPE.END_OF_HALF:
                half_end_events[int(period)] = event.raw_event

        periods = []
        for start_event, end_event in zip_longest(
            half_start_events.values(), half_end_events.values()
        ):
            if start_event is None or end_event is None:
                raise DeserializationError(
                    'Failed to determine start and end time of periods.'
                )

            period = Period(
                id=int(start_event['period']),
                start_timestamp=timedelta(seconds=start_event['startTime']),
                end_timestamp=timedelta(seconds=end_event['startTime']),
            )

            periods.append(period)

        return periods
