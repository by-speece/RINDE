#Import
import pyfiglet
import os
import rich

#Rich
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown

#Colors
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def MainMenuUI():
        console = Console()
        menu_table = Table(show_header=True, header_style="bold magenta")
        menu_table.add_column("Number", justify="left")
        menu_table.add_column("Module Name", justify="left")
        menu_table.add_column("Last Update Date",style="dim", justify="right")
        menu_table.add_column("Version",style="dim", justify="center")

        menu_table.add_row(
                "1",        "Pacman Settings", "20-02-2021", "0.1"
        )

        menu_table.add_row(
                "2",  "Yet another Yogurth", "Work in Progress", "-"
        )

        menu_table.add_row(
                "3",   "Settings/Autorun Manager", "Work in Progress", "-"
        )

        menu_table.add_row(
                "4",    "Arch Helper", "Work in Progress", "-"
        )

        menu_table.add_row(
                "5",     "Power Manager", "Work in Progress", "-"
        )

        menu_table.add_row(
                "6",     "Rice Manager", "Work in Progress", "-"
        )

        menu_table.add_row(
                "7",       "Update Manager", "Work in Progress", "-"
        )

        menu_table.add_row(
                "8",        "Exit", "Work in Progress", "-"
        )

        console.print(menu_table)

def PacmanMenuUI():
        console = Console()
        menu_table = Table(show_header=True, header_style="bold magenta")
        menu_table.add_column("Number", justify="left")
        menu_table.add_column("Module Name", justify="left")
        menu_table.add_column("Last Update Date",style="dim", justify="right")

        menu_table.add_row(
                "1",        "Update Manager", "23.02.2021"
        )

        menu_table.add_row(
                "2",        "Full Update", "23.02.2021"
        )

        console.print(menu_table)


