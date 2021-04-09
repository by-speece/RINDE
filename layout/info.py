#Import

import os
import rich
import pynput

#Rich
from rich import print
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.layout import Layout
from rich.align import Align
from rich.text import Text


def Author():
        menu_table = Table(show_lines=True, header_style="bold magenta")
        menu_table.add_column("Author", justify="center")
        menu_table.add_column("by-speece", justify="center")

        menu_table.add_row(
                "Code Name",     "Spring Rain"
        )
        menu_table.add_row(
                "Version",       "0.2.3-unstable"
        )
        menu_table.add_row(
                "Build",        "070421"
        )
        menu_table.add_row(
                "Licence",      "GPL3"
        )
        menu_table.add_row(
                "Github",      "by-speece/RINDE"
        )
        return menu_table

