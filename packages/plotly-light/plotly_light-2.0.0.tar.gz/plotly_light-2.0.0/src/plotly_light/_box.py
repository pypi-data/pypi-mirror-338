from typing import Any, List, Optional, Sequence, Tuple, Union

import plotly.graph_objects as go

from . import default


def box(
    data: Sequence[Any],
    text: Optional[Sequence[str]] = None,
    name: Optional[str] = None,
    col: Optional[str] = None,
    opacity: float = 1,
    show_points: bool = False,
    only_points: bool = False,
    marker_size: Optional[float] = None,
    horizontal: bool = False,
    show_legend: bool = False,
    show_init: bool = True,
) -> go.Box:
    """Create a simple Trace object of a box plot.

    positional arguments:
      @ data : Sequence (of sequence(s)) of data values.

    optional arguments:
      @ name        : Display name of the trace in legend and plot.
      @ col         : Color of the plot.
      @ opacity     : Opacity of the plot.
      @ show_points : Plot markers as well as the box.
      @ only_points : Plot only markers and hide the box.
      @ show_legend : Show this trace in legend.
      @ show_init   : Show this trace initially.
    """
    return go.Box(
        x=data if horizontal else None,
        y=data if not horizontal else None,
        text=text,
        orientation="h" if horizontal else None,
        boxpoints="all" if show_points or only_points else None,
        pointpos=0 if only_points else None,
        hoveron="points" if only_points else None,
        fillcolor="rgba(255,255,255,0)" if only_points else None,
        line={"color": "rgba(255,255,255,0)"} if only_points else None,
        marker={
            "color": (
                default.layout["colorway"][0] if col is None and only_points else col
            ),
            "size": marker_size,
        },
        opacity=opacity,
        name=name,
        showlegend=show_legend,
        visible=None if show_init else "legendonly",
    )


def violin(
    data: Sequence[Any],
    text: Optional[Sequence[str]] = None,
    name: Optional[str] = None,
    col: Optional[str] = None,
    opacity: float = 1,
    side: Optional[str] = None,
    pointpos: Optional[float] = None,
    show_box: bool = False,
    show_points: bool = False,
    horizontal: bool = False,
    show_legend: bool = False,
    show_init: bool = True,
) -> go.Box:
    """Create a simple Trace object of a box plot.

    positional arguments:
      @ data : Sequence (of sequence(s)) of data values.

    optional arguments:
      @ name        : Display name of the trace in legend and plot.
      @ col         : Color of the plot.
      @ opacity     : Opacity of the plot.
      @ side        : Must be one of {None, "positive", "negative"}.
      @ show_box    : Show the box plot.
      @ show_points : Plot markers as well as the box.
      @ show_legend : Show this trace in legend.
      @ show_init   : Show this trace initially.
    """
    if side == "positive" and pointpos is None:
        pointpos = 1
    return go.Violin(
        x=data if horizontal else None,
        y=data if not horizontal else None,
        text=text,
        orientation="h" if horizontal else None,
        box_visible=show_box,
        points="all" if show_points else None,
        marker={"color": col},
        opacity=opacity,
        side=side,
        pointpos=pointpos,
        name=name,
        showlegend=show_legend,
        visible=None if show_init else "legendonly",
    )
