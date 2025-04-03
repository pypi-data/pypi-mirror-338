from typing import cast

from matplotlib.axes import Axes
from mplsoccer import Pitch


def view_event(event: dict, color='red', ax: Axes | None = None) -> Axes:
    pitch = Pitch(pitch_type='impect')
    if ax:
        pitch.draw(ax=ax)
    else:
        _, ax = pitch.draw()  # type: ignore
        ax = cast(Axes, ax)

    if event.get('end_x'):
        pitch.arrows(
            event['x'],
            event['y'],
            event['end_x'],
            event['end_y'],
            width=2,
            headwidth=5,
            headlength=5,
            color=color,
            ax=ax,
        )
    elif event.get('x'):
        pitch.scatter(event['x'], event['y'], color=color, ax=ax)

    return ax
