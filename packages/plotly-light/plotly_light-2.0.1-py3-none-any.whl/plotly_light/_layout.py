from typing import Dict, List, Optional, Tuple, Union

import plotly.graph_objects as go


def layout(
    # plot size
    width: Optional[int] = None,
    height: Optional[int] = None,
    # plot range
    x_range: Optional[Tuple[Optional[float], Optional[float]]] = None,
    y_range: Optional[Tuple[Optional[float], Optional[float]]] = None,
    # overall font
    font: Optional[str] = None,
    font_col: Optional[str] = None,
    font_size: Optional[int] = None,
    # title
    title: Optional[str] = None,
    x_title: Optional[str] = None,
    y_title: Optional[str] = None,
    x_titlefontsize: Optional[int] = None,
    y_titlefontsize: Optional[int] = None,
    # grids
    x_grid: Optional[bool] = None,
    y_grid: Optional[bool] = None,
    grid_col: Optional[str] = None,
    x_zeroline: Optional[bool] = None,
    y_zeroline: Optional[bool] = None,
    zeroline_col: Optional[str] = None,
    x_bounding_line: Optional[bool] = None,
    y_bounding_line: Optional[bool] = None,
    bounding_line_col: Optional[str] = None,
    bounding_line_width: Optional[float] = None,
    x_mirror: Optional[Union[bool, str]] = None,
    y_mirror: Optional[Union[bool, str]] = None,
    # axes
    anchor_axes: Optional[bool] = None,
    x_category: Optional[bool] = None,
    y_category: Optional[bool] = None,
    x_logscale: Optional[bool] = None,
    y_logscale: Optional[bool] = None,
    x_reversed: Optional[bool] = None,
    y_reversed: Optional[bool] = None,
    # axis ticks
    x_ticks: Optional[Union[str, bool]] = None,
    y_ticks: Optional[Union[str, bool]] = None,
    x_ticks_minor: Optional[Union[str, bool]] = None,
    y_ticks_minor: Optional[Union[str, bool]] = None,
    x_dtick: Optional[int] = None,
    y_dtick: Optional[int] = None,
    x_ticklabel: Optional[bool] = None,
    y_ticklabel: Optional[bool] = None,
    x_tickformat: Optional[str] = None,
    y_tickformat: Optional[str] = None,
    x_tickfontsize: Optional[int] = None,
    y_tickfontsize: Optional[int] = None,
    x_standoff: Optional[int] = None,
    y_standoff: Optional[int] = None,
    tick_col: Optional[str] = None,
    tick_len: Optional[float] = None,
    tick_width: Optional[float] = None,
    # legend
    show_legend: Optional[bool] = None,
    legend_horizontal: Optional[bool] = None,
    legend_coord: Optional[Tuple[Optional[float], Optional[float]]] = None,
    legend_border_col: Optional[str] = None,
    legend_border_width: Optional[int] = None,
    margin: Optional[Dict] = None,
    # shapes
    shapes: Optional[List[Dict]] = None,
    # bar plot
    barmode: Optional[str] = None,
    # interactive features
    hovermode: Optional[Union[str, bool]] = None,
) -> go.Layout:
    """Create a minimal Layout object.

    optional arguments:
      @ width                : Width of the plot.
      @ height               : Height of the plot.
      @ font                 : Font of characters in the plots.
      @ font_col             : Font color of charactoers in the plots.
      @ font_size_[title|axis_title|axis_tick|legend]
                             : Font size of title/x,y_title/x,y_tick/legend.
      @ title                : Title of the plot.
      @ [x|y]_title          : Title of [x|y]-axis of the plot.
      @ [x|y]_range          : Range on [x|y]-axis to be drawn in the plot.
      @ [x|y]_category       : Use categorical (string) labels for [x|y]-axis if True.
      @ [x|y]_logscale       : Use log scale for [x|y]-axis if True.
      @ [x|y]_grid           : Show grid on [x|y]-axis if True.
      @ [x|y]_zeroline       : Show zeroline on [x|y]-axis if True.
      @ [x|y]_reversed       : Reverse [x|y]-axis if True.
      @ [x|y]_ticks          : {"" (or False; default), "outside" (or True), "inside"}.
      @ [x|y]_dtick          : Distance between two adjacent ticks.
      @ [x|y]_ticklabel      : Show tick labels of [x|y]-axis if True.
      @ [x|y]_tickformat     : e.g. ",.0f" (integer w/ commas), "%"
      @ [x|y]_standoff       : Size (in px) of the margin between tick labels and axis title.
      @ [x|y]_bounding_line  : Show line bewteen axis and plot if True.
      @ [x|y]_mirror         : {True, "ticks", False, "all", "allticks"}.
                               Show bounding line/ticks on the other side of the plot.
      @ anchor_axes          : Use same scale for both x/y axes.
      @ [grid|zeroline]_col  : Color of the grids and the zerolines.
      @ tick_[col|len|width] : Color/length/width of the ticks.
      @ bounding_line_[col|width]
                             : Color/width of the ticks.
      @ show_legend          : Show legend if True.
      @ legend_horizontal    : Shoe legend horizontally if True.
      @ legend_coord         : Relative coordinate (x, y) of the legend.
                               Default: (x, y) = (1.02, 1).
      @ legend_border_[col|width]
                             : Color/width for the borderlines of the legend box.
      @ margin               : Margin of the plot. Any number of keys can be specified.
                               Default: `dict(t=50, b=10, l=10, r=10, pad=0)`.
      @ shapes               : List of non-interactive shape objects.
      @ barmode              : {"group" (default), "stack", "overlay", "relative"}.
      @ hovermode            : {"closest" (default), "[x|y] [unified]", False}.
    """
    return go.Layout(
        width=width,
        height=height,
        hovermode=hovermode,
        font=dict(family=font, size=font_size, color=font_col),
        title=dict(text=title),
        xaxis=dict(
            title=dict(
                text=x_title, font=dict(size=x_titlefontsize), standoff=x_standoff
            ),
            type=(
                "category"
                if x_category is True
                else "log" if x_logscale is True else None
            ),
            autorange="reversed" if x_reversed is True else None,
            showline=x_bounding_line,
            mirror=x_mirror,
            showgrid=x_grid,
            zeroline=x_zeroline,
            showticklabels=x_ticklabel,
            range=x_range,
            ticks="outside" if x_ticks is True else "" if x_ticks is False else x_ticks,
            minor_ticks=(
                "outside"
                if x_ticks_minor is True
                else "" if x_ticks_minor is False else x_ticks_minor
            ),
            dtick=x_dtick,
            tickformat=x_tickformat,
            tickfont=dict(size=x_tickfontsize),
            ticklen=tick_len,
            tickwidth=tick_width,
            gridcolor=grid_col,
            zerolinecolor=zeroline_col,
            tickcolor=tick_col,
            linecolor=bounding_line_col,
            linewidth=bounding_line_width,
        ),
        yaxis=dict(
            title=dict(
                text=y_title, font=dict(size=y_titlefontsize), standoff=y_standoff
            ),
            type=(
                "category"
                if y_category is True
                else "log" if y_logscale is True else None
            ),
            autorange="reversed" if y_reversed is True else None,
            scaleanchor="x" if anchor_axes is True else None,
            showline=y_bounding_line,
            mirror=y_mirror,
            showgrid=y_grid,
            zeroline=y_zeroline,
            showticklabels=y_ticklabel,
            range=y_range,
            ticks="outside" if y_ticks is True else "" if y_ticks is False else y_ticks,
            minor_ticks=(
                "outside"
                if y_ticks_minor is True
                else "" if y_ticks_minor is False else y_ticks_minor
            ),
            dtick=y_dtick,
            tickformat=y_tickformat,
            tickfont=dict(size=y_tickfontsize),
            ticklen=tick_len,
            tickwidth=tick_width,
            gridcolor=grid_col,
            zerolinecolor=zeroline_col,
            tickcolor=tick_col,
            linecolor=bounding_line_col,
            linewidth=bounding_line_width,
        ),
        showlegend=show_legend,
        legend=dict(
            orientation="h" if legend_horizontal else None,
            bordercolor=legend_border_col,
            borderwidth=legend_border_width,
            x=None if legend_coord is None else legend_coord[0],
            y=None if legend_coord is None else legend_coord[1],
        ),
        margin=margin,
        shapes=shapes,
        barmode=barmode,
    )


def merge_layout(base_layout, *layouts) -> go.Layout:
    """Merge multiple layouts. The `base_layout` is iteratively updated by each
    of the other layouts in the order of arguments.
    """
    if not isinstance(base_layout, go.Layout):
        base_layout = layout().update(base_layout)
    for _layout in layouts:
        base_layout = base_layout.update(_layout)
    return base_layout
