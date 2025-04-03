import time
from pathlib import Path

from matplotlib.pyplot import close, savefig

from .frame import view_frame


def export_frame_sequence_as_png(
    frames: dict | list[dict],
    metadata: list[dict] | None = None,
    filename: str | None = None,
) -> list[str]:
    paths = []

    if isinstance(frames, dict):
        frames = [frames]

    if filename is None:
        filename = f'gandula_img_{int(time.time() * 1000)}'

    if filename.endswith('.png'):
        filename = filename[:-4]

    for index, frame in enumerate(frames):
        ax = view_frame(frame, metadata)
        fig = ax.get_figure()
        filepath = f'{filename}_{index}.png'
        savefig(filepath, bbox_inches='tight', dpi=100)
        paths.append(str(Path(filepath).resolve()))
        close(fig)

    return paths
