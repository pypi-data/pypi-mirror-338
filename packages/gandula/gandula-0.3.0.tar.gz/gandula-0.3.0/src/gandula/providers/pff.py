import tempfile
from pathlib import Path

import orjson
import pandas as pd
from tqdm.auto import tqdm

from ..core.logging import get_logger
from ..io.reader import read_file, read_line
from .pff_gdrive_mapping import GDRIVE_FILE_IDS, PFF_MATCH_INFO

logger = get_logger(__name__)


def available() -> pd.DataFrame:
    return pd.DataFrame(PFF_MATCH_INFO)


def load_open_data(
    ids: int | list[int] | None = None,
    *,
    output_dir: str | None = None,
    events: bool = True,
    tracks: bool = True,
):
    if not events and not tracks:
        raise ValueError('At least one of events or tracks must be set to True')

    if isinstance(ids, int) and str(ids) not in GDRIVE_FILE_IDS:
        raise ValueError(f'Match {ids} not found')
    elif isinstance(ids, list) and all(str(_id) not in GDRIVE_FILE_IDS for _id in ids):
        raise ValueError(f'At least one match from {ids} was not found')

    if ids is None:
        logger.info('Loading all matches')
        matches = GDRIVE_FILE_IDS.keys()
    elif isinstance(ids, int):
        matches = [str(ids)]
    elif isinstance(ids, list):
        matches = [str(_id) for _id in ids]
    else:
        raise ValueError('Invalid match ID type')

    result = []
    for match_id in tqdm(matches, desc='Downloading matches'):
        try:
            data = _load_open_data_match(
                match_id,
                output_dir=output_dir,
                events=events,
                tracks=tracks,
            )
            result.append(data)
        except Exception as e:
            logger.exception(f'Error loading match {match_id}: {e}')
            continue

    if len(result) == 0:
        return []

    if len(result) == 1:
        return result[0]

    return result


def _load_open_data_match(
    id: str, *, output_dir: str | None = None, events=True, tracks=True
):
    output = None
    use_temp = output_dir is None

    if not use_temp:
        output = Path(output_dir)
        output.mkdir(parents=True, exist_ok=True)

    rosters_id = GDRIVE_FILE_IDS[id]['rosters']
    events_id = GDRIVE_FILE_IDS[id]['event']
    tracks_id = GDRIVE_FILE_IDS[id]['tracking']
    metadata_id = GDRIVE_FILE_IDS[id]['metadata']

    rosters = _load_from_gdrive(rosters_id, id, output, 'rosters')
    metadata = _load_from_gdrive(metadata_id, id, output, 'metadata')

    event_data = _load_from_gdrive(events_id, id, output, 'events') if events else None
    tracking_data = (
        _load_from_gdrive(tracks_id, id, output, 'tracks', track=True)
        if tracks
        else None
    )

    if events and tracks:
        return rosters, metadata, event_data, tracking_data

    return rosters, metadata, event_data or tracking_data


def _load_from_gdrive(
    id: str, match_id: str, output: Path | None, suffix: str | None, *, track=False
):
    if output is None:
        contents = None

        with tempfile.NamedTemporaryFile(delete_on_close=False) as fp:
            fp.close()

            import gdown

            gdown.download(id=id, output=fp.name, quiet=True)

            if track:
                contents = [orjson.loads(line) for line in read_line(fp.name, bz2=True)]
            else:
                contents = orjson.loads(read_file(fp.name))

        return contents

    if not suffix:
        output_file = output / f'{match_id}.json'
    else:
        output_file = output / f'{match_id}_{suffix}.json'

    import gdown

    gdown.download(id=id, output=str(output_file), quiet=True)
    return output_file
