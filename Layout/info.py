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
        menu_table = Table(show_lines=True)
        menu_table.add_column("Author", justify="center")
        menu_table.add_column("by-speece", justify="center")

        menu_table.add_row(
                "Code Name",     "Spring Rain"
        )
        menu_table.add_row(
                "Version",       "0.2.1-unstable"
        )
        menu_table.add_row(
                "Build",        "250321"
        )
        menu_table.add_row(
                "Licence",      "GPL3"
        )
        menu_table.add_row(
                "Github",      "by-speece/RINDE"
        )
        return menu_table

def Coffee():
        menu_table = Table()
        menu_table.add_column("<-|New Dotations|->", justify="center")
        
        menu_table.add_row(
                "-------"
        )
        menu_table.add_row(
                "-------"
        )
        menu_table.add_row(
                "-------"
        )
        return menu_table