#Import

import os
import rich

#Rich
from rich import print
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.panel import Panel
from rich.layout import Layout
from rich.align import Align
from rich.text import Text

#Readchar - Key Reading Without Enter
import readchar

#Another stuff
def Author():
        menu_table = Table(show_lines=True, header_style="bold magenta")
        menu_table.add_column("Author", justify="center")
        menu_table.add_column("by-speece", justify="center")

        menu_table.add_row(
                "Code Name",     "Spring Rain"
        )
        menu_table.add_row(
                "Version",       "0.3.4-testing"
        )
        menu_table.add_row(
                "Build",        "270421"
        )
        menu_table.add_row(
                "Licence",      "GPL3"
        )
        menu_table.add_row(
                "Github",      "by-speece/RINDE"
        )
        return menu_table