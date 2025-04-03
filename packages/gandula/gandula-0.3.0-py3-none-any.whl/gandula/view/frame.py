from typing import cast

import matplotlib.pyplot as plt
from IPython.display import HTML
from matplotlib.animation import FuncAnimation
from matplotlib.axes import Axes
from mplsoccer import Pitch

player_opts = {'s': 169, 'alpha': 0.8, 'linewidths': 1, 'marker': 'o'}
shirt_opts = {'ha': 'center', 'va': 'center', 'fontsize': 8, 'fontweight': 'bold'}
ball_opts = {'facecolor': 'black', 'edgecolor': 'lightyellow'}


def view_frame(frame: dict, metadata: list[dict] | None = None, ax: Axes | None = None):
    pitch = Pitch(pitch_type='impect', linewidth=1, line_alpha=0.8, goal_alpha=0.8)  # type: ignore
    if ax:
        pitch.draw(ax=ax)
    else:
        _, ax = pitch.draw()  # type: ignore
        ax = cast(Axes, ax)

    home_kit = metadata[0]['homeTeamKit'] if metadata else None
    away_kit = metadata[0]['awayTeamKit'] if metadata else None

    colors = {
        'home': (
            (home_kit['primaryColor'], home_kit['primaryTextColor'])
            if home_kit
            else ('darkred', 'white')
        ),
        'away': (
            (away_kit['primaryColor'], away_kit['primaryTextColor'])
            if away_kit
            else ('darkblue', 'white')
        ),
    }

    for side in ['home', 'away']:
        for player in frame[f'{side}PlayersSmoothed']:
            _plot_player(player, colors[side], ax)

    ball = frame['ballsSmoothed'] or (frame['balls'][0] if frame['balls'] else None)
    if ball:
        ball_x = ball['x']
        ball_y = ball['y']
        ax.scatter(ball_x, ball_y, **ball_opts, zorder=2)  # type: ignore

    return ax


def _plot_player(player: dict, colors: tuple, ax: Axes):
    x = player['x']
    y = player['y']
    shirt = player['jerseyNum']
    ax.scatter(x, y, facecolor=colors[0], edgecolor='black', **player_opts)
    if shirt:
        ax.text(x, y, str(shirt), c=colors[1], **shirt_opts, zorder=2)


def view_frame_sequence(
    frames: list[dict],
    metadata: list[dict] | None = None,
    *,
    ax: Axes | None = None,
    fps=30,
):
    pitch = Pitch(pitch_type='impect', linewidth=1, line_alpha=0.8, goal_alpha=0.8)  # type: ignore
    if ax:
        pitch.draw(ax=ax)
    else:
        fig, ax = pitch.draw()  # type: ignore
        ax = cast(Axes, ax)

    home_kit = metadata[0]['homeTeamKit'] if metadata else None
    away_kit = metadata[0]['awayTeamKit'] if metadata else None

    colors = {
        'home': (
            (home_kit['primaryColor'], home_kit['primaryTextColor'])
            if home_kit
            else ('darkred', 'white')
        ),
        'away': (
            (away_kit['primaryColor'], away_kit['primaryTextColor'])
            if away_kit
            else ('darkblue', 'white')
        ),
    }

    home_scatter = ax.scatter(
        [],
        [],
        facecolor=colors['home'][0],
        edgecolor='black',
        **player_opts,
    )
    away_scatter = ax.scatter(
        [],
        [],
        facecolor=colors['away'][0],
        edgecolor='black',
        **player_opts,
    )
    ball_scatter = ax.scatter([], [], **ball_opts, zorder=2)
    shirts = [ax.text(0, 0, '', **shirt_opts) for _ in range(22)]

    def update(frame_idx):
        nonlocal shirts

        frame = frames[frame_idx]

        home_positions = [[p['x'], p['y']] for p in frame['homePlayersSmoothed']]
        home_scatter.set_offsets(home_positions)

        away_positions = [[p['x'], p['y']] for p in frame['awayPlayersSmoothed']]
        away_scatter.set_offsets(away_positions)

        ball = frame['ballsSmoothed'] or (frame['balls'][0] if frame['balls'] else None)
        if ball:
            ball_x = ball['x']
            ball_y = ball['y']
            ball_position = [[ball_x, ball_y]]
            ball_scatter.set_offsets(ball_position)
            ball_scatter.set_visible(True)
        else:
            ball_scatter.set_visible(False)

        shirt_index = 0
        for pos, player in zip(
            home_positions, frame['homePlayersSmoothed'], strict=False
        ):
            x, y = pos[0], pos[1]
            shirts[shirt_index].set_position((x, y))
            shirts[shirt_index].set_text(str(player['jerseyNum']))
            shirts[shirt_index].set_color(colors['home'][1])
            shirts[shirt_index].set_visible(True)
            shirt_index += 1

        for pos, player in zip(
            away_positions, frame['awayPlayersSmoothed'], strict=False
        ):
            x, y = pos[0], pos[1]
            shirts[shirt_index].set_position((x, y))
            shirts[shirt_index].set_text(str(player['jerseyNum']))
            shirts[shirt_index].set_color(colors['away'][1])
            shirts[shirt_index].set_visible(True)
            shirt_index += 1

        for i in range(shirt_index, len(shirts)):
            shirts[i].set_visible(False)

        return (home_scatter, away_scatter, ball_scatter, *shirts)

    anim = FuncAnimation(
        fig,
        update,
        frames=len(frames),
        blit=True,
        interval=1000 / 30,
        repeat_delay=5000,
    )

    html_output = anim.to_jshtml()
    plt.close(fig)

    return HTML(html_output)
