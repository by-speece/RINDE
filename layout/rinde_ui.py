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


#UI Modules
from layout.rinde_ui import *
from data.version import *

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



###############################################################
#########################UI SECTION############################
###############################################################
def Hotkeys():
        menu_table = Table(show_lines=True, header_style="bold magenta")
        menu_table.add_column("Key", justify="center")
        menu_table.add_column("Function", justify="center")

        menu_table.add_row(
                "p", "PowerMenu"
        )
        menu_table.add_row(
                "b", "MainMenu"
        )
        menu_table.add_row(
                "q", "Quit"
        )
        return menu_table

def MainMenuUI():
        menu_table = Table(show_lines=True, header_style="bold magenta")
        menu_table.add_column("Number", justify="center")
        menu_table.add_column("Module Name", justify="center")


        menu_table.add_row(
                "1",     "Package Manager"
        )

        menu_table.add_row(
                "2",     "Yet another Yogurth"
        )

        menu_table.add_row(
                "3",     "Install apps with configs"
        )

        menu_table.add_row(
                "4",     "Extra scrips"
        )

        menu_table.add_row(
                "5",     "Arch Gnu/Linux Settings"
        )

        menu_table.add_row(
                "6",     "RINDE Settings"
        )


        return menu_table



def PacmanMenuUI():
        console = Console()
        menu_table = Table(show_lines=True, show_header=True, header_style="bold magenta")
        menu_table.add_column("Number", justify="center")
        menu_table.add_column("Module Name", justify="center")

        menu_table.add_row(
                "1",        "Fast Update"
        )

        menu_table.add_row(
                "2",        "Full Update"
        )
        return menu_table



def YayMenuUI():
        console = Console()
        menu_table = Table(show_lines=True, show_header=True, header_style="bold magenta")
        menu_table.add_column("Number", justify="center")
        menu_table.add_column("Module", justify="center")

        menu_table.add_row(
                "1",        "Fast Update"
        )
        menu_table.add_row(
                "2",        "Full Update"
        )
        return menu_table

def AppsConfigsMenuUI():
        console = Console()
        menu_table = Table(show_header=True, header_style="bold magenta")
        menu_table.add_column("Number", justify="center")
        menu_table.add_column("Module", justify="center")

        menu_table.add_row(
                "1",        "Samba"
        )
        return menu_table


def PowerMenuUI():
        console = Console()
        menu_table = Table(show_lines=True, show_header=True, header_style="bold magenta")
        menu_table.add_column("Number", justify="center")
        menu_table.add_column("Power Menu", justify="center")

        menu_table.add_row(
                "1",        "Shutdown"
        )
        menu_table.add_row(
                "2",        "Restart"
        )
        menu_table.add_row(
                "3",        "Suspend"
        )

        return menu_table

def RindeSettingsMenuUI():
        console = Console()
        menu_table = Table(show_lines=True, show_header=True, header_style="bold magenta")
        menu_table.add_column("Number", justify="center")
        menu_table.add_column("Module", justify="center")

        menu_table.add_row(
                "1",        "Autorun settings"
        )
        menu_table.add_row(
                "2",        "Check/Install Rinde Update"
        )
        menu_table.add_row(
                "3",        "Install rice"
        )
        menu_table.add_row(
                "4",        "Speece Apps Packs(with speece repo)"
        )
        menu_table.add_row(
                "5",        "Speece Apps Packs(without speece repo)"
        )


        return menu_table

def ExtraScriptsUI():
        console = Console()
        menu_table = Table(show_header=True, header_style="bold magenta")
        menu_table.add_column("Number", justify="center")
        menu_table.add_column("Module", justify="center")

        menu_table.add_row(
                "1",        ""


        return menu_table

def SettingsMenuUI():
        console = Console()
        menu_table = Table(show_header=True, header_style="bold magenta")
        menu_table.add_column("Number", justify="center")
        menu_table.add_column("Module", justify="center")

        menu_table.add_row(
                "1",        ""


        return menu_table
###############################################################
#########################Layout Section########################
###############################################################

def MainMenuLayout():
      #Layout-Start
      #########################################################
      layout = Layout()

      layout.split(
         Layout(name="left"),
         Layout(Panel(Align.center(MainMenuUI(), vertical="middle"))),
         direction="horizontal"
      )

      layout["left"].split(
         Layout(Panel(Align.center(Author(), vertical="middle"))),
         Layout(name="down")
      )
      layout["down"].ratio = 0.6
      layout["down"].update(
         Panel(Align.center(Hotkeys(), vertical="middle"))
      )

      print(layout)
      #########################################################
      #Layout-END

def PacmanMenuLayout():
      #Layout-Start
      #########################################################
      layout = Layout()

      layout.split(
         Layout(name="left"),
         Layout(Panel(Align.center(PacmanMenuUI(), vertical="middle"))),
         direction="horizontal"
      )

      layout["left"].split(
         Layout(Panel(Align.center(Author(), vertical="middle"))),
         Layout(name="down")
      )
      layout["down"].ratio = 0.6
      layout["down"].update(
         Panel(Align.center(Hotkeys(), vertical="middle"))
      )
      print(layout)
      #########################################################
      #Layout-END

def PowerMenuLayout():
      #Layout-Start
      #########################################################
      layout = Layout()

      layout.split(
         Layout(name="left"),
         Layout(Panel(Align.center(PowerMenuUI(), vertical="middle"))),
         direction="horizontal"
      )

      layout["left"].split(
         Layout(Panel(Align.center(Author(), vertical="middle"))),
         Layout(name="down")
      )
      layout["down"].ratio = 0.6
      layout["down"].update(
         Panel(Align.center(Hotkeys(), vertical="middle"))
      )
      print(layout)
      #########################################################
      #Layout-END

def YayMenuLayout():
      #Layout-Start
      #########################################################
      layout = Layout()

      layout.split(
         Layout(name="left"),
         Layout(Panel(Align.center(YayMenuUI(), vertical="middle"))),
         direction="horizontal"
      )

      layout["left"].split(
         Layout(Panel(Align.center(Author(), vertical="middle"))),
         Layout(name="down")
      )
      layout["down"].ratio = 0.6
      layout["down"].update(
         Panel(Align.center(Hotkeys(), vertical="middle"))
      )

      print(layout)
      #########################################################
      #Layout-END

def AppsConfigsMenuLayout():
      #Layout-Start
      #########################################################
      layout = Layout()

      layout.split(
         Layout(name="left"),
         Layout(Panel(Align.center(AppsConfigsMenuUI(), vertical="middle"))),
         direction="horizontal"
      )

      layout["left"].split(
         Layout(Panel(Align.center(Author(), vertical="middle"))),
         Layout(name="down")
      )
      layout["down"].ratio = 0.6
      layout["down"].update(
         Panel(Align.center(Hotkeys(), vertical="middle"))
      )

      print(layout)
      #########################################################
      #Layout-END

def RindeSettingsMenuLayout():
      #Layout-Start
      #########################################################
      layout = Layout()

      layout.split(
         Layout(name="left"),
         Layout(Panel(Align.center(RindeSettingsMenuUI(), vertical="middle"))),
         direction="horizontal"
      )

      layout["left"].split(
         Layout(Panel(Align.center(Author(), vertical="middle"))),
         Layout(name="down")
      )
      layout["down"].ratio = 0.6
      layout["down"].update(
         Panel(Align.center(Hotkeys(), vertical="middle"))
      )

      print(layout) 
      #########################################################
      #Layout-END

def ExtraScriptsLayout():
      #Layout-Start
      #########################################################
      layout = Layout()

      layout.split(
         Layout(name="left"),
         Layout(Panel(Align.center(ExtraScriptsUI(), vertical="middle"))),
         direction="horizontal"
      )

      layout["left"].split(
         Layout(Panel(Align.center(Author(), vertical="middle"))),
         Layout(name="down")
      )
      layout["down"].ratio = 0.6
      layout["down"].update(
         Panel(Align.center(Hotkeys(), vertical="middle"))
      )

      print(layout) 
      #########################################################
      #Layout-END

def SettingsMenuLayout():
      #Layout-Start
      #########################################################
      layout = Layout()

      layout.split(
         Layout(name="left"),
         Layout(Panel(Align.center(SettingsMenuUI(), vertical="middle"))),
         direction="horizontal"
      )

      layout["left"].split(
         Layout(Panel(Align.center(Author(), vertical="middle"))),
         Layout(name="down")
      )
      layout["down"].ratio = 0.6
      layout["down"].update(
         Panel(Align.center(Hotkeys(), vertical="middle"))
      )

      print(layout) 
      #########################################################
      #Layout-END