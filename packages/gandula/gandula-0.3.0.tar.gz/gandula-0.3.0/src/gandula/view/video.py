"""Implements functionality for watching videos of possession events."""

from typing import cast
from uuid import uuid4

from bs4 import Tag
from IPython import get_ipython  #  type: ignore
from IPython.display import HTML, display

from ..core.config import get_config_value
from ..html_templates import env


def _scrape_playlist_from_pff_video(url: str) -> str:
    """Scrape PFF video details from a given URL.

    Parameters:
    -----------
    url : HttpUrl
        The URL we want to scrape.

    Returns:
    --------
    str
        The url to the m3u8 playlist.
    """
    import requests
    from bs4 import BeautifulSoup

    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f'Failed to load video. status_code={response.status_code}')

    soup = BeautifulSoup(response.text, 'html.parser')
    video = soup.find('video')

    if not video:
        raise ValueError('Failed to find the <video> element in the page.')

    video = cast(Tag, video)

    return video.get('data-playlist-url')  # type: ignore


def video(
    event: dict,
    *,
    width: int | str = '80%',
    height: int | str = 'auto',
    start_buffer_sec: float | None = None,
    end_buffer_sec: float | None = None,
) -> None:
    """Display a video for a PFF_PossessionEvent on IPython environments."""
    buffer = get_config_value('visualization', 'video_buffer_sec')
    if start_buffer_sec is None:
        start_buffer_sec = buffer
    if end_buffer_sec is None:
        end_buffer_sec = buffer

    if not get_ipython():
        raise RuntimeError('This function is only available on IPython environments')

    if not event['gameEvents']['videoUrl']:
        raise ValueError('No video URL found for this event.')

    # this is temporary fix as PFF is serving the url without the film_room
    split_url = event['gameEvents']['videoUrl'].split('/')
    event_path = '/'.join(split_url[1:])
    # film_room_url = f'https://epitome-staging.pff.com/en/film_room/{event_path}'
    film_room_url = event['gameEvents']['videoUrl']

    playlist_url = _scrape_playlist_from_pff_video(film_room_url)
    blob_url = f'blob:https://epitome-staging.pff.com/{split_url[1]}'

    video_vars = {
        'width': width,
        'height': height,
        'event_id': f'{event['gameEventId']}-{uuid4()}',
        'start_position': float(event['startTime']) - start_buffer_sec,  # type: ignore
        'end_position': float(event['endTime']) + end_buffer_sec,  # type: ignore
        'playlist_url': playlist_url,
        'video_url': blob_url,
    }

    video_template = env.get_template('video.jinja2')

    display(HTML(video_template.render(video_vars)))
