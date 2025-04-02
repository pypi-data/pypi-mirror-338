from logzero import logger as _logger

from . import default
from ._bar import bar
from ._box import box, violin
from ._config import (
    set_default_colors,
    set_default_config,
    set_default_layout,
    set_default_renderer,
    set_default_theme,
    update_default_config,
    update_default_layout,
)
from ._const import IFRAME_DIR, colors
from ._crawl import _remove_unused_htmls
from ._histogram import hist
from ._image import image, show_image
from ._layout import layout, merge_layout
from ._line import lines, lines_shape
from ._rectangle import rect
from ._renderer import _set_custom_iframe_renderers
from ._scatter import scatter
from ._show import figure, show, show_mult
from ._type import BaseTraceType, Traces
from ._venn import venn

# Set default theme/layout/config of Plotly Light
set_default_theme(default.theme)
set_default_layout(default.layout)
set_default_config(default.config)


# If imported from an IPython environment, turn on the connected notebook mode.
# Moreover, if it is a Jupyter notebook, define and set a customized iframe renderer.
try:
    get_ipython()
except NameError:
    pass
except Exception as e:
    print(e)
else:
    import plotly.offline as _py

    _py.init_notebook_mode(connected=True)

    try:
        _set_custom_iframe_renderers()
    except Exception as e:
        print(e)
    else:
        set_default_renderer("iframe_connected")
        _remove_unused_htmls()

_logger.info(f"pl.default.renderer = {default.renderer}")
