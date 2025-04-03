import io
import time
from pathlib import Path

import imageio
from matplotlib.pyplot import close, savefig
from pygifsicle import optimize

from .frame import view_frame


def export_frame_sequence_as_gif(
    frames: list[dict],
    metadata: list[dict] | None = None,
    filename: str | None = None,
    fps=25,
) -> str:
    images = []

    if filename is None:
        filename = f'gandula_gif_{int(time.time() * 1000)}.gif'

    for frame in frames:
        ax = view_frame(frame, metadata)
        fig = ax.get_figure()

        buf = io.BytesIO()
        savefig(buf, format='png')
        buf.seek(0)
        images.append(imageio.mimread(buf))
        close(fig)
        buf.close()

    if not filename.endswith('.gif'):
        filename = f'{filename}.gif'

    with imageio.get_writer(filename, fps=fps, mode='I') as writer:
        for img in images:
            writer.append_data(img)

    optimize(filename)  # shrinks the gif size

    return str(Path(filename).resolve())
