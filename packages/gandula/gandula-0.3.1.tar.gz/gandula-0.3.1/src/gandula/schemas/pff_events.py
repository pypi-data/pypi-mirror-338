from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class PFFEventAdvantageType(str, Enum):
    NON_EVENT = 'N'


class PFFEventBallCarryType(str, Enum):
    CARRY = 'C'
    DRIBBLE = 'D'
    TOUCH = 'T'


class PFFEventBallCarryOutcomeType(str, Enum):
    LEADS_INTO_CHALLENGE = 'C'
    BALL_LOSS = 'L'
    RETAIN = 'R'
    STOPPAGE = 'S'


class PFFEventBetterOptionType(str, Enum):
    BALL_CARRY = 'B'
    CROSS = 'C'
    HOLD = 'H'
    CLEARANCE = 'L'
    CONTINUE = 'O'
    PASS = 'P'
    SHOT = 'S'


class PFFEventBodyMovementType(str, Enum):
    AWAY_FROM_GOAL = 'AG'
    LATERALLY = 'LA'
    STATIC = 'ST'
    TOWARDS_GOAL = 'TG'


class PFFEventBodyType(str, Enum):
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


class PFFEventCarryType(str, Enum):
    LINE_BREAK = 'B'
    CHANGE_OF_DIRECTION = 'C'
    DRIVE_WITH_INTENT = 'D'
    LONG_CARRY = 'L'


class PFFEventChallengeOutcomeType(str, Enum):
    DISTRIBUTION_DISRUPTED = 'B'
    FORCED_OUT_OF_PLAY = 'C'
    DISTRIBUTES_BALL = 'D'  # tem um passe/clearance/shot/cross na hora do challenge
    FOUL = 'F'
    SHIELDS_IN_PLAY = 'I'
    KEEPS_BALL_WITH_CONTACT = 'K'
    ROLLS = 'L'  # girar em volta do marcador (geralmente tem pressao)
    BEATS_MAN_LOSES_BALL = 'M'
    NO_WIN_KEEP_BALL = 'N'  # tentou driblar, nao conseguiu passar e manteve a posse
    OUT_OF_PLAY = 'O'
    PLAYER = 'P'  # a bola vai para um jogador que nao tava envolvido (ex: espirrou)
    RETAIN = 'R'
    SHIELDS_OUT_OF_PLAY = 'S'


class PFFEventChallengeType(str, Enum):
    AERIAL_DUEL = 'A'
    FROM_BEHIND = 'B'
    DRIBBLE = 'D'
    FIFTY = 'FIFTY'
    GK_SMOTHERS = 'G'
    SHIELDING = 'H'
    HAND_TACKLE = 'K'
    SLIDE_TACKLE = 'L'
    SHOULDER_TO_SHOULDER = 'S'
    STANDING_TACKLE = 'T'


class PFFEventClearanceOutcomeType(str, Enum):
    INADVERTENT_SHOT_AT_GOAL = 'A'
    BLOCK = 'B'
    INADVERTENT_SHOT_OWN_GOAL = 'D'
    DELIBERATE_TO_OPPOSITION = 'E'
    OWN_POST = 'N'
    OUT_OF_PLAY = 'O'
    PLAYER = 'P'
    STOPPAGE = 'S'
    DELIBERATE_TO_TOUCH = 'U'
    POST = 'W'


class PFFEventCrossOutcomeType(str, Enum):
    BLOCKED = 'B'
    COMPLETE = 'C'
    DEFENSIVE_INTERCEPTION = 'D'
    LUCKY_SHOT_AT_GOAL = 'I'
    OUT_OF_PLAY = 'O'
    STOPPAGE = 'S'
    UNTOUCHED = 'U'


# TOOD: CONFIRM IF == BELOW
# AWAY_FROM_DEFENDER = 'A'
# CHECKS_MOVEMENT = 'C'
# LEADS_INTO_CHALLENGE = 'E'
# HEAVY = 'H'
# IN_STRIDE = 'I'
# LIGHT = 'L'
# PRECISE = 'P'
# REDIRECTS = 'R'
# STANDARD = 'S'
class PFFEventCrossAccuracyType(str, Enum):
    UNKNOWN_PFF_TYPE_A = 'A'
    UNKNOWN_PFF_TYPE_C = 'C'
    UNKNOWN_PFF_TYPE_E = 'E'
    UNKNOWN_PFF_TYPE_H = 'H'
    UNKNOWN_PFF_TYPE_I = 'I'
    UNKNOWN_PFF_TYPE_L = 'L'
    UNKNOWN_PFF_TYPE_P = 'P'
    UNKNOWN_PFF_TYPE_R = 'R'
    UNKNOWN_PFF_TYPE_S = 'S'


class PFFEventCrossType(str, Enum):
    DRILLED = 'D'
    FLOATED = 'F'
    SWING_IN = 'I'
    SWING_OUT = 'O'
    PLACED = 'P'


class PFFEventCrossZoneType(str, Enum):
    CENTRAL = 'C'
    FAR_POST = 'F'
    NEAR_POST = 'N'
    SIX_YARD_BOX = 'S'


class PFFEventDribbleOutcomeType(str, Enum):
    KEEPS_BALL_WITH_CONTACT = 'B'
    FOUL = 'F'
    MISHIT = 'H'
    KEEPS_BALL = 'K'
    BEATS_MAN_LOSES_BALL = 'L'
    MISSED_FOUL = 'M'
    FORCED_OUT_OF_PLAY = 'O'
    SUCCESSFUL_TACKLE = 'S'


class PFFEventDribbleType(str, Enum):
    BETWEEN_TWO_DEFENDERS = 'B'
    INSIDE = 'I'
    KNOCKS_IN_FRONT = 'K'
    OUTSIDE = 'O'
    TRICK = 'T'


class PFFEventEndType(str, Enum):
    EXTRA_1 = 'F'
    FIRST = 'FIRST'
    GAME = 'G'
    EXTRA_2 = 'S'
    SECOND = 'SECOND'
    Z_TEST_9 = 'Z'


class PFFEventFacingType(str, Enum):
    BACK_TO_GOAL = 'B'
    GOAL = 'G'
    LATERAL = 'L'


class PFFEventFoulOutcomeType(str, Enum):
    NO_FOUL = 'F'
    NO_WARNING = 'N'
    RED_CARD = 'R'
    SECOND_YELLOW = 'S'
    WARNING = 'W'
    YELLOW_CARD = 'Y'


class PFFEventFoulType(str, Enum):
    ADVANTAGE = 'A'
    INFRINGEMENT = 'I'
    MISSED_INFRINGEMENT = 'M'


class PFFEventEventType(str, Enum):
    FIRST_HALF_KICKOFF = 'FIRSTKICKOFF'
    SECOND_HALF_KICKOFF = 'SECONDKICKOFF'
    EXTRA_1_KICKOFF = 'THIRDKICKOFF'
    EXTRA_2_KICKOFF = 'FOURTHKICKOFF'
    GAME_CLOCK_OBSERVATION = 'CLK'
    END_OF_HALF = 'END'
    GROUND = 'G'  # trave!!! travessao ou bandeira de escanteio. O evento eh vazio.
    PLAYER_OFF = 'OFF'
    PLAYER_ON = 'ON'
    POSSESSION = 'OTB'
    BALL_OUT_OF_PLAY = 'OUT'
    PAUSE_OF_GAME_TIME = 'PAU'
    SUB = 'SUB'
    VIDEO = 'VID'


class PFFEventHeightType(str, Enum):
    ABOVE_HEAD = 'A'
    GROUND = 'G'
    BETWEEN_WAIST_AND_HEAD = 'H'
    OFF_GROUND_BELOW_WAIST = 'L'
    VIDEO_MISSING = 'M'
    HALF_VOLLEY = 'V'  # Bola quica e ta subindo


class PFFEventIncompletionReasonType(str, Enum):
    BEHIND = 'BH'
    BLOCKED = 'BL'
    CAUGHT = 'CA'
    DEFENSIVE_CONTACT = 'CO'
    DELIBERATE = 'DB'
    DEFENSIVE_CHALLENGE = 'DC'
    DEFLECTED = 'DF'
    DEFENDER_INTERCEPTION = 'DI'
    FOUL = 'FO'
    HIGH = 'HI'
    HIT_OFFICIAL = 'HO'
    IN_FRONT = 'IF'
    RECEIVER_LETS_BALL_RUN = 'LB'
    MISCOMMUNICATION = 'MC'
    MISS_HIT = 'MH'
    PASSER_SLIPPED = 'PS'
    RECEIVER_DIDNT_RETURN_TO_BALL = 'RB'
    RECEIVER_SLIPPED = 'RF'
    RECEIVER_MISSES_BALL = 'RM'
    RECEIVER_STOPPED = 'RS'
    REFEREE_IN_WAY = 'RW'
    SPECULATIVE = 'SP'
    UNDERHIT = 'UH'
    VIDEO_MISSING = 'VM'


class PFFEventInitialTouchType(str, Enum):
    H2C_BAD = 'B'
    H2C_GOOD = 'G'
    MISCONTROL = 'M'
    PLUS = 'P'
    STANDARD = 'S'


class PFFEventLinesBrokenType(str, Enum):
    ATT = 'A'
    ATT_DEF = 'AD'
    ATT_MID = 'AM'
    ATT_MID_DEF = 'AMD'
    DEF = 'D'
    MID = 'M'
    MID_DEF = 'MD'


class PFFEventMissedTouchType(str, Enum):
    MISSED_CROSS = 'C'
    DUMMY = 'D'  # deixa a bola passar pra outro
    MISSED_INTERCEPTION = 'I'
    MISSED_CLEARANCE = 'L'
    MISSED_TOUCH = 'M'
    MISSED_SHOT = 'O'
    MISSED_PASS = 'P'
    SLIP = 'S'


class PFFEventOpportunityType(str, Enum):
    CHANCE_CREATED = 'C'
    DANGEROUS_POSITION = 'D'
    HALF_CHANCE = 'H'
    SPACE_TO_CLEAR = 'L'
    NEGATIVE_CHANCE_CREATED = 'N'
    NEGATIVE_DANGEROUS_POSITION = 'P'
    SPACE_TO_CROSS = 'R'
    SPACE_TO_SHOOT = 'S'


class PFFEventOriginateType(str, Enum):
    CORNER_FLAG = 'C'
    MISCELLANEOUS = 'M'
    PLAYER = 'P'
    POST = 'W'


class PFFEventOutType(str, Enum):
    AWAY_SCORE = 'A'
    HOME_SCORE = 'H'
    TOUCH = 'T'
    WHISTLE = 'W'


class PFFEventPassAccuracyType(str, Enum):
    AWAY_FROM_DEFENDER = 'A'
    CHECKS_MOVEMENT = 'C'
    LEADS_INTO_CHALLENGE = 'E'
    HEAVY = 'H'
    IN_STRIDE = 'I'
    LIGHT = 'L'
    PRECISE = 'P'
    REDIRECTS = 'R'
    STANDARD = 'S'


class PFFEventPassOutcomeType(str, Enum):
    BLOCKED = 'B'
    COMPLETE = 'C'
    DEFENSIVE_INTERCEPTION = 'D'
    LUCKY_SHOT_OWN_GOAL = 'G'
    LUCKY_SHOT_GOAL = 'I'
    OUT_OF_PLAY = 'O'
    STOPPAGE = 'S'


class PFFEventPassType(str, Enum):
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


class PFFEventPlayerOffType(str, Enum):
    EQUIPMENT = 'E'
    INJURY = 'I'
    MISCELLANEOUS = 'M'
    RED_CARD = 'R'
    # YELLOW_CARD = 'Y'


class PFFEventPositionGroupType(str, Enum):
    ATTACK_MID = 'AM'
    CENTER_FORWARD = 'CF'
    CENTER_MID = 'CM'
    DEFENDER = 'D'
    DEFENSIVE_MID = 'DM'
    FORWARD = 'F'
    GK = 'GK'
    LEFT_BACK = 'LB'
    LEFT_CENTER_BACK = 'LCB'
    LEFT_MID = 'LM'
    LEFT_WINGER = 'LW'
    LEFT_WING_BACK = 'LWB'
    MIDFIELDER = 'M'
    MID_CENTER_BACK = 'MCB'
    RIGHT_BACK = 'RB'
    RIGHT_CENTER_BACK = 'RCB'
    CENTER_BACK = 'CB'
    RIGHT_MID = 'RM'
    RIGHT_WINGER = 'RW'
    RIGHT_WING_BACK = 'RWB'


class PFFEventPossessionEventType(str, Enum):
    BALL_CARRY = 'BC'
    CHALLENGE = 'CH'
    CLEARANCE = 'CL'
    CROSS = 'CR'
    PASS = 'PA'
    REBOUND = 'RE'
    SHOT = 'SH'


class PFFEventPotentialOffenseType(str, Enum):
    DISSENT = 'D'
    OFF_THE_BALL = 'F'
    HAND_BALL = 'H'
    ON_THE_BALL = 'N'
    OFFSIDE = 'O'
    TECHNICAL = 'T'
    DIVA = 'V'


class PFFEventPressureType(str, Enum):
    ATTEMPTED = 'A'
    PASSING_LANE = 'L'
    PRESSURED = 'P'


# Rebound: a bola bateu no jogador
class PFFEventReboundOutcomeType(str, Enum):
    LUCKY_SHOT_GOAL = 'A'
    LUCKY_SHOT_OWN_GOAL = 'D'
    PLAYER = 'P'
    RETAIN = 'R'
    OUT_OF_TOUCH = 'T'


class PFFEventSaveReboundType(str, Enum):
    CROSSBAR = 'CB'
    LEFT_BEHIND_GOAL = 'GL'
    RIGHT_BEHIND_GOAL = 'GR'
    LEFT_BEHIND_GOAL_HIGH = 'HL'
    RIGHT_BEHIND_GOAL_HIGH = 'HR'
    LEFT_SIX_YARD_BOX = 'L6'
    LEFT_AREA = 'LA'
    LEFT_OUT_OF_BOX = 'LO'
    LEFT_POST = 'LP'
    MIDDLE_SIX_YARD_BOX = 'M6'
    MIDDLE_AREA = 'MA'
    MIDDLE_OUT_OF_BOX = 'MO'
    CROSSBAR_OVER = 'OC'
    RIGHT_SIX_YARD_BOX = 'R6'
    RIGHT_AREA = 'RA'
    RIGHT_OUT_OF_BOX = 'RO'
    RIGHT_POST = 'RP'


class PFFEventSetpieceType(str, Enum):
    CORNER = 'C'
    DROP_BALL = 'D'
    FREE_KICK = 'F'
    GOAL_KICK = 'G'
    KICKOFF = 'K'
    PENALTY = 'P'
    THROW_IN = 'T'


class PFFEventShotHeightType(str, Enum):
    BOTTOM_THIRD = 'BOTTOMTHIRD'
    CROSSBAR = 'C'
    SHORT = 'F'
    GROUND = 'G'
    MIDDLE_THIRD = 'MIDDLETHIRD'
    CROSSBAR_NARROW_OVER = 'N'
    OVER = 'O'
    TOP_THIRD = 'TOPTHIRD'
    CROSSBAR_NARROW_UNDER = 'U'
    UNKNOWN_TYPE_PFF_1 = '1'
    UNKNOWN_TYPE_PFF_2 = '2'
    UNKNOWN_TYPE_PFF_3 = '3'


class PFFEventShotNatureType(str, Enum):
    PLACEMENT = 'A'
    FLICK = 'F'
    LACES = 'L'
    POWER = 'P'
    SCUFF = 'S'
    TOE_PUNT = 'T'


class PFFEventShotOutcomeType(str, Enum):
    ON_TARGET_BLOCK = 'B'
    OFF_TARGET_BLOCK = 'C'
    SAVE_OFF_TARGET = 'F'
    GOAL = 'G'
    GOALLINE_CLEARANCE = 'L'
    OFF_TARGET = 'O'
    ON_TARGET = 'S'


class PFFEventShotType(str, Enum):
    BICYCLE = 'B'
    DIVING = 'D'
    SIDE_FOOT = 'F'
    SLIDING = 'I'
    LOB = 'L'
    OUTSIDE_FOOT = 'O'
    STANDARD = 'S'
    STUDS = 'T'
    VOLLEY = 'V'


class PFFEventStadiumGrassType(str, Enum):
    ASTRO_TURF = 'A'
    FIELD_TURF = 'F'
    REAL = 'R'
    NATURAL = 'N'


class PFFEventStadiumType(str, Enum):
    CONVERSION = 'C'
    DOMED = 'D'
    INDOOR = 'I'
    OUTDOOR = 'O'


class PFFEventSubType(str, Enum):
    BLOOD = 'B'
    SIN_BIN_COVER = 'C'
    HEAD_INJURY_ASSESSMENT = 'H'
    RETURN_FROM_HEAD_INJURY_ASSESSMENT = 'R'
    STANDARD = 'S'


class PFFEventTackleAttemptType(str, Enum):
    DELIBERATE_FOUL = 'D'
    NO_TACKLE_FAKE_EVENT = 'F'
    GO_FOR_BALL = 'G'
    NO_TACKLE = 'T'


class PFFEventTouchOutcomeType(str, Enum):
    INADVERTENT_SHOT_AT_GOAL = 'A'
    CHALLENGE = 'C'
    INADVERTENT_SHOT_OWN_GOAL = 'D'
    GOAL = 'G'
    OUT_OF_PLAY = 'O'
    PLAYER = 'P'
    RETAIN = 'R'
    OWN_GOAL = 'W'


class PFFEventTouchType(str, Enum):
    BALL_IN_HAND = 'B'
    FAILED_CROSS = 'C'
    HAND_BALL = 'D'
    FAILED_TRAP = 'F'
    FAILED_CATCH = 'G'
    HEAVY_TOUCH = 'H'
    FAILED_CLEARANCE = 'L'
    FAILED_PASS = 'P'
    FAILED_SHOT = 'S'
    TAKE_OVER = 'T'


class PFFEventVarReasonType(str, Enum):
    MISSED = 'I'
    OVERTURN = 'O'


class PFFEventVideoAngleType(str, Enum):
    BAD_ANGLE = 'B'
    MISSING = 'M'


class PFFEventId(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str


class PFFEventPlayerIdNickname(BaseModel):
    model_config = ConfigDict(extra='forbid')

    id: str
    # nickname: str
    # team: PFFEventId


class PFFEventBallCarryEvent(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str
    game: PFFEventId
    gameEvent: PFFEventId
    possessionEvent: PFFEventId

    badParry: bool
    ballCarrierPlayer: PFFEventPlayerIdNickname | None
    ballCarryOutcome: PFFEventBallCarryOutcomeType | None
    ballCarryType: PFFEventBallCarryType | None
    betterOptionPlayer: PFFEventPlayerIdNickname | None
    betterOptionTime: str | None
    betterOptionType: PFFEventBetterOptionType | None
    carryIntent: str | None
    carryType: PFFEventCarryType | None
    challengerPlayer: PFFEventPlayerIdNickname | None
    clearerPlayer: PFFEventPlayerIdNickname | None
    createsSpace: bool | None
    defenderPlayer: PFFEventPlayerIdNickname | None
    dribbleOutcomeType: PFFEventDribbleOutcomeType | None
    keeperPlayer: PFFEventPlayerIdNickname | None
    linesBrokenType: PFFEventLinesBrokenType | None
    missedTouchPlayer: PFFEventPlayerIdNickname | None
    missedTouchType: PFFEventMissedTouchType | None
    opportunityType: PFFEventOpportunityType | None
    period: int | None
    pressurePlayer: PFFEventPlayerIdNickname | None
    pressureType: PFFEventPressureType
    saveReboundType: PFFEventSaveReboundType | None
    saveable: bool
    shotInitialHeightType: PFFEventShotHeightType | None
    shotOutcomeType: PFFEventShotOutcomeType | None
    successful: bool | None
    tackleAttemptType: PFFEventTackleAttemptType | None
    touchOutcomeType: PFFEventTouchOutcomeType | None
    touchType: PFFEventTouchType | None


class PFFEventCacheStats(BaseModel):
    model_config = ConfigDict(extra='forbid')
    hitRate: float
    name: str


class PFFEventChallengeEvent(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str
    game: PFFEventId
    gameEvent: PFFEventId
    possessionEvent: PFFEventId

    additionalChallenger1: PFFEventPlayerIdNickname | None
    additionalChallenger2: PFFEventPlayerIdNickname | None
    additionalChallenger3: PFFEventPlayerIdNickname | None
    advantageType: PFFEventAdvantageType | None
    ballCarrierPlayer: PFFEventPlayerIdNickname | None
    challengeOutcomeType: PFFEventChallengeOutcomeType | None
    challengeType: PFFEventChallengeType | None
    challengeWinnerPlayer: PFFEventPlayerIdNickname | None
    challengerAwayPlayer: PFFEventPlayerIdNickname | None
    challengerHomePlayer: PFFEventPlayerIdNickname | None
    challengerPlayer: PFFEventPlayerIdNickname | None
    createsSpace: bool | None
    dribbleType: PFFEventDribbleType | None
    keeperPlayer: PFFEventPlayerIdNickname | None
    linesBrokenType: PFFEventLinesBrokenType | None
    missedTouchPlayer: PFFEventPlayerIdNickname | None
    missedTouchType: PFFEventMissedTouchType | None
    opportunityType: PFFEventOpportunityType | None
    period: str | None
    pressurePlayer: PFFEventPlayerIdNickname | None
    tackleAttemptType: PFFEventTackleAttemptType | None
    trickType: str | None


class PFFEventClearanceEvent(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str
    game: PFFEventId
    gameEvent: PFFEventId
    possessionEvent: PFFEventId

    advantageType: PFFEventAdvantageType | None
    badParry: bool
    ballHeightType: PFFEventHeightType | None
    betterOptionPlayer: PFFEventPlayerIdNickname | None
    betterOptionTime: str | None
    betterOptionType: PFFEventBetterOptionType | None
    blockerPlayer: PFFEventPlayerIdNickname | None
    clearanceBodyType: PFFEventBodyType | None
    clearanceOutcomeType: PFFEventClearanceOutcomeType
    clearancePlayer: PFFEventPlayerIdNickname
    createsSpace: bool | None
    createsSpaceVsPlayer: PFFEventPlayerIdNickname | None
    failedInterventionPlayer: PFFEventPlayerIdNickname | None
    failedInterventionPlayer1: PFFEventPlayerIdNickname | None
    failedInterventionPlayer2: PFFEventPlayerIdNickname | None
    failedInterventionPlayer3: PFFEventPlayerIdNickname | None
    heightType: PFFEventHeightType | None
    keeperPlayer: PFFEventPlayerIdNickname | None
    missedTouchPlayer: PFFEventPlayerIdNickname | None
    missedTouchType: PFFEventMissedTouchType | None
    opportunityType: PFFEventOpportunityType | None
    period: str | None
    pressurePlayer: PFFEventPlayerIdNickname | None
    pressureType: PFFEventPressureType | None
    saveReboundType: PFFEventSaveReboundType | None
    saveable: bool
    shotInitialHeightType: PFFEventShotHeightType | None
    shotOutcomeType: PFFEventShotOutcomeType | None


class PFFEventCompetition(BaseModel):
    model_config = ConfigDict(extra='forbid')
    availableSeasons: list[PFFEventCompetitionSeason] = Field(default_factory=list)
    id: str
    games: list[PFFEventGame] = Field(default_factory=list)
    name: str
    seasonGames: list[PFFEventGame] = Field(default_factory=list)
    teams: list[PFFEventTeam] = Field(default_factory=list)


class PFFEventCompetitionSeason(BaseModel):
    model_config = ConfigDict(extra='forbid')
    season: str
    start: str
    end: str


class PFFEventConfederation(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    abbreviation: str
    name: str


class PFFEventCrossEvent(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str
    game: PFFEventId
    gameEvent: PFFEventId
    possessionEvent: PFFEventId

    advantageType: PFFEventAdvantageType | None
    badParry: bool
    ballHeightType: PFFEventHeightType
    betterOptionPlayer: PFFEventPlayerIdNickname | None
    betterOptionTime: str | None
    betterOptionType: PFFEventBetterOptionType | None
    blockerPlayer: PFFEventPlayerIdNickname | None
    clearerPlayer: PFFEventPlayerIdNickname | None
    completeToPlayer: PFFEventPlayerIdNickname | None
    createsSpace: bool | None
    createsSpaceVsPlayer: PFFEventPlayerIdNickname | None
    crossAccuracyType: PFFEventCrossAccuracyType | None
    crossHighPointType: PFFEventHeightType | None
    crossOutcomeType: PFFEventCrossOutcomeType | None
    crossType: PFFEventCrossType | None
    crossZoneType: PFFEventCrossZoneType | None
    crosserBodyType: PFFEventBodyType
    crosserPlayer: PFFEventPlayerIdNickname
    defenderBallHeightType: PFFEventHeightType | None
    defenderBodyType: PFFEventBodyType | None
    defenderPlayer: PFFEventPlayerIdNickname | None
    deflectorBodyType: PFFEventBodyType | None
    deflectorPlayer: PFFEventPlayerIdNickname | None
    failedInterventionPlayer: PFFEventPlayerIdNickname | None
    failedInterventionPlayer1: PFFEventPlayerIdNickname | None
    failedInterventionPlayer2: PFFEventPlayerIdNickname | None
    failedInterventionPlayer3: PFFEventPlayerIdNickname | None
    incompletionReasonType: PFFEventIncompletionReasonType | None
    intendedTargetPlayer: PFFEventPlayerIdNickname | None
    keeperPlayer: PFFEventPlayerIdNickname | None
    late: bool | None
    missedTouchPlayer: PFFEventPlayerIdNickname | None
    missedTouchType: PFFEventMissedTouchType | None
    noLook: bool
    opportunityType: PFFEventOpportunityType | None
    period: str | None
    pressurePlayer: PFFEventPlayerIdNickname | None
    pressureType: PFFEventPressureType | None
    receiverBallHeightType: PFFEventHeightType | None
    receiverBodyType: PFFEventBodyType | None
    saveReboundType: PFFEventSaveReboundType | None
    saveable: bool
    secondIncompletionReasonType: PFFEventIncompletionReasonType | None
    shotInitialHeightType: PFFEventShotHeightType | None
    shotOutcomeType: PFFEventShotOutcomeType | None


class PFFEventDefender(BaseModel):
    model_config = ConfigDict(extra='forbid')

    id: str

    defenderPlayer: PFFEventPlayerIdNickname
    game: PFFEventId
    gameEvent: PFFEventId
    possessionEvent: PFFEventId


class PFFEventFederation(BaseModel):
    model_config = ConfigDict(extra='forbid')

    id: str
    name: str
    englishName: str
    abbreviation: str
    confederation: PFFEventConfederation
    country: str


class PFFEventFoul(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str
    game: PFFEventId
    gameEvent: PFFEventId
    possessionEvent: PFFEventId

    badCall: bool | None
    correctDecision: bool
    culpritPlayer: PFFEventPlayerIdNickname | None
    foulOutcomeType: PFFEventFoulOutcomeType | None
    foulType: PFFEventFoulType | None
    potentialOffenseType: PFFEventPotentialOffenseType | None
    sequence: int | None
    tacticalFoul: bool | None
    var: bool | None
    varCulpritPlayer: PFFEventPlayerIdNickname | None
    varOutcomeType: PFFEventFoulOutcomeType | None
    varPotentialOffenseType: PFFEventPotentialOffenseType | None
    varReasonType: PFFEventVarReasonType | None
    victimPlayer: PFFEventPlayerIdNickname | None


class PFFEventLocation(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str

    eventModule: str
    # ballCarryEvent: PFFEventBallCarryEvent
    # challengeEvent: PFFEventChallengeEvent
    # clearanceEvent: PFFEventClearanceEvent
    # crossEvent: PFFEventCrossEvent
    # gameEvent: PFFEventId # Deveri incluir...
    name: str
    # passingEvent: PFFEventPassingEvent
    # possessionEvent: PFFEventId # Deveria incruir....
    # reboundEvent: PFFEventReboundEvent
    # shootingEvent: PFFEventShootingEvent
    x: float
    y: float


class PFFEventNation(BaseModel):
    model_config = ConfigDict(extra='forbid')
    country: str
    federation: PFFEventFederation
    fifaCode: str
    id: str
    iocCode: str


class PFFEventPassingEvent(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str
    game: PFFEventId
    gameEvent: PFFEventId
    possessionEvent: PFFEventId

    advantageType: PFFEventAdvantageType | None
    badParry: bool
    ballHeightType: PFFEventHeightType | None
    betterOptionPlayer: PFFEventPlayerIdNickname | None
    betterOptionTime: str | None
    betterOptionType: PFFEventBetterOptionType | None
    blockerPlayer: PFFEventPlayerIdNickname | None
    clearerPlayer: PFFEventPlayerIdNickname | None
    createsSpace: bool | None
    createsSpaceVsPlayer: PFFEventPlayerIdNickname | None
    defenderBodyType: PFFEventBodyType | None
    defenderHeightType: PFFEventHeightType | None
    defenderPlayer: PFFEventPlayerIdNickname | None
    deflectorBodyType: PFFEventBodyType | None
    deflectorPlayer: PFFEventPlayerIdNickname | None
    failedInterventionPlayer: PFFEventPlayerIdNickname | None
    failedInterventionPlayer1: PFFEventPlayerIdNickname | None
    failedInterventionPlayer2: PFFEventPlayerIdNickname | None
    failedInterventionPlayer3: PFFEventPlayerIdNickname | None
    incompletionReasonType: PFFEventIncompletionReasonType | None
    keeperPlayer: PFFEventPlayerIdNickname | None
    late: bool | None
    linesBrokenType: PFFEventLinesBrokenType | None
    missedTouchPlayer: PFFEventPlayerIdNickname | None
    missedTouchType: PFFEventMissedTouchType | None
    noLook: bool | None
    opportunityType: PFFEventOpportunityType | None
    passAccuracyType: PFFEventPassAccuracyType | None
    passBodyType: PFFEventBodyType | None
    passHighPointType: PFFEventHeightType | None
    passOutcomeType: PFFEventPassOutcomeType | None
    passType: PFFEventPassType | None
    passerPlayer: PFFEventPlayerIdNickname | None
    period: str | None
    pressurePlayer: PFFEventPlayerIdNickname | None
    pressureType: PFFEventPressureType | None
    receiverBodyType: PFFEventBodyType | None
    receiverFacingType: PFFEventFacingType | None
    receiverHeightType: PFFEventHeightType | None
    receiverPlayer: PFFEventPlayerIdNickname | None
    saveReboundType: PFFEventSaveReboundType | None
    saveable: bool
    secondIncompletionReasonType: PFFEventIncompletionReasonType | None
    shotInitialHeightType: PFFEventShotHeightType | None
    shotOutcomeType: PFFEventShotOutcomeType | None
    targetFacingType: PFFEventFacingType
    targetPlayer: PFFEventPlayerIdNickname | None


class PFFEventPlayer(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    dob: str | None
    firstName: str
    lastName: str
    nickname: str
    height: float | None  # in cm
    weight: float | None
    gender: str | None
    nationality: PFFEventNation | None
    positionGroupType: PFFEventPositionGroupType
    preferredFoot: str | None
    secondNationality: PFFEventNation | None
    countryOfBirth: PFFEventNation | None


class PFFEventPossessionEvent(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str
    game: PFFEventId
    gameEvent: PFFEventId

    ballCarryEvent: PFFEventBallCarryEvent | None
    challengeEvent: PFFEventChallengeEvent | None
    clearanceEvent: PFFEventClearanceEvent | None
    crossEvent: PFFEventCrossEvent | None
    reboundEvent: PFFEventReboundEvent | None
    shootingEvent: PFFEventShootingEvent | None
    passingEvent: PFFEventPassingEvent | None

    defenders: list[PFFEventDefender] = Field(default_factory=list)
    endTime: float | None
    formattedGameClock: str | None
    fouls: list[PFFEventFoul] = Field(default_factory=list)
    gameClock: float | None
    lastInGameEvent: int
    period: str | None
    possessionEventType: PFFEventPossessionEventType
    startTime: float
    videoUrl: str


class PFFEventReboundEvent(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str
    game: PFFEventId
    gameEvent: PFFEventId
    possessionEvent: PFFEventId

    advantageType: PFFEventAdvantageType | None
    badParry: bool
    blockerPlayer: PFFEventPlayerIdNickname | None
    # clearerPlayer: PFFEventPlayerIdNickname | None
    keeperPlayer: PFFEventPlayerIdNickname | None
    missedTouchPlayer: PFFEventPlayerIdNickname | None
    missedTouchType: PFFEventMissedTouchType | None
    originateType: PFFEventOriginateType
    period: str | None
    reboundBodyType: PFFEventBodyType | None
    reboundHeightType: PFFEventHeightType | None
    reboundHighPointType: PFFEventHeightType | None
    reboundOutcomeType: PFFEventReboundOutcomeType | None
    rebounderPlayer: PFFEventPlayerIdNickname | None
    saveReboundType: PFFEventSaveReboundType | None
    saveable: bool
    shotInitialHeightType: PFFEventShotHeightType | None
    shotOutcomeType: PFFEventShotOutcomeType | None


class PFFEventRoster(BaseModel):
    model_config = ConfigDict(extra='forbid')

    id: str
    game: PFFEventId
    player: PFFEventPlayer
    positionGroupType: PFFEventPositionGroupType
    shirtNumber: int
    started: bool
    team: PFFEventTeam


class PFFEventShootingEvent(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str
    game: PFFEventId
    gameEvent: PFFEventId
    possessionEvent: PFFEventId

    advantageType: PFFEventAdvantageType | None
    badParry: bool
    ballHeightType: PFFEventHeightType | None
    ballMoving: bool
    betterOptionPlayer: PFFEventPlayerIdNickname | None
    betterOptionTime: str | None
    betterOptionType: PFFEventBetterOptionType | None
    blockerPlayer: PFFEventPlayerIdNickname | None
    bodyMovementType: PFFEventBodyMovementType | None
    clearerPlayer: PFFEventPlayerIdNickname | None
    createsSpace: bool | None
    createsSpaceVsPlayer: PFFEventPlayerIdNickname | None
    deflectorBodyType: PFFEventBodyType | None
    deflectorPlayer: PFFEventPlayerIdNickname | None
    failedInterventionPlayer: PFFEventPlayerIdNickname | None
    failedInterventionPlayer1: PFFEventPlayerIdNickname | None
    failedInterventionPlayer2: PFFEventPlayerIdNickname | None
    failedInterventionPlayer3: PFFEventPlayerIdNickname | None
    keeperTouchType: PFFEventBodyType | None
    late: bool | None
    missedTouchPlayer: PFFEventPlayerIdNickname | None
    missedTouchType: PFFEventMissedTouchType | None
    noLook: bool
    period: str | None
    pressurePlayer: PFFEventPlayerIdNickname | None
    pressureType: PFFEventPressureType | None
    saveHeightType: PFFEventShotHeightType | None
    saveReboundType: PFFEventSaveReboundType | None
    saveable: bool | None
    saverPlayer: PFFEventPlayerIdNickname | None
    shooterPlayer: PFFEventPlayerIdNickname | None
    shotBodyType: PFFEventBodyType | None
    shotInitialHeightType: PFFEventShotHeightType | None
    shotNatureType: PFFEventShotNatureType | None
    shotOutcomeType: PFFEventShotOutcomeType | None
    shotType: PFFEventShotType


class PFFEventPitch(BaseModel):
    model_config = ConfigDict(extra='forbid')

    length: float
    width: float
    startDate: datetime
    endDate: datetime
    # grassType: PFFEventStadiumGrassType


class PFFEventStadium(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    name: str
    pitches: list[PFFEventPitch] = Field(default_factory=list)


class PFFEventTeam(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    name: str
    shortName: str


class PFFEventKit(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    name: str
    primaryColor: str
    primaryTextColor: str
    secondaryColor: str
    secondaryTextColor: str


class PFFEventVideo(BaseModel):
    duration: float
    fps: float
    # game: PFFEventId
    id: str
    originalFilename: str
    # status: int
    videoUrl: str


class PFFEventGameEvent(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str

    advantageType: PFFEventAdvantageType | None
    bodyType: PFFEventBodyType | None
    defenderLocations: list[PFFEventLocation] | None = Field(default_factory=list)
    duration: float
    earlyDistribution: bool | None
    endTime: float | None
    endType: PFFEventEndType | None
    facingType: PFFEventFacingType | None
    formattedGameClock: str
    game: PFFEventId
    gameClock: float
    gameEventType: PFFEventEventType
    heightType: PFFEventHeightType
    initialTouchType: PFFEventInitialTouchType | None
    offenderLocations: list[PFFEventLocation] | None = Field(default_factory=list)
    otherPlayer: PFFEventPlayerIdNickname | None
    outType: PFFEventOutType | None
    period: int | None
    player: PFFEventPlayerIdNickname | None
    playerOff: PFFEventPlayerIdNickname | None
    playerOffType: PFFEventPlayerOffType | None
    playerOn: PFFEventPlayerIdNickname | None
    possessionEvents: list[PFFEventPossessionEvent] = Field(default_factory=list)
    pressurePlayer: PFFEventPlayerIdNickname | None
    pressureType: PFFEventPressureType | None
    setpieceType: PFFEventSetpieceType | None
    startTime: float
    subType: PFFEventSubType
    team: PFFEventTeam | None
    touches: int | None
    touchesInBox: int | None
    # video: PFFEventVideo | None
    videoAngleType: PFFEventVideoAngleType | None
    # videoMissing: bool | None
    videoUrl: str


class PFFEventGame(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    awayTeam: PFFEventTeam
    homeTeam: PFFEventTeam
    awayTeamKit: PFFEventKit
    homeTeamKit: PFFEventKit
    competition: PFFEventCompetition
    complete: bool
    date: datetime
    endPeriod1: float
    endPeriod2: float
    gameEvents: list[PFFEventGameEvent] = Field(default_factory=list)
    halfPeriod: float
    homeTeamStartLeft: bool
    homeTeamStartLeftExtraTime: bool
    period1: float
    period2: float
    rosters: list[PFFEventRoster] = Field(default_factory=list)
    season: str | int
    stadium: PFFEventStadium
    startPeriod1: float
    startPeriod2: float
    venue: str | None
    videos: list[PFFEventVideo] = Field(default_factory=list)
    week: int
