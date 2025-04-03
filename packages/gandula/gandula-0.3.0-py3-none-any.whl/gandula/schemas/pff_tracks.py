from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict


class PFFFrameJerseyConfidence(str, Enum):
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'


class PFFFrameVisibility(str, Enum):
    VISIBLE = 'VISIBLE'
    ESTIMATED = 'ESTIMATED'


class PFFFrameGameEventType(str, Enum):
    FIRST_KICK_OFF = 'FIRSTKICKOFF'
    SECOND_KICK_OFF = 'SECONDKICKOFF'
    THIRD_KICK_OFF = 'THIRDKICKOFF'
    FOURTH_KICK_OFF = 'FOURTHKICKOFF'
    # FIRST_HALF_KICKOFF = '1KO'
    # SECOND_HALF_KICKOFF = '2KO'
    END_OF_HALF = 'END'
    PBC_IN_PLAY = 'G'
    PLAYER_ON = 'ON'
    PLAYER_OFF = 'OFF'
    ON_THE_BALL = 'OTB'
    OUT_OF_PLAY = 'OUT'
    SUB = 'SUB'
    VIDEO_MISSING = 'VID'
    CLOCK = 'CLK'  # TODO: Check if this is correct


class PFFFrameSetPieceType(str, Enum):
    CORNER = 'C'
    DROP_BALL = 'D'
    FREE_KICK = 'F'
    GOAL_KICK = 'G'
    KICK_OFF = 'K'
    PENALTY = 'P'
    THROW_IN = 'T'


class PFFFramePlayer(BaseModel):
    model_config = ConfigDict(extra='forbid')

    jerseyNum: int  # ignore
    confidence: PFFFrameJerseyConfidence
    visibility: PFFFrameVisibility
    x: float
    y: float
    speed: float | None = None


class PFFFrameBall(BaseModel):
    model_config = ConfigDict(extra='forbid')

    visibility: PFFFrameVisibility
    x: float | None
    y: float | None
    z: float | None


class PFFFrameEvent(BaseModel):
    model_config = ConfigDict(extra='forbid')

    game_id: int
    game_event_type: PFFFrameGameEventType
    formatted_game_clock: str | None
    player_id: int | None
    team_id: int | None
    setpiece_type: PFFFrameSetPieceType | None = None
    touches: int | None = None
    touches_in_box: int | None = None
    start_time: float
    end_time: float | None = None
    duration: float | None = None
    video_missing: bool | None = False
    inserted_at: datetime | None = None
    updated_at: datetime | None = None
    start_frame: int
    end_frame: int
    sequence: int | None = None
    home_ball: int | None = None
    competition_id: int | None = None
    season: str | None = None
    shirt_number: int | None
    position_group_type: str | None
    home_team: int | None
    player_name: str | None = None
    team_name: str | None = None
    video_url: str | None = None


class PFFFramePossessionEventType(str, Enum):
    BALL_CARRY = 'BC'
    CHALLENGE = 'CH'  # includes dribbles
    CLEARANCE = 'CL'
    CROSS = 'CR'
    PASS = 'PA'
    REBOUND = 'RE'
    SHOT = 'SH'


class PFFFramePossession(BaseModel):
    model_config = ConfigDict(extra='forbid')

    duration: float | None = None
    end_time: float | None = None
    formatted_game_clock: str | None
    game_event_id: int
    game_id: int
    inserted_at: datetime | None = None
    possession_event_type: PFFFramePossessionEventType
    start_time: float
    updated_at: datetime | None = None
    start_frame: int
    end_frame: int | None = None
    video_url: str | None = None


class PFFFrame(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True, arbitrary_types_allowed=True, extra='forbid'
    )

    awayPlayers: list[PFFFramePlayer]
    awayPlayersSmoothed: list[PFFFramePlayer] | None
    balls: list[PFFFrameBall] | None
    ballsSmoothed: PFFFrameBall | None
    periodElapsedTime: float
    game_event: PFFFrameEvent | None
    game_event_id: int | None
    frameNum: int
    periodGameClockTime: float
    gameRefId: int | None
    generatedTime: datetime | None
    home_ball: int | None = None
    homePlayers: list[PFFFramePlayer]
    homePlayersSmoothed: list[PFFFramePlayer] | None
    period: int
    possession_event: PFFFramePossession | None
    possession_event_id: int | None
    sequence: int | None = None
    version: str | None
    videoTimeMs: float
    smoothedTime: datetime | None = None


class PFFFrames(BaseModel):
    frames: list[PFFFrame]
