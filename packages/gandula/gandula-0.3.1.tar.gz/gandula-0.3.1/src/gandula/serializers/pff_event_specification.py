from datetime import timedelta
from enum import Enum, EnumMeta
from typing import NamedTuple

from kloppy.domain import (
    BallState,
    BodyPart,
    BodyPartQualifier,
    CardQualifier,
    CardType,
    CarryResult,
    DuelQualifier,
    DuelResult,
    DuelType,
    Event,
    EventFactory,
    GoalkeeperActionType,
    GoalkeeperQualifier,
    InterceptionResult,
    PassQualifier,
    PassResult,
    PassType,
    PositionType,
    SetPieceQualifier,
    SetPieceType,
    ShotResult,
    TakeOnResult,
)
from kloppy.exceptions import DeserializationError
from pydantic import BaseModel

from ..core.logging import get_logger
from .pff_event_helpers import (
    get_period_by_timestamp,
    get_team_by_id,
    get_team_by_player_id,
)

logger = get_logger(__name__)

# TODOs:
#  - [ ] Function to extract the event duration... impossibru? (forward pass?)
#  - [ ] Fix period calculation for SUBS between periods
#  - [ ] Fix ball_owning_team (who the hell owns it in PFF without a double pass?)
#  - [ ] Goalkeeping events from Rebound will need a double pass for bodypart
#  - [ ] Calculate duration of certain events like ball carry and passes


class UnderPressureQualifier(BaseModel):
    name: str = 'under_pressure'
    value: bool

    def to_dict(self):
        return {'is_under_pressure': self.value}


class Version(NamedTuple):
    version: str


position_types_mapping: dict[str, PositionType] = {
    'GK': PositionType.Goalkeeper,  # Provider: Goalkeeper
    'RB': PositionType.RightBack,  # Provider: Right Back
    'RCB': PositionType.RightCenterBack,  # Provider: Right Center Back
    'CB': PositionType.CenterBack,  # Provider: Center Back
    'LCB': PositionType.LeftCenterBack,  # Provider: Left Center Back
    'MCB': PositionType.CenterBack,  # Provider: Mid Center Back
    'LB': PositionType.LeftBack,  # Provider: Left Back
    'RWB': PositionType.RightWingBack,  # Provider: Right Wing Back
    'LWB': PositionType.LeftWingBack,  # Provider: Left Wing Back
    'D': PositionType.Defender,  # Provider: Defender
    'DM': PositionType.DefensiveMidfield,  # Provider: Defensive Midfield
    'M': PositionType.Midfielder,  # Provider: Midfielder
    'RM': PositionType.RightMidfield,  # Provider: Right Midfielder
    'CM': PositionType.CenterMidfield,  # Provider: Center Midfield
    'LM': PositionType.LeftMidfield,  # Provider: Left Midfield
    'RW': PositionType.RightWing,  # Provider: Right Wing
    'AM': PositionType.AttackingMidfield,  # Provider: Attacking Midfield
    'LW': PositionType.LeftWing,  # Provider: Left Wing
    'CF': PositionType.Striker,  # Provider: Center Forward (mapped to Striker)
    'F': PositionType.Attacker,  # Provider: Forward (mapped to Attacker)
}


class TypesEnumMeta(EnumMeta):
    def __call__(cls, value, *args, **kw):
        if isinstance(value, dict):
            if value['id'] not in cls._value2member_map_:
                raise ValueError(
                    'Unknown PFF {}: {}/{}'.format(
                        (cls.__qualname__.replace('_', ' ').replace('.', ' ').title()),
                        value['id'],
                        value['name'],
                    )
                )
            value = cls(value['id'])
        elif value not in cls._value2member_map_:
            raise ValueError(
                'Unknown PFF {}: {}'.format(
                    (cls.__qualname__.replace('_', ' ').replace('.', ' ').title()),
                    value,
                )
            )
        return super().__call__(value, *args, **kw)


class EVENT_TYPE(Enum, metaclass=TypesEnumMeta):
    """The list of game event types used in PFF data."""

    FIRST_HALF_KICKOFF = 'FIRSTKICKOFF'
    SECOND_HALF_KICKOFF = 'SECONDKICKOFF'
    EXTRA_1_KICKOFF = 'THIRDKICKOFF'
    EXTRA_2_KICKOFF = 'FOURTHKICKOFF'
    GAME_CLOCK_OBSERVATION = 'CLK'
    END_OF_HALF = 'END'
    GROUND = 'G'
    PLAYER_OFF = 'OFF'
    PLAYER_ON = 'ON'
    POSSESSION = 'OTB'
    BALL_OUT_OF_PLAY = 'OUT'
    PAUSE_OF_GAME_TIME = 'PAU'
    SUB = 'SUB'
    VIDEO = 'VID'


class POSSESSION_EVENT_TYPE(Enum, metaclass=TypesEnumMeta):
    """The list of possession event types used in PFF data."""

    BALL_CARRY = 'BC'
    CHALLENGE = 'CH'
    CLEARANCE = 'CL'
    CROSS = 'CR'
    PASS = 'PA'
    REBOUND = 'RE'
    SHOT = 'SH'


class BODYPART(Enum, metaclass=TypesEnumMeta):
    """The list of body parts used in PFF data."""

    BACK = 'BA'
    BOTTOM = 'BO'
    TWO_HAND_CATCH = 'CA'
    CHEST = 'CH'
    HEAD = 'HE'
    LEFT_FOOT = 'L'
    LEFT_ARM = 'LA'
    LEFT_BACK_HEEL = 'LB'
    LEFT_SHOULDER = 'LC'
    LEFT_HAND = 'LH'
    LEFT_KNEE = 'LK'
    LEFT_SHIN = 'LS'
    LEFT_THIGH = 'LT'
    TWO_HAND_PALM = 'PA'
    TWO_HAND_PUNCH = 'PU'
    RIGHT_FOOT = 'R'
    RIGHT_ARM = 'RA'
    RIGHT_BACK_HEEL = 'RB'
    RIGHT_SHOULDER = 'RC'
    RIGHT_HAND = 'RH'
    RIGHT_KNEE = 'RK'
    RIGHT_SHIN = 'RS'
    RIGHT_THIGH = 'RT'
    TWO_HANDS = 'TWOHANDS'
    VIDEO_MISSING = 'VM'


class SETPIECE(Enum, metaclass=TypesEnumMeta):
    """The list of set piece types used in PFF data."""

    CORNER = 'C'
    DROP_BALL = 'D'
    FREE_KICK = 'F'
    GOAL_KICK = 'G'
    KICK_OFF = 'K'
    PENALTY = 'P'
    THROW_IN = 'T'


class EVENT:
    """Base class for PFF events.

    This class is used to deserialize PFF events into kloppy events.
    This default implementation is used for all events that do not have a
    specific implementation. They are deserialized into a generic event.

    Args:
        raw_event: The raw JSON event.
        data_version: The version of the StatsBomb data.
    """

    def __init__(self, raw_event: dict, raw_possession_event: dict | None = None):
        self.raw_event = raw_event
        self.raw_possession_event = raw_possession_event

    def set_version(self, data_version: Version):
        self.version = data_version.version
        return self

    def set_refs(self, periods, teams, events):
        self.teams = teams
        # PFF's period has a bug and tags the event period's in a wrong way.
        # I have reported to Alexander, let's see if it's fixed. We can use
        # startTime to determine the period safely until it gets corrected.
        # TODO: Solve for interval SUB -- event happens between the periods
        self.period = get_period_by_timestamp(
            timedelta(seconds=self.raw_event['startTime']), periods
        )
        self.team = (
            get_team_by_id(self.raw_event['team']['id'], teams)
            if self.raw_event.get('team')
            else None
        )
        self.possession_team = (
            get_team_by_id(self.raw_event['team']['id'], teams)
            if self.raw_event.get('team')
            else None
        )
        self.player = (
            self.team.get_player_by_id(self.raw_event['player']['id'])
            if self.raw_event.get('player') and self.team
            else None
        )
        self.related_events = [
            events.get(event_id)
            for event_id in self.raw_event.get('related_events', [])
        ]
        return self

    def deserialize(self, event_factory: EventFactory) -> list[Event]:
        """Deserialize the event.

        Args:
            event_factory: The event factory to use to build the event.

        Returns:
            A list of kloppy events.
        """
        generic_event_kwargs = self._parse_generic_kwargs()

        # create events
        base_events = self._create_events(event_factory, **generic_event_kwargs)
        # ball_out_events = self._create_ball_out_event(
        #     event_factory, **generic_event_kwargs
        # )

        # add qualifiers
        for event in base_events:
            self._add_set_piece_qualifiers(event)
            self._add_under_pressure_qualifier(event)
        # for event in base_events + ball_out_events:
        #     self._add_play_pattern_qualifiers(event)

        # return events (note: order is important)
        return base_events  # + ball_out_events

    def _parse_generic_kwargs(self) -> dict:
        return {
            'period': self.period,
            'timestamp': timedelta(seconds=self.raw_event['startTime']),
            'ball_owning_team': self.possession_team,
            'ball_state': BallState.DEAD,
            'event_id': self.raw_event['id'],
            'team': self.team,
            'player': self.player,
            'coordinates': None,
            'raw_event': self.raw_event,
            'statistics': [],
        }

    def _create_shot_event(self, event_factory: EventFactory, **generic_event_kwargs):
        generic_event_kwargs['event_id'] = f"shot-{generic_event_kwargs['event_id']}"
        ...

    def _create_pass_event(): ...

    def _create_gk_event(): ...

    def _add_set_piece_qualifiers(self, event: Event) -> Event:
        if self.raw_event.get('setPieceType'):
            q = _get_set_piece_qualifiers(self.raw_event)
            event.qualifiers = event.qualifiers or []
            event.qualifiers.extend(q)

        return event

    def _add_under_pressure_qualifier(self, event: Event) -> Event:
        if self.raw_event.get('under_pressure'):
            q = UnderPressureQualifier(True)
            event.qualifiers = event.qualifiers or []
            event.qualifiers.append(q)

        return event

    def _build_generic_event(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> Event:
        return event_factory.build_generic(
            result=None,
            qualifiers=None,
            event_name=self.raw_event['gameEventType'],
            **generic_event_kwargs,
        )

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        return [self._build_generic_event(event_factory, **generic_event_kwargs)]


class POSSESSION_EVENT(EVENT):
    def __init__(self, raw_event: dict, raw_possession_event: dict):
        self.raw_event = raw_event
        self.raw_possession_event = raw_possession_event

    def _parse_generic_kwargs(self) -> dict:
        return {
            'period': self.period,
            'timestamp': timedelta(seconds=self.raw_possession_event['startTime']),
            'ball_owning_team': self.possession_team,
            'ball_state': BallState.ALIVE,
            'event_id': f"otb-{self.raw_event['id']}",
            'team': self.team,
            'player': self.player,
            'coordinates': None,
            'raw_event': self.raw_event,
            'statistics': [],
        }

    def _build_generic_event(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> Event:
        generic_event_kwargs['event_id'] = f"otb-{self.raw_event['id']}"
        return event_factory.build_generic(
            result=None,
            qualifiers=None,
            event_name=self.raw_possession_event['possessionEventType'],
            **generic_event_kwargs,
        )


class PASS(POSSESSION_EVENT):
    """PFF Possession Event PA/Pass event."""

    class TYPE(Enum, metaclass=TypesEnumMeta):
        CUTBACK = 'B'
        CREATE_CONTEST = 'C'
        FLICK_ON = 'F'
        LONG_THROW = 'H'
        LONG_PASS = 'L'
        MISS_HIT = 'M'
        BALL_OVER_THE_TOP = 'O'
        STANDARD_PASS = 'S'
        THROUGH_BALL = 'T'
        SWITCH = 'W'

    class OUTCOME(Enum, metaclass=TypesEnumMeta):
        BLOCKED = 'B'
        COMPLETE = 'C'
        DEFENSIVE_INTERCEPTION = 'D'
        INADVERTENT_SHOT_OWN_GOAL = 'G'
        INADVERTENT_SHOT_GOAL = 'I'
        OUT_OF_PLAY = 'O'
        STOPPAGE = 'S'

    class CROSS_TYPE(Enum, metaclass=TypesEnumMeta):
        DRILLED = 'D'
        FLOATED = 'F'
        SWING_IN = 'I'
        SWING_OUT = 'O'
        PLACED = 'P'

    class HEIGHT(Enum, metaclass=TypesEnumMeta):
        GROUND = 1
        LOW = 2
        HIGH = 3

    class TECHNIQUE(Enum, metaclass=TypesEnumMeta):
        THROUGH_BALL = 108
        INSWINGING = 104
        OUTSWINGING = 105
        STRAIGHT = 107

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        team = generic_event_kwargs['team']
        timestamp = generic_event_kwargs['timestamp']
        pass_dict = self.raw_event['pass']

        result = None
        receiver_player = None
        receiver_coordinates = parse_coordinates(
            pass_dict['end_location'],
            self.fidelity_version,
        )
        receive_timestamp = timestamp + timedelta(
            seconds=self.raw_event.get('duration', 0.0)
        )

        if 'outcome' in pass_dict:
            outcome_id = pass_dict['outcome']['id']
            outcome_mapping = {
                PASS.OUTCOME.OUT: PassResult.OUT,
                PASS.OUTCOME.INCOMPLETE: PassResult.INCOMPLETE,
                PASS.OUTCOME.OFFSIDE: PassResult.OFFSIDE,
                PASS.OUTCOME.INJURY_CLEARANCE: PassResult.OUT,
                PASS.OUTCOME.UNKNOWN: None,
            }
            result = outcome_mapping.get(PASS.OUTCOME(outcome_id))
        else:
            result = PassResult.COMPLETE
            receiver_player = team.get_player_by_id(pass_dict['recipient']['id'])

        qualifiers = (
            _get_pass_qualifiers(pass_dict)
            + _get_set_piece_qualifiers(EVENT_TYPE.PASS, pass_dict)
            + _get_body_part_qualifiers(pass_dict)
        )

        pass_event = event_factory.build_pass(
            result=result,
            receive_timestamp=receive_timestamp,
            receiver_coordinates=receiver_coordinates,
            receiver_player=receiver_player,
            qualifiers=qualifiers,
            **generic_event_kwargs,
        )

        # if pass is an interception, insert interception prior to pass event
        if 'type' in pass_dict:
            generic_event_kwargs['event_id'] = (
                f"interception-{generic_event_kwargs['event_id']}"
            )
            type_id = PASS.TYPE(pass_dict['type']['id'])
            if type_id == PASS.TYPE.ONE_TOUCH_INTERCEPTION:
                interception_event = event_factory.build_interception(
                    **generic_event_kwargs,
                    result=InterceptionResult.SUCCESS,
                    qualifiers=None,
                )
                return [interception_event, pass_event]

        return [pass_event]

    def _create_ball_out_event(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        pass_dict = self.raw_event['pass']
        if (
            self.raw_event.get('out', False)
            or 'outcome' in pass_dict
            and PASS.OUTCOME(pass_dict['outcome']) == PASS.OUTCOME.OUT
        ):
            # If there is a related (failed) ball receipt event recorded for
            # the pass, we create the ball out event from that event.
            if any(
                isinstance(related_event, BALL_RECEIPT)
                for related_event in self.related_events
            ):
                return []
            generic_event_kwargs['event_id'] = f"out-{generic_event_kwargs['event_id']}"
            generic_event_kwargs['ball_state'] = BallState.DEAD
            generic_event_kwargs['coordinates'] = parse_coordinates(
                pass_dict['end_location'],
                self.fidelity_version,
            )

            ball_out_event = event_factory.build_ball_out(
                result=None,
                qualifiers=None,
                **generic_event_kwargs,
            )
            return [ball_out_event]
        return []


class BALL_RECEIPT(EVENT):
    """StatsBomb 42/Ball Receipt* event."""

    def _create_ball_out_event(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        for related_event in self.related_events:
            if isinstance(related_event, PASS):
                pass_dict = related_event.raw_event.get('pass', {})
                if (
                    related_event.raw_event.get('out', False)
                    or 'outcome' in pass_dict
                    and PASS.OUTCOME(pass_dict['outcome']) == PASS.OUTCOME.OUT
                ):
                    generic_event_kwargs['event_id'] = (
                        f"out-{generic_event_kwargs['event_id']}"
                    )
                    generic_event_kwargs['ball_state'] = BallState.DEAD
                    generic_event_kwargs['coordinates'] = parse_coordinates(
                        pass_dict['end_location'],
                        self.fidelity_version,
                    )
                    generic_event_kwargs['raw_event'] = related_event.raw_event

                    ball_out_event = event_factory.build_ball_out(
                        result=None,
                        qualifiers=None,
                        **generic_event_kwargs,
                    )
                    return [ball_out_event]
                return []
        return []


class SHOT(POSSESSION_EVENT):
    """PFF Possession Event SH/Shot event."""

    class OUTCOME(Enum, metaclass=TypesEnumMeta):
        ON_TARGET_BLOCKED = 'B'
        OFF_TARGET_BLOCKED = 'C'
        SAVED_OFF_TARGET = 'F'
        GOAL = 'G'
        GOAL_LINE_CLEARANCE = 'L'
        OFF_TARGET = 'O'
        ON_TARGET = 'S'

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        shot_dict = self.raw_possession_event['shootingEvent']

        outcome_id = shot_dict['shotOutcomeType']

        if outcome_id is None:
            # Skip if there's no outcome, leave it as generic
            # TODO: Add some sort of message indicating reason?
            return [self._build_generic_event(event_factory, **generic_event_kwargs)]

        # TODO: Fix shots that hit the post. Look for 'G' event type coming after shot
        shot_result = _pff_shot_outcome_to_kloppy_shot_result(outcome_id)

        pff_body_type = shot_dict.get('shotBodyType')
        qualifiers = _get_line_player_body_part_qualifier(pff_body_type)

        # Redo team and player
        shot_player = shot_dict.get('shooterPlayer')
        if not shot_player:
            # not good enough... skip when theres no shooter player
            return [self._build_generic_event(event_factory, **generic_event_kwargs)]

        events = []

        shot_player_id = shot_player['id']
        team = get_team_by_player_id(shot_player_id, self.teams)
        player = team.get_player_by_id(shot_player_id)

        shot_kwargs = generic_event_kwargs.copy()
        shot_kwargs['team'] = team
        shot_kwargs['player'] = player

        # TODO: Add shot end-location
        shot_event = event_factory.build_shot(
            result=shot_result,
            qualifiers=qualifiers,
            result_coordinates=None,
            **shot_kwargs,
        )

        events.append(shot_event)

        # If there's a saver keeper, add him with a save.
        # Later, maybe look for a nearby rebound event with the save details
        # like bodypart, correct time, etc
        if shot_dict['saverPlayer'] is not None:
            keeper_id = shot_dict['saverPlayer']['id']
            keeper_team = get_team_by_player_id(keeper_id, self.teams)
            keeper = keeper_team.get_player_by_id(keeper_id)

            gk_kwargs = generic_event_kwargs.copy()
            gk_kwargs['team'] = keeper_team
            gk_kwargs['player'] = keeper

            pff_body_type = shot_dict['keeperTouchType']
            try:
                body_part_qualifier = _get_gk_body_part_qualifiers(pff_body_type)
            except ValueError:
                body_part_qualifier = []

            gk_qualifier = []
            if outcome_id == SHOT.OUTCOME.GOAL:
                gk_qualifier.append(
                    GoalkeeperQualifier(value=GoalkeeperActionType.SAVE_ATTEMPT)
                )
            elif outcome_id in [SHOT.OUTCOME.ON_TARGET, SHOT.OUTCOME.SAVED_OFF_TARGET]:
                gk_qualifier.append(
                    GoalkeeperQualifier(value=GoalkeeperActionType.SAVE)
                )

            # If there's a on_target_blocked or off_target_blocked, there might
            # be a save or save_attempt by the keeper if there is a rebound
            # event, by the keeper, nearby this shot event.

            qualifiers = body_part_qualifier + gk_qualifier
            gk_event = event_factory.build_goalkeeper_event(
                result=None,
                qualifiers=(qualifiers if qualifiers else None),
                **gk_kwargs,
            )

            events.append(gk_event)

        return events

    def _create_ball_out_event(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        shot_dict = self.raw_event['shot']
        if (
            self.raw_event.get('out', False)
            or 'outcome' in shot_dict
            and SHOT.OUTCOME(shot_dict['outcome']) == SHOT.OUTCOME.OFF_TARGET
        ):
            # If there is a related goalkeeper event recorded for
            # the shot, we create the ball out event from that event.
            if any(
                isinstance(related_event, GOALKEEPER)
                for related_event in self.related_events
            ):
                return []
            generic_event_kwargs['event_id'] = f"out-{generic_event_kwargs['event_id']}"
            generic_event_kwargs['ball_state'] = BallState.DEAD
            generic_event_kwargs['coordinates'] = parse_coordinates(
                shot_dict['end_location'],
                self.fidelity_version,
            )

            ball_out_event = event_factory.build_ball_out(
                result=None,
                qualifiers=None,
                **generic_event_kwargs,
            )
            return [ball_out_event]
        return []


class INTERCEPTION(EVENT):
    """StatsBomb 10/Interception event."""

    class OUTCOME(Enum, metaclass=TypesEnumMeta):
        LOST = 1
        WON = 4
        LOST_IN_PLAY = 13
        LOST_OUT = 14
        SUCCESS = 15
        SUCCESS_IN_PLAY = 16
        SUCCESS_OUT = 17

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        interception_dict = self.raw_event.get('interception', {})

        outcome = interception_dict.get('outcome', {})
        outcome_id = INTERCEPTION.OUTCOME(outcome)
        if outcome_id in [
            INTERCEPTION.OUTCOME.LOST_OUT,
            INTERCEPTION.OUTCOME.SUCCESS_OUT,
        ]:
            result = InterceptionResult.OUT
        elif outcome_id in [
            INTERCEPTION.OUTCOME.WON,
            INTERCEPTION.OUTCOME.SUCCESS,
            INTERCEPTION.OUTCOME.SUCCESS_IN_PLAY,
        ]:
            result = InterceptionResult.SUCCESS
        elif outcome_id in [
            INTERCEPTION.OUTCOME.LOST,
            INTERCEPTION.OUTCOME.LOST_IN_PLAY,
        ]:
            result = InterceptionResult.LOST
        else:
            raise DeserializationError(
                f"Unknown interception outcome: {outcome.get('name')}({outcome_id})"
            )

        interception_event = event_factory.build_interception(
            result=result,
            qualifiers=None,
            **generic_event_kwargs,
        )

        return [interception_event]

    def _create_ball_out_event(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        interception_dict = self.raw_event.get('interception', {})
        if (
            self.raw_event.get('out', False)
            or 'outcome' in interception_dict
            and INTERCEPTION.OUTCOME(interception_dict['outcome'])
            in [
                INTERCEPTION.OUTCOME.LOST_OUT,
                INTERCEPTION.OUTCOME.SUCCESS_OUT,
            ]
        ):
            generic_event_kwargs['event_id'] = f"out-{generic_event_kwargs['event_id']}"
            generic_event_kwargs['ball_state'] = BallState.DEAD
            ball_out_event = event_factory.build_ball_out(
                result=None,
                qualifiers=None,
                **generic_event_kwargs,
            )
            return [ball_out_event]
        return []


class OWN_GOAL_AGAINST(EVENT):
    """StatsBomb 20/Own goal against event."""

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        shot_event = event_factory.build_shot(
            result=ShotResult.OWN_GOAL,
            qualifiers=None,
            **generic_event_kwargs,
        )
        return [shot_event]


class OWN_GOAL_FOR(EVENT):
    """StatsBomb 25/Own goal for event."""

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        return []


class CLEARANCE(POSSESSION_EVENT):
    """PFF Possession Event CL/Clearance event."""

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        clearance_dict = self.raw_possession_event['clearanceEvent']
        clearance_player = clearance_dict.get('clearancePlayer', {})
        clearance_player_id = clearance_player.get('id')

        if not clearance_player or not clearance_player_id:
            return []

        team = get_team_by_player_id(clearance_player_id, self.teams)
        player = team.get_player_by_id(clearance_player_id)

        if not player:
            return []

        generic_event_kwargs['team'] = team
        generic_event_kwargs['player'] = player

        pff_body_type = clearance_dict.get('clearanceBodyType')

        # TODO: Fix when a GOALKEEPER becomes a field player (probably ask PFF)
        if player.starting_position == PositionType.Goalkeeper:
            body_part_qualifier = _get_gk_body_part_qualifiers(pff_body_type)

            gk_qualifier = []
            if pff_body_type in [
                BODYPART.TWO_HANDS,
                BODYPART.TWO_HAND_PUNCH,
                BODYPART.TWO_HAND_PALM,
                BODYPART.RIGHT_ARM,
                BODYPART.LEFT_ARM,
                BODYPART.RIGHT_SHOULDER,
                BODYPART.LEFT_SHOULDER,
                BODYPART.RIGHT_HAND,
                BODYPART.LEFT_HAND,
            ]:
                # Assuming any clearance with hands/arms by the GK is a punch
                gk_qualifier = [GoalkeeperQualifier(value=GoalkeeperActionType.PUNCH)]

            qualifiers = body_part_qualifier + gk_qualifier

            gk_event = event_factory.build_goalkeeper_event(
                result=None,
                qualifiers=qualifiers,
                **generic_event_kwargs,
            )

            return [gk_event]

        qualifiers = _get_line_player_body_part_qualifier(pff_body_type)

        clearance_event = event_factory.build_clearance(
            result=None,
            qualifiers=qualifiers,
            **generic_event_kwargs,
        )

        return [clearance_event]


class REBOUND(POSSESSION_EVENT):
    """PFF Possession Event RE/Rebound event."""

    class OUTCOME(Enum, metaclass=TypesEnumMeta):
        INADVERTENT_SHOT_GOAL = 'A'
        INADVERTENT_SHOT_OWN_GOAL = 'D'
        PLAYER = 'P'
        RETAIN = 'R'
        OUT_OF_TOUCH = 'T'

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        rebound_dict = self.raw_possession_event['reboundEvent']

        rebound_player = rebound_dict.get('reboundPlayer', {})
        rebound_player_id = rebound_player.get('id')

        if not rebound_player or not rebound_player_id:
            return [self._build_generic_event(event_factory, **generic_event_kwargs)]

        team = get_team_by_player_id(rebound_player_id, self.teams)
        player = team.get_player_by_id(rebound_player_id)

        if not player:
            return [self._build_generic_event(event_factory, **generic_event_kwargs)]

        generic_event_kwargs['team'] = team
        generic_event_kwargs['player'] = player

        pff_body_part = rebound_dict.get('reboundBodyType')
        outcome = REBOUND.OUTCOME(pff_body_part)

        events = []

        if outcome == REBOUND.OUTCOME.INADVERTENT_SHOT_GOAL:
            # Should become a shot event by the reboundPlayer
            shot_outcome = rebound_dict.get('shotOutcomeType')
            shot_result = _pff_shot_outcome_to_kloppy_shot_result(shot_outcome)

            shot_kwargs = generic_event_kwargs.copy()
            shot_kwargs['event_id'] = f"shot-{generic_event_kwargs['event_id']}"

            body_part_qualifier = _get_line_player_body_part_qualifier(pff_body_part)

            shot_event = event_factory.build_shot(
                result=shot_result,
                qualifiers=body_part_qualifier,
                **shot_kwargs,
            )

            events.append(shot_event)

            # If shot was saved, should become a goalkeeper save event,
            # if keeperPlayer is set (or we can search for the goalkeeper)
            if shot_result == ShotResult.SAVED and rebound_dict.get('keeperPlayer'):
                gk_player = rebound_dict['keeperPlayer']

                gk_team = get_team_by_player_id(gk_player['id'], self.teams)
                gk = gk_team.get_player_by_id(gk_player['id'])

                gk_kwargs = generic_event_kwargs.copy()
                gk_kwargs['team'] = gk_team
                gk_kwargs['player'] = gk
                gk_kwargs['event_id'] = f"goalkeeper-{generic_event_kwargs['event_id']}"

                # There is no body part in the event for the line player.
                # The goalkeeper rebound event will have the save.
                gk_event = event_factory.build_goalkeeper_event(
                    result=GoalkeeperActionType.SAVE,
                    qualifiers=None,
                    **gk_kwargs,
                )
                events.append(gk_event)

        elif outcome == REBOUND.OUTCOME.INADVERTENT_SHOT_OWN_GOAL:
            ...
        elif outcome == REBOUND.OUTCOME.RETAIN:
            # Could retain == recovery?
            ...

        # Rebound should become

        # if player.starting_position == PositionType.Goalkeeper:
        #     body_part_qualifier = _get_gk_body_part_qualifiers(rebound_body_part)
        #     if

        rebound_event = self._build_generic_event(event_factory, **generic_event_kwargs)

        return events


class MISCONTROL(EVENT):
    """StatsBomb 38/Miscontrol event."""

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        miscontrol_event = event_factory.build_miscontrol(
            result=None,
            qualifiers=None,
            **generic_event_kwargs,
        )

        return [miscontrol_event]


class CARRY(POSSESSION_EVENT):
    """PFF Possession Event BC/Ball Carry event."""

    class BALL_CARRY_TYPE(Enum, metaclass=TypesEnumMeta):
        CARRY = 'C'
        DRIBBLE = 'D'
        TOUCH = 'T'

    class CARRY_TYPE(Enum, metaclass=TypesEnumMeta):
        LINE_BREAK = 'B'
        CHANGE_OF_DIRECTION = 'C'
        DRIVE_WITH_INTENT = 'D'
        LONG_CARRY = 'L'

    class OUTCOME(Enum, metaclass=TypesEnumMeta):
        RETAIN = 'R'
        STOPPAGE = 'S'
        BALL_LOSS = 'L'
        LEADS_INTO_CHALLENGE = 'C'

    class TOUCH_OUTCOME(Enum, metaclass=TypesEnumMeta):
        INADVERTENT_SHOT_AT_GOAL = 'A'
        CHALLENGE = 'C'
        INADVERTENT_SHOT_OWN_GOAL = 'D'
        GOAL = 'G'
        OUT_OF_PLAY = 'O'
        PLAYER = 'P'
        RETAIN = 'R'
        OWN_GOAL = 'W'

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        carry_dict = self.raw_possession_event['ballCarryEvent']
        carry_outcome_id = carry_dict['ballCarryOutcome']
        touch_outcome_id = carry_dict['touchOutcomeType']
        ball_carrier = carry_dict['ballCarrierPlayer']

        # Drop all ball carry events without carry and touch outcomes
        if (not carry_outcome_id and not touch_outcome_id) or not ball_carrier:
            return [self._build_generic_event(event_factory, **generic_event_kwargs)]

        ball_carrier_id = ball_carrier.get('id')

        # TODO: Calculate duration properly
        timestamp = timedelta(seconds=self.raw_possession_event['startTime'])
        duration = timedelta(seconds=0)

        carry_outcome = (
            CARRY.OUTCOME(carry_dict['ballCarryOutcome'])
            if carry_dict['ballCarryOutcome']
            else None
        )
        touch_outcome = (
            CARRY.TOUCH_OUTCOME(carry_dict['touchOutcomeType'])
            if carry_dict['touchOutcomeType']
            else None
        )
        ball_carry_type = (
            CARRY.BALL_CARRY_TYPE(carry_dict['ballCarryType'])
            if carry_dict['ballCarryType']
            else None
        )
        carry_type = (
            CARRY.CARRY_TYPE(carry_dict['carryType'])
            if carry_dict['carryType']
            else None
        )

        carry_mapping = {
            CARRY.OUTCOME.LEADS_INTO_CHALLENGE: CarryResult.COMPLETE,
            CARRY.OUTCOME.RETAIN: CarryResult.COMPLETE,
            CARRY.OUTCOME.STOPPAGE: CarryResult.COMPLETE,
            CARRY.OUTCOME.BALL_LOSS: CarryResult.INCOMPLETE,
        }

        team = get_team_by_player_id(ball_carrier_id, self.teams)
        ball_carrier = team.get_player_by_id(ball_carrier_id)

        generic_event_kwargs['team'] = team
        generic_event_kwargs['player'] = ball_carrier

        if (
            carry_type == CARRY.BALL_CARRY_TYPE.TOUCH
            and carry_outcome == CARRY.OUTCOME.BALL_LOSS
        ):
            miscontrol_event = event_factory.build_miscontrol(
                result=None,
                end_timestamp=timestamp + duration,
                end_coordinates=None,
                **generic_event_kwargs,
            )
            return [miscontrol_event]

        elif carry_type == CARRY.BALL_CARRY_TYPE.CARRY and carry_outcome:
            carry_event = event_factory.build_carry(
                qualifiers=None,
                end_timestamp=timestamp + duration,
                result=carry_mapping.get(carry_outcome),
                end_coordinates=None,
                **generic_event_kwargs,
            )
            return [carry_event]

        if touch_outcome == CARRY.TOUCH_OUTCOME.OWN_GOAL:
            shot_event = event_factory.build_shot(
                result=ShotResult.OWN_GOAL,
                qualifiers=None,
                result_coordinates=None,
                **generic_event_kwargs,
            )
            return [shot_event]

        elif touch_outcome == CARRY.TOUCH_OUTCOME.GOAL:
            shot_event = event_factory.build_shot(
                result=ShotResult.GOAL,
                qualifiers=None,
                result_coordinates=None,
                **generic_event_kwargs,
            )
            return [shot_event]

        elif touch_outcome == CARRY.TOUCH_OUTCOME.INADVERTENT_SHOT_AT_GOAL:
            shot_outcome_id = carry_dict.get('shotOutcomeType')
            shot_result = _pff_shot_outcome_to_kloppy_shot_result(shot_outcome_id)
            shot_event = event_factory.build_shot(
                result=shot_result,
                qualifiers=None,
                result_coordinates=None,
                **generic_event_kwargs,
            )
            return [shot_event]

        return [self._build_generic_event(event_factory, **generic_event_kwargs)]


class CHALLENGE(POSSESSION_EVENT):
    """PFF Possession event CH/Challenge event."""

    class TYPE(Enum, metaclass=TypesEnumMeta):
        AERIAL_DUEL = 'A'
        FROM_BEHIND = 'B'
        DRIBBLE = 'D'
        FIFTY = 'FIFTY'
        GK_SMOTHERS = 'G'
        SHIELDING = 'H'  # GK specific event
        HAND_TACKLE = 'K'
        SLIDE_TACKLE = 'L'
        SHOULDER_TO_SHOULDER = 'S'
        STANDING_TACKLE = 'T'

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        # Some challenges are broken into multiple events
        challenge_events = []

        challenge_dict = self.raw_possession_event.get('challengeEvent', {})

        type_id = CHALLENGE.TYPE(challenge_dict['challengeType'])
        outcome_id = challenge_dict['challengeOutcomeType']

        # Some events are none... skip them if there's no type_id or outcome
        if type_id is None or outcome_id is None:
            return [self._build_generic_event(event_factory, **generic_event_kwargs)]

        # update the id to be the challenge id instead of the event_id
        generic_event_kwargs['event_id'] = f"otb-challenge-{self.raw_event['id']}"

        # extract basic qualifiers
        duel_qualifiers = []

        if type_id == CHALLENGE.TYPE.AERIAL_DUEL:
            duel_qualifiers = [
                DuelQualifier(value=DuelType.LOOSE_BALL),
                DuelQualifier(value=DuelType.AERIAL),
            ]
        elif type_id in [
            CHALLENGE.TYPE.FROM_BEHIND,
            CHALLENGE.TYPE.STANDING_TACKLE,
            CHALLENGE.TYPE.SHOULDER_TO_SHOULDER,
            CHALLENGE.TYPE.SHIELDING,
            CHALLENGE.TYPE.HAND_TACKLE,
        ]:
            duel_qualifiers = [
                DuelQualifier(value=DuelType.GROUND),
            ]
        elif type_id == CHALLENGE.TYPE.SLIDE_TACKLE:
            duel_qualifiers = [
                DuelQualifier(value=DuelType.GROUND),
                DuelQualifier(value=DuelType.SLIDING_TACKLE),
            ]
        elif type_id == CHALLENGE.TYPE.FIFTY:
            duel_qualifiers = [
                DuelQualifier(value=DuelType.LOOSE_BALL),
                DuelQualifier(value=DuelType.GROUND),
            ]

        # duels
        winner = challenge_dict['challengeWinnerPlayer']
        challengers = []

        # gk events
        if type_id == CHALLENGE.TYPE.GK_SMOTHERS:
            gk_id = challenge_dict['keeperPlayer']['id']
            gk_team = get_team_by_player_id(gk_id, self.teams)
            generic_event_kwargs['team'] = gk_team
            generic_event_kwargs['player'] = gk_team.get_player_by_id(gk_id)

            challenge_events.append(
                event_factory.build_goalkeeper_event(
                    result=None,
                    qualifiers=[GoalkeeperActionType.SMOTHER],
                    **generic_event_kwargs,
                )
            )

            challengers = [challenge_dict['ballCarrierPlayer']]

        elif type_id == CHALLENGE.TYPE.DRIBBLE:
            # if no winner, this cannot be calculated, right? check events again
            ball_carrier = challenge_dict['ballCarrierPlayer']
            is_winner = winner['id'] == ball_carrier['id'] if winner else None

            if challenge_dict['challengeOutcomeType'] == 'O':  # out of play
                result = TakeOnResult.OUT
            else:
                result = TakeOnResult.COMPLETE if is_winner else TakeOnResult.INCOMPLETE

            challenge_events.append(
                event_factory.build_take_on(
                    result=result,
                    qualifiers=[DuelQualifier(value=DuelType.GROUND)],
                    **generic_event_kwargs,
                )
            )

            challengers = [challenge_dict['challengerPlayer']]

        elif type_id in [
            CHALLENGE.TYPE.FROM_BEHIND,
            CHALLENGE.TYPE.STANDING_TACKLE,
            CHALLENGE.TYPE.SLIDE_TACKLE,
            CHALLENGE.TYPE.SHOULDER_TO_SHOULDER,
            CHALLENGE.TYPE.SHIELDING,
        ]:
            challengers = [
                challenge_dict['challengerPlayer'],
                challenge_dict['ballCarrierPlayer'],
            ]

        elif type_id in [CHALLENGE.TYPE.AERIAL_DUEL, CHALLENGE.TYPE.FIFTY]:
            challengers = [
                challenge_dict['challengerHomePlayer'],
                challenge_dict['challengerAwayPlayer'],
            ]

        elif type_id in [CHALLENGE.TYPE.HAND_TACKLE]:
            challengers = [
                challenge_dict['keeperPlayer'],
                challenge_dict['ballCarrierPlayer'],
            ]

        # don't log incomplete events
        if not any(challengers):
            logger.debug(
                f"Not enough challengers in event {generic_event_kwargs['event_id']}."
            )
            return [self._build_generic_event(event_factory, **generic_event_kwargs)]

        for player in challengers:
            team = get_team_by_player_id(player['id'], self.teams)

            kwargs = {**generic_event_kwargs}
            kwargs['event_id'] = f"otb-challenge-{self.raw_event['id']}"
            kwargs['team'] = team
            kwargs['player'] = team.get_player_by_id(player['id'])

            if not winner:
                result = DuelResult.NEUTRAL
            else:
                is_winner = winner['id'] == player['id']
                result = DuelResult.WON if is_winner else DuelResult.LOST

            duel_event = event_factory.build_duel(
                result=result, qualifiers=duel_qualifiers, **kwargs
            )

            challenge_events.append(duel_event)

        return challenge_events


class GOALKEEPER(EVENT):
    """StatsBomb 23/Goalkeeper event."""

    class TYPE(Enum, metaclass=TypesEnumMeta):
        COLLECTED = 25
        GOAL_CONCEDED = 26
        KEEPER_SWEEPER = 27
        PENALTY_CONCEDED = 28
        PENALTY_SAVED = 29
        PUNCH = 30
        PENALTY_SAVED_TO_POST = 109
        SAVE = 31
        SAVED_TO_POST = 110  # A save by the goalkeeper that hits the post
        SHOT_FACED = 32
        SHOT_SAVED = 33
        SHOT_SAVED_OFF_TARGET = 113
        SHOT_SAVED_TO_POST = 114  # A shot saved by the goalkeeper that hits the post
        SMOTHER = 34

    class KEEPER_SWEEPER:
        class OUTCOME(Enum, metaclass=TypesEnumMeta):
            CLAIM = 47
            CLEAR = 48
            WON = 4
            SUCCESS = 15

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        goalkeeper_dict = self.raw_event['goalkeeper']
        generic_event_kwargs = self._parse_generic_kwargs()

        # parse body part
        body_part_qualifiers = _get_body_part_qualifiers(goalkeeper_dict)
        hands_used = any(
            q.value
            in [
                BodyPart.LEFT_HAND,
                BodyPart.RIGHT_HAND,
                BodyPart.BOTH_HANDS,
            ]
            for q in body_part_qualifiers
        )
        head_or_foot_used = any(
            q.value
            in [
                BodyPart.LEFT_FOOT,
                BodyPart.RIGHT_FOOT,
                BodyPart.HEAD,
            ]
            for q in body_part_qualifiers
        )
        bodypart_missing = len(body_part_qualifiers) == 0

        # parse action type qualifiers
        save_event_types = [
            GOALKEEPER.TYPE.SHOT_SAVED,
            GOALKEEPER.TYPE.PENALTY_SAVED_TO_POST,
            GOALKEEPER.TYPE.SAVED_TO_POST,
            GOALKEEPER.TYPE.SHOT_SAVED_OFF_TARGET,
            GOALKEEPER.TYPE.SHOT_SAVED_TO_POST,
        ]
        type_id = GOALKEEPER.TYPE(goalkeeper_dict.get('type', {}).get('id'))
        outcome_id = goalkeeper_dict.get('outcome', {}).get('id')
        qualifiers = []
        if type_id in save_event_types:
            qualifiers.append(GoalkeeperQualifier(value=GoalkeeperActionType.SAVE))
        elif type_id == GOALKEEPER.TYPE.SMOTHER:
            qualifiers.append(GoalkeeperQualifier(value=GoalkeeperActionType.SMOTHER))
        elif type_id == GOALKEEPER.TYPE.PUNCH:
            qualifiers.append(GoalkeeperQualifier(value=GoalkeeperActionType.PUNCH))
        elif type_id == GOALKEEPER.TYPE.COLLECTED:
            qualifiers.append(GoalkeeperQualifier(value=GoalkeeperActionType.CLAIM))
        elif type_id == GOALKEEPER.TYPE.KEEPER_SWEEPER:
            outcome_id = GOALKEEPER.KEEPER_SWEEPER.OUTCOME(
                goalkeeper_dict.get('outcome', {}).get('id')
            )
            if outcome_id == GOALKEEPER.KEEPER_SWEEPER.OUTCOME.CLAIM:
                # a goalkeeper can only pick up the ball with his hands
                if hands_used or bodypart_missing:
                    qualifiers.append(
                        GoalkeeperQualifier(value=GoalkeeperActionType.PICK_UP)
                    )
                # otherwise it's a recovery
                else:
                    recovery = event_factory.build_recovery(
                        result=None,
                        qualifiers=body_part_qualifiers,
                        **generic_event_kwargs,
                    )
                    return [recovery]
            elif outcome_id in [
                GOALKEEPER.KEEPER_SWEEPER.OUTCOME.CLEAR,
                GOALKEEPER.KEEPER_SWEEPER.OUTCOME.SUCCESS,
            ]:
                # if the goalkeeper uses his foot or head, it's a clearance
                if head_or_foot_used:
                    clearance = event_factory.build_clearance(
                        result=None,
                        qualifiers=body_part_qualifiers,
                        **generic_event_kwargs,
                    )
                    return [clearance]
                # otherwise, it's a save
                else:
                    qualifiers.append(
                        GoalkeeperQualifier(value=GoalkeeperActionType.SAVE)
                    )

        if qualifiers:
            goalkeeper_event = event_factory.build_goalkeeper_event(
                result=None,
                qualifiers=qualifiers + body_part_qualifiers,
                **generic_event_kwargs,
            )
            return [goalkeeper_event]

        generic_event = event_factory.build_generic(
            result=None,
            qualifiers=None,
            event_name=self.raw_event['type']['name'],
            **generic_event_kwargs,
        )
        return [generic_event]

    def _create_ball_out_event(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        goalkeeper_dict = self.raw_event['goalkeeper']
        if (
            self.raw_event.get('out', False)
            or 'outcome' in goalkeeper_dict
            and 'Out' in goalkeeper_dict['outcome']['name']
        ):
            generic_event_kwargs['event_id'] = f"out-{generic_event_kwargs['event_id']}"
            generic_event_kwargs['ball_state'] = BallState.DEAD
            ball_out_event = event_factory.build_ball_out(
                result=None,
                qualifiers=None,
                **generic_event_kwargs,
            )
            return [ball_out_event]
        for related_event in self.related_events:
            if isinstance(related_event, SHOT):
                shot_dict = related_event.raw_event.get('shot', {})
                if (
                    related_event.raw_event.get('out', False)
                    or 'outcome' in shot_dict
                    and SHOT.OUTCOME(shot_dict['outcome']) == SHOT.OUTCOME.OFF_TARGET
                ):
                    generic_event_kwargs['event_id'] = (
                        f"out-{generic_event_kwargs['event_id']}"
                    )
                    generic_event_kwargs['ball_state'] = BallState.DEAD
                    generic_event_kwargs['coordinates'] = parse_coordinates(
                        shot_dict['end_location'],
                        self.fidelity_version,
                    )
                    generic_event_kwargs['raw_event'] = related_event.raw_event

                    ball_out_event = event_factory.build_ball_out(
                        result=None,
                        qualifiers=None,
                        **generic_event_kwargs,
                    )
                    return [ball_out_event]
                return []
        return []


class SUBSTITUTION(EVENT):
    """PFF SUB/Substitution event."""

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        team = generic_event_kwargs['team']

        replaced_player = team.get_player_by_id(self.raw_event['playerOff']['id'])
        if replaced_player is None:
            raise DeserializationError(
                f'Could not find player {self.raw_event["playerOff"]["id"]}'
            )

        replacement_player_id = self.raw_event['playerOn']['id']
        replacement_player = next(
            (
                player
                for player in team.players
                if player.player_id == str(replacement_player_id)
            ),
            None,
        )

        if replacement_player is None:
            raise DeserializationError(
                f'Could not find replacement player {replacement_player_id}'
            )

        generic_event_kwargs['player'] = replaced_player
        generic_event_kwargs['ball_state'] = BallState.DEAD

        substitution_event = event_factory.build_substitution(
            result=None,
            qualifiers=None,
            replacement_player=replacement_player,
            **generic_event_kwargs,
        )
        return [substitution_event]


class FOUL(POSSESSION_EVENT):
    """PFF Foul possession event."""

    class OUTCOME(Enum, metaclass=TypesEnumMeta):
        FIRST_YELLOW = 'Y'
        SECOND_YELLOW = 'S'
        RED = 'R'
        WARNING = 'W'
        NO_FOUL = 'F'
        NO_WARNING = 'N'

    class TYPE(Enum, metaclass=TypesEnumMeta):
        ADVANTAGE = 'A'
        INFRINGEMENT = 'I'
        MISSED_INFRINGEMENT = 'M'

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        events = []

        card_mapping = {
            FOUL.OUTCOME.FIRST_YELLOW: CardType.FIRST_YELLOW,
            FOUL.OUTCOME.SECOND_YELLOW: CardType.SECOND_YELLOW,
            FOUL.OUTCOME.RED: CardType.RED,
        }

        for foul in self.raw_possession_event.get('fouls', []):
            # skip non-fouls
            if FOUL.TYPE(foul['foulType']) != FOUL.TYPE.INFRINGEMENT:
                continue

            generic_event_kwargs['event_id'] = f"otb-foul-{self.raw_event['id']}"
            generic_event_kwargs['ball_state'] = BallState.DEAD

            foul_committer_id = (
                foul['culpritPlayer']['id'] if foul['culpritPlayer'] else None
            )

            generic_event_kwargs['team'] = None
            generic_event_kwargs['player'] = None

            if foul_committer_id:
                team = get_team_by_player_id(foul_committer_id, self.teams)
                player = team.get_player_by_id(foul_committer_id)
                generic_event_kwargs['team'] = team
                generic_event_kwargs['player'] = player

            card_type = FOUL.OUTCOME(foul['foulOutcomeType'])
            card_type = card_mapping.get(card_type)

            card_qualifier = [CardQualifier(value=card_type)] if card_type else None

            foul_committed_event = event_factory.build_foul_committed(
                result=None,
                qualifiers=card_qualifier,
                **generic_event_kwargs,
            )

            events.append(foul_committed_event)

            if card_type:
                card_event = event_factory.build_card(
                    result=None,
                    qualifiers=None,
                    card_type=card_type,
                    **generic_event_kwargs,
                )
                events.append(card_event)

        return events


class BALL_OUT(EVENT):
    """PFF OUT/Ball out of play event."""

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        generic_event_kwargs['ball_state'] = BallState.DEAD
        ball_out_event = event_factory.build_ball_out(
            result=None,
            qualifiers=None,
            **generic_event_kwargs,
        )
        return [ball_out_event]


class PLAYER_ON(EVENT):
    """PFF ON/Player off event."""

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        player_on_event = event_factory.build_player_on(
            result=None,
            qualifiers=None,
            **generic_event_kwargs,
        )
        return [player_on_event]


class PLAYER_OFF(EVENT):
    """PFF OFF/Player off event."""

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        player_off_event = event_factory.build_player_off(
            result=None,
            qualifiers=None,
            **generic_event_kwargs,
        )
        return [player_off_event]


class BALL_RECOVERY(EVENT):
    """StatsBomb 2/Ball recovery event."""

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        recovery_dict = self.raw_event.get('ball_recovery', {})
        recovery_failure = recovery_dict.get('recovery_failure', False)
        if recovery_failure:
            duel_event = event_factory.build_duel(
                result=DuelResult.LOST,
                qualifiers=[
                    DuelQualifier(value=DuelType.LOOSE_BALL),
                ],
                **generic_event_kwargs,
            )
            return [duel_event]

        recovery_event = event_factory.build_recovery(
            result=None,
            qualifiers=None,
            **generic_event_kwargs,
        )
        return [recovery_event]


class PRESSURE(EVENT):
    """PFF Pressure qualifies."""

    def _create_events(
        self, event_factory: EventFactory, **generic_event_kwargs
    ) -> list[Event]:
        end_timestamp = generic_event_kwargs['timestamp'] + timedelta(
            seconds=self.raw_event.get('duration', 0.0)
        )

        pressure_event = event_factory.build_pressure_event(
            result=None,
            qualifiers=None,
            end_timestamp=end_timestamp,
            **generic_event_kwargs,
        )
        return [pressure_event]


def _get_card_type(event_type: EVENT_TYPE, event_dict: dict) -> CardType | None:
    sb_to_kloppy_card_mappings = {
        FOUL_COMMITTED.CARD.FIRST_YELLOW: CardType.FIRST_YELLOW,
        FOUL_COMMITTED.CARD.SECOND_YELLOW: CardType.SECOND_YELLOW,
        FOUL_COMMITTED.CARD.RED: CardType.RED,
        BAD_BEHAVIOUR.CARD.FIRST_YELLOW: CardType.FIRST_YELLOW,
        BAD_BEHAVIOUR.CARD.SECOND_YELLOW: CardType.SECOND_YELLOW,
        BAD_BEHAVIOUR.CARD.RED: CardType.RED,
    }
    if 'card' in event_dict:
        if event_type == EVENT_TYPE.FOUL_COMMITTED:
            card_id = FOUL_COMMITTED.CARD(event_dict['card'])
        elif event_type == EVENT_TYPE.BAD_BEHAVIOUR:
            card_id = BAD_BEHAVIOUR.CARD(event_dict['card'])
        return sb_to_kloppy_card_mappings[card_id]
    return None


def _pff_shot_outcome_to_kloppy_shot_result(shot_outcome_type: str) -> ShotResult:
    outcome_mapping = {
        SHOT.OUTCOME.ON_TARGET_BLOCKED: ShotResult.BLOCKED,
        SHOT.OUTCOME.OFF_TARGET_BLOCKED: ShotResult.BLOCKED,
        SHOT.OUTCOME.SAVED_OFF_TARGET: ShotResult.SAVED,
        SHOT.OUTCOME.GOAL: ShotResult.GOAL,
        SHOT.OUTCOME.GOAL_LINE_CLEARANCE: ShotResult.BLOCKED,
        SHOT.OUTCOME.ON_TARGET: ShotResult.SAVED,
        SHOT.OUTCOME.OFF_TARGET: ShotResult.OFF_TARGET,
    }

    outcome = SHOT.OUTCOME(shot_outcome_type)
    result = outcome_mapping.get(outcome)

    if result is None:
        raise DeserializationError(f'Unknown shot outcome: {shot_outcome_type}')

    return result


def _get_line_player_body_part_qualifier(pff_body_part: str) -> list[BodyPartQualifier]:
    pff_to_kloppy_body_part_mapping = {
        BODYPART.HEAD: BodyPart.HEAD,
        BODYPART.LEFT_FOOT: BodyPart.LEFT_FOOT,
        BODYPART.LEFT_BACK_HEEL: BodyPart.LEFT_FOOT,
        BODYPART.LEFT_SHIN: BodyPart.LEFT_FOOT,
        BODYPART.LEFT_THIGH: BodyPart.LEFT_FOOT,
        BODYPART.LEFT_KNEE: BodyPart.LEFT_FOOT,
        BODYPART.RIGHT_FOOT: BodyPart.RIGHT_FOOT,
        BODYPART.RIGHT_BACK_HEEL: BodyPart.RIGHT_FOOT,
        BODYPART.RIGHT_SHIN: BodyPart.RIGHT_FOOT,
        BODYPART.RIGHT_THIGH: BodyPart.RIGHT_FOOT,
        BODYPART.RIGHT_KNEE: BodyPart.RIGHT_FOOT,
        # Other
        BODYPART.BOTTOM: BodyPart.OTHER,
        BODYPART.BACK: BodyPart.OTHER,
        BODYPART.CHEST: BodyPart.OTHER,
        BODYPART.LEFT_ARM: BodyPart.OTHER,
        BODYPART.LEFT_HAND: BodyPart.OTHER,
        BODYPART.LEFT_SHOULDER: BodyPart.OTHER,
        BODYPART.RIGHT_ARM: BodyPart.OTHER,
        BODYPART.RIGHT_HAND: BodyPart.OTHER,
        BODYPART.RIGHT_SHOULDER: BodyPart.OTHER,
        BODYPART.TWO_HAND_PALM: BodyPart.OTHER,
        BODYPART.TWO_HAND_CATCH: BodyPart.OTHER,
        BODYPART.TWO_HAND_PUNCH: BodyPart.OTHER,
        BODYPART.TWO_HANDS: BodyPart.OTHER,
        # Non-one-to-one-mapped body parts from PFF to Kloppy:
        # BodyPart.KEEPER_ARM, BodyPart.NO_TOUCH, BodyPart.DROP_KICK
        # These are determined by _get_gk_bodypart and when looking
        # PFF's MissedTouchType = 'D' for dummy
    }

    body_part_id = BODYPART(pff_body_part)
    if body_part_id in pff_to_kloppy_body_part_mapping:
        body_part = pff_to_kloppy_body_part_mapping[body_part_id]
        return [BodyPartQualifier(value=body_part)]

    return []


def _get_body_part_qualifiers(pff_body_part: str) -> list[BodyPartQualifier]: ...


def _get_gk_body_part_qualifiers(pff_body_part: str) -> list[BodyPartQualifier]:
    pff_to_kloppy_body_part_mapping = {
        BODYPART.HEAD: BodyPart.HEAD,
        BODYPART.LEFT_FOOT: BodyPart.LEFT_FOOT,
        BODYPART.LEFT_BACK_HEEL: BodyPart.LEFT_FOOT,
        BODYPART.LEFT_SHIN: BodyPart.LEFT_FOOT,
        BODYPART.LEFT_THIGH: BodyPart.LEFT_FOOT,
        BODYPART.LEFT_KNEE: BodyPart.LEFT_FOOT,
        BODYPART.RIGHT_FOOT: BodyPart.RIGHT_FOOT,
        BODYPART.RIGHT_BACK_HEEL: BodyPart.RIGHT_FOOT,
        BODYPART.RIGHT_SHIN: BodyPart.RIGHT_FOOT,
        BODYPART.RIGHT_THIGH: BodyPart.RIGHT_FOOT,
        BODYPART.RIGHT_KNEE: BodyPart.RIGHT_FOOT,
        # Other
        BODYPART.BACK: BodyPart.OTHER,
        BODYPART.BOTTOM: BodyPart.OTHER,
        # Goalkeeper specific
        BODYPART.CHEST: BodyPart.CHEST,
        BODYPART.LEFT_ARM: BodyPart.LEFT_HAND,
        BODYPART.LEFT_HAND: BodyPart.LEFT_HAND,
        BODYPART.LEFT_SHOULDER: BodyPart.LEFT_HAND,
        BODYPART.RIGHT_ARM: BodyPart.RIGHT_HAND,
        BODYPART.RIGHT_HAND: BodyPart.RIGHT_HAND,
        BODYPART.RIGHT_SHOULDER: BodyPart.RIGHT_HAND,
        BODYPART.TWO_HAND_PALM: BodyPart.BOTH_HANDS,
        BODYPART.TWO_HAND_CATCH: BodyPart.BOTH_HANDS,
        BODYPART.TWO_HAND_PUNCH: BodyPart.BOTH_HANDS,
        BODYPART.TWO_HANDS: BodyPart.BOTH_HANDS,
        # Non-one-to-one-mapped body parts from PFF to Kloppy:
        # BodyPart.KEEPER_ARM, BodyPart.NO_TOUCH, BodyPart.DROP_KICK
        # These are determined by _get_gk_bodypart and when looking
        # PFF's MissedTouchType = 'D' for dummy
    }

    body_part_id = BODYPART(pff_body_part)
    if body_part_id in pff_to_kloppy_body_part_mapping:
        body_part = pff_to_kloppy_body_part_mapping[body_part_id]
        return [BodyPartQualifier(value=body_part)]

    return []


def _get_pass_qualifiers(pass_dict: dict) -> list[PassQualifier]:
    qualifiers = []

    add_qualifier = lambda value: qualifiers.append(PassQualifier(value=value))

    if 'cross' in pass_dict:
        add_qualifier(PassType.CROSS)
    if 'technique' in pass_dict:
        technique_id = PASS.TECHNIQUE(pass_dict['technique'])
        if technique_id == PASS.TECHNIQUE.THROUGH_BALL:
            add_qualifier(PassType.THROUGH_BALL)
    if 'switch' in pass_dict:
        add_qualifier(PassType.SWITCH_OF_PLAY)
    if 'height' in pass_dict:
        height_id = PASS.HEIGHT(pass_dict['height'])
        if height_id == PASS.HEIGHT.HIGH:
            add_qualifier(PassType.HIGH_PASS)
    if 'length' in pass_dict:
        pass_length = pass_dict['length']
        if pass_length > 35:  # adopt Opta definition: 32 meters -> 35 yards
            add_qualifier(PassType.LONG_BALL)
    if 'body_part' in pass_dict:
        body_part_id = BODYPART(pass_dict['body_part'])
        if body_part_id == BODYPART.HEAD:
            add_qualifier(PassType.HEAD_PASS)
        elif body_part_id == BODYPART.KEEPER_ARM:
            add_qualifier(PassType.HAND_PASS)
    if 'shot_assist' in pass_dict:
        add_qualifier(PassType.SHOT_ASSIST)
    if 'goal_assist' in pass_dict:
        add_qualifier(PassType.ASSIST)
        add_qualifier(PassType.SHOT_ASSIST)
    return qualifiers


def _get_set_piece_qualifiers(event_dict: dict) -> list[SetPieceQualifier]:
    pff_to_kloppy_set_piece_mapping = {
        SETPIECE.CORNER: SetPieceType.CORNER_KICK,
        SETPIECE.DROP_BALL: SetPieceType.FREE_KICK,
        SETPIECE.FREE_KICK: SetPieceType.FREE_KICK,
        SETPIECE.KICK_OFF: SetPieceType.KICK_OFF,
        SETPIECE.PENALTY: SetPieceType.PENALTY,
        SETPIECE.THROW_IN: SetPieceType.THROW_IN,
    }

    if pff_set_piece_type := event_dict.get('setpieceType'):
        set_piece_type = pff_to_kloppy_set_piece_mapping[pff_set_piece_type]
        if set_piece_type is not None:
            return [SetPieceQualifier(value=set_piece_type)]

    return []


def event_decoder(raw_event: dict) -> list[EVENT | dict]:
    type_to_event = {
        # EVENT_TYPE.POSSESSION: POSSESSION_EVENT,  # MELHOR COM OTB HANDLER E CADE PEVT DENTRO DO POSS_EVENT
        EVENT_TYPE.BALL_OUT_OF_PLAY: BALL_OUT,
        EVENT_TYPE.PLAYER_ON: PLAYER_ON,
        EVENT_TYPE.PLAYER_OFF: PLAYER_OFF,
        EVENT_TYPE.SUB: SUBSTITUTION,
        POSSESSION_EVENT_TYPE.CHALLENGE: CHALLENGE,
        POSSESSION_EVENT_TYPE.BALL_CARRY: CARRY,
        POSSESSION_EVENT_TYPE.CLEARANCE: CLEARANCE,
        POSSESSION_EVENT_TYPE.SHOT: SHOT,
        # INCOMPLETE, WILL DEAL LATER
        POSSESSION_EVENT_TYPE.REBOUND: POSSESSION_EVENT,  # REBOUND,
        # TODO
        POSSESSION_EVENT_TYPE.PASS: POSSESSION_EVENT,  # TODO
        POSSESSION_EVENT_TYPE.CROSS: POSSESSION_EVENT,  # TODO
        EVENT_TYPE.FIRST_HALF_KICKOFF: EVENT,  # TODO
        EVENT_TYPE.SECOND_HALF_KICKOFF: EVENT,  # TODO
        EVENT_TYPE.EXTRA_1_KICKOFF: EVENT,  # TODO
        EVENT_TYPE.EXTRA_2_KICKOFF: EVENT,  # TODO
        EVENT_TYPE.END_OF_HALF: EVENT,  # TODO
        EVENT_TYPE.GROUND: EVENT,  # TODO
        EVENT_TYPE.PAUSE_OF_GAME_TIME: EVENT,  # TODO
        EVENT_TYPE.VIDEO: EVENT,  # TODO
    }

    events = []

    if possession_events := raw_event.get('possessionEvents'):
        possession_events = sorted(possession_events, key=lambda x: x['startTime'])
        for possession_event in possession_events:
            event_type = POSSESSION_EVENT_TYPE(possession_event['possessionEventType'])
            event_creator = type_to_event.get(event_type, POSSESSION_EVENT)
            events.append(event_creator(raw_event, possession_event))

            # fouls are embedded into possession events
            if foul := possession_event.get('fouls'):
                possession_event['foul'] = foul
                events.append(FOUL(raw_event, possession_event))

    else:
        event_type = EVENT_TYPE(raw_event['gameEventType'])
        event_creator = type_to_event.get(event_type, EVENT)
        events.append(event_creator(raw_event))

    return events
