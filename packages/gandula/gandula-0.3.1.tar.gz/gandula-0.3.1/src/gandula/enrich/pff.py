# Only possession event types with start_x, start_y, and maybe end_x, end_y.
POSSESSION_EVENT_TYPES_NEW_FORMAT = {
    'BALL_CARRY': 'BC',
    'PASS': 'PA',
    'SHOT': 'SH',
    'CHALLENGE': 'CH',
    'CROSS': 'CR',
    'CLEARANCE': 'CL',
}


def enhance_pff(events: list[dict], tracks) -> list[dict]:
    for event in events:
        try:
            add_starting_coordinates_from_freeze_frame(event)
            frame = find_event_end_frame(event, tracks)
            if frame:
                add_end_coordinates_from_frame(event, frame)
        except ValueError:
            continue
    return events


def add_starting_coordinates_from_freeze_frame(event: dict) -> dict:
    player_id = event['gameEvents']['playerId']
    for player in event['homePlayers'] + event['awayPlayers']:
        if player['playerId'] == player_id:
            event['x'] = player['x']
            event['y'] = player['y']
            return event
    # event['x'] = None
    # event['y'] = None
    # return event
    raise ValueError('Player not found in event')


def add_end_coordinates_from_frame(event: dict, frame: dict) -> dict:
    possession_event_type = event['possessionEvents']['possessionEventType']
    if possession_event_type is None:
        return event

    player_shirt = frame['game_event']['shirt_number']
    player = next(
        (
            player
            for player in frame['homePlayers'] + frame['awayPlayers']
            if player['jerseyNum'] == player_shirt
        ),
        None,
    )
    if player is None:
        return event

    event['end_x'] = player['x']
    event['end_y'] = player['y']
    return event


def find_event_end_frame(event: dict, tracks: list[dict]) -> dict | None:
    possession_event_type = event['possessionEvents']['possessionEventType']

    if possession_event_type == 'BC':
        frame = next(
            (
                track
                for track in tracks
                if track['possession_event_id'] == event['possessionEventId']
            ),
            None,
        )
        return frame
    elif possession_event_type in ['CL', 'CR', 'PA']:
        iterator = iter(tracks)
        _ = next(
            (
                track
                for track in iterator
                if track['possession_event_id'] == event['possessionEventId']
            ),
            None,
        )
        next_frame = next(
            (
                track
                for track in iterator
                if track['possession_event'] is not None
                and track['game_event_id'] is not None
                and track['possession_event']['possession_event_type'] != 'RE'
            ),
            None,
        )
        return next_frame
