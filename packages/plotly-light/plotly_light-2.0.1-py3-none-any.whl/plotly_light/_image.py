from typing import Optional, Tuple

import PIL.Image
import plotly.graph_objects as go
from IPython.display import Image, display
from logzero import logger

from . import _layout, _show


def image(
    in_fname: str,
    width: Optional[int] = None,
    height: Optional[int] = None,
    x_range: Optional[Tuple[int, int]] = None,
    y_range: Optional[Tuple[int, int]] = None,
    layer: str = "above",
    opacity: Optional[float] = None,
    layout: go.Layout = None,
    verbose: bool = False,
):
    img = PIL.Image.open(in_fname)
    iw, ih = img.size
    ar = ih / iw

    if x_range is not None:
        xb, xe = x_range
        if y_range is not None:
            yb, ye = y_range
        else:
            yb, ye = 0, (xe - xb) * ar
    else:
        if y_range is not None:
            yb, ye = y_range
            xb, xe = 0, (ye - yb) / ar
        else:
            xb, xe = 0, iw
            yb, ye = 0, ih

    if width is not None:
        if height is not None:
            width, height = min(width, height / ar), min(height, width * ar)
        else:
            height = width * ar
    else:
        if height is not None:
            width = height / ar
        else:
            width, height = iw, ih

    # if width < 10:
    #     logger.warning(
    #         f"Width ({width:.1f}) is too small. Setting the minimum value, 10."
    #     )
    #     width = 10
    # if height < 10:
    #     logger.warning(
    #         f"Height ({height:.1f}) is too small. Setting the minimum value, 10."
    #     )
    #     height = 10

    if verbose:
        logger.info(
            f"plot = W {width:.1f} x H {height:.1f}, range = x[{xb:.1f}..{xe:.1f}] - y[{yb:.1f}..{ye:.1f}]"
        )

    fig = go.Figure(
        layout=_layout.merge_layout(
            _layout.layout(
                width=width,
                height=height,
                x_zeroline=False,
                y_zeroline=False,
                x_range=(xb, xe),
                y_range=(yb, ye),
                anchor_axes=True,
                margin=dict(l=0, r=0, t=0, b=0),
            ),
            layout,
        )
    )
    if x_range is None and y_range is None:
        fig.update_layout(
            xaxis=dict(showticklabels=False),
            yaxis=dict(showticklabels=False),
        )
    fig.add_layout_image(
        dict(
            source=img,
            xref="x",
            yref="y",
            x=xb,
            y=ye,
            sizex=xe - xb,
            sizey=ye - yb,
            sizing="stretch",
            layer=layer,
            opacity=opacity,
        )
    )
    return fig


def show_image(
    fname: str,
    static: bool = False,
    width: Optional[int] = None,
    height: Optional[int] = None,
    x_range: Optional[Tuple[int, int]] = None,
    y_range: Optional[Tuple[int, int]] = None,
    layer: str = "above",
    opacity: Optional[float] = None,
    layout: go.Layout = None,
    return_fig: bool = False,
    verbose: bool = False,
) -> None:
    """Quick utility for plotting an image file in Jupyter Notebook.

    positional arguments:
      @ fname : Name of the image file.

    optional arguments:
      @ static         : If True, show the image as a non-interactive, static plot.
      @ width | height : Of the image.
    """
    if static:
        assert not return_fig, "`return_fig` must not be True for static image"
        display(Image(fname, width=width, height=height))
        return

    fig = image(fname, width, height, x_range, y_range, layer, opacity, layout, verbose)

    if return_fig:
        return fig

    _show.show(fig)
