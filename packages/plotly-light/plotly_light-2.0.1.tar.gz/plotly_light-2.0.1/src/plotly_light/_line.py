from typing import Dict, List, Optional, Sequence, Tuple, Union

import plotly.graph_objects as go

from ._scatter import scatter

Coord = Tuple[int, int, int, int]


def lines(
    coords: Union[Coord, List[Coord]],
    text: Optional[Sequence] = None,
    width: float = 1,
    col: str = "black",
    opacity: Optional[float] = None,
    name: Optional[str] = None,
    show_legend: bool = False,
    show_init: bool = True,
    use_webgl: bool = False,
) -> go.Scatter:
    """For a collection of lines with same width and color. Returns as a Scatter object.

    positional arguments:
      @ coords : (A list of) coordinate (x0, y0, x1, y1).

    optional arguments:
      @ width       : Line width applied to all lines.
      @ col         : Line color applied to all lines.
      @ opacity     : Opacity of the lines.
      @ text        : Texts for each data.
      @ name        : Display name of the trace in the legend.
      @ show_legend : Show this trace in legend.
      @ use_webgl   : Use WebGL instead of SVG.
    """
    if not isinstance(coords, list):
        coords = [coords]

    return scatter(
        x=[x for x0, _, x1, _ in coords for x in (x0, x1, None)],
        y=[y for _, y0, _, y1 in coords for y in (y0, y1, None)],
        text=([x for t in text for x in (t, t, None)] if text is not None else text),
        mode="lines",
        line_width=width,
        col=col,
        opacity=opacity,
        name=name,
        show_legend=show_legend,
        show_init=show_init,
        use_webgl=use_webgl,
    )


def lines_shape(
    coords: Union[Coord, List[Coord]],
    width: float = 1,
    col: str = "black",
    opacity: Optional[float] = None,
    xref: str = "x",
    yref: str = "y",
    layer: str = "above",
) -> List[Dict]:
    """For a collection of lines with same width and color.

    positional arguments:
      @ coords : (A list of) coordinate (x0, y0, x1, y1).

    optional arguments:
      @ width       : Line width applied to all lines.
      @ col         : Line color applied to all lines.
      @ opacity     : Opacity of the lines.
      @ [x|y]ref    : Must be one of {'[x|y]', 'paper'}.
                      If "paper", values of `[x|y]0,1` must be within [0, 1]
                      and are interpreted as relative positions in the entire
                      [x|y]-axis.
      @ layer       : Drawing layer. Must be one of {'above', 'below'}.
    """

    def coord_to_shape(coord: Coord) -> Dict:
        x0, y0, x1, y1 = coord
        return dict(
            type="line",
            xref=xref,
            yref=yref,
            x0=x0,
            y0=y0,
            x1=x1,
            y1=y1,
            line=dict(color=col, width=width),
            opacity=opacity,
            layer=layer,
        )

    if not isinstance(coords, list):
        coords = [coords]

    return list(map(coord_to_shape, coords))
