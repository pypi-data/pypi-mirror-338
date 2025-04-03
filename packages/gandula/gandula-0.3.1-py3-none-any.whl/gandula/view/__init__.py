from typing import Literal

from matplotlib.axes import Axes

from .event import view_event
from .frame import view_frame, view_frame_sequence
from .gif import export_frame_sequence_as_gif
from .png import export_frame_sequence_as_png


def view(
    obj: dict | list[dict],
    metadata: list[dict] | None = None,
    export: Literal['gif', 'png'] | None = None,
    ax: Axes | None = None,
):
    if export is None:
        if isinstance(obj, list):
            if len(obj) > 0:
                if 'homePlayersSmoothed' in obj[0] or 'awayPlayersSmoothed' in obj[0]:
                    return view_frame_sequence(obj, metadata, ax=ax)
                else:
                    ax = None
                    for evt in obj:
                        if ax is None:
                            ax = view_event(evt, ax=ax)
                        else:
                            view_event(evt, ax=ax)
        elif isinstance(obj, dict):
            if 'homePlayersSmoothed' in obj or 'awayPlayersSmoothed' in obj:
                print('HERE')
                return view_frame(obj, metadata, ax=ax)
            else:
                print('THERE')
                return view_event(obj, ax=ax)
    elif export == 'gif':
        if isinstance(obj, list):
            return export_frame_sequence_as_gif(obj, metadata)
        else:
            raise ValueError('GIF export only works with frame sequences')
    elif export == 'png':
        if isinstance(obj, list):
            return export_frame_sequence_as_png(obj, metadata)
    else:
        raise ValueError('Invalid export format. Choose between "gif" and "png"')
