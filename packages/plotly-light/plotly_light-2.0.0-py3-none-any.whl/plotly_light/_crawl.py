import glob
import json
from os import remove
from typing import List

from ._const import IFRAME_DIR


def _get_html_list_jupyter(fname: str) -> List[str]:
    """Get the list of plotly HTML file names in a jupyter notebook."""
    data = json.load(open(fname, "r"))
    plotly_htmls = []
    if "cells" in data:
        for cell in data["cells"]:
            if "outputs" not in cell:
                continue
            for output in cell["outputs"]:
                if "data" in output and "text/html" in output["data"]:
                    for html in output["data"]["text/html"]:
                        if html.startswith(f'src="{IFRAME_DIR}/') and html.endswith(
                            '.html"\n'
                        ):
                            plotly_htmls.append(html.split('"')[1].strip())
    return plotly_htmls


def _remove_unused_htmls() -> None:
    """Remove plot HTML files that are no longer used in the Notebook currently opened."""

    htmls_jupyter = set(
        [
            x
            for ipynb_file in glob.glob("*.ipynb")
            for x in _get_html_list_jupyter(ipynb_file)
        ]
    )
    for html in glob.glob(f"{IFRAME_DIR}/*.html"):
        if html not in htmls_jupyter:
            remove(html)
