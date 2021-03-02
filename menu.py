#Import
import pyfiglet
import os
import rich

#Rich
from rich import print
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.layout import Layout
from rich.align import Align

#UI Modules
from menu_ui import *

#Commands
from custom_commands import *

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

console = Console()
layout = Layout()

def MainMenu():
      clear()

      MainMenuUI()
      MainMenuInput = input("Select an option:")
      if MainMenuInput == "1":
         PacmanMenu()

      if MainMenuInput == "5":
         PowerMenu()

      if MainMenuInput == "E":
         clear()
         exit()

def PacmanMenu():
         clear()
         pyfiglet.print_figlet("Pacman Settings",font="slant")
         PacmanMenuUI()
         PacmanMenuInput = input("Select an option:")

         if PacmanMenuInput == "1":
            clear()
            os.system('sudo pacman -Syu --noconfirm')
            print('Update Complete')
            MainMenu()

         if PacmanMenuInput == "2":
            clear()
            print('Updating Mirrorlist......')
            os.system('sudo reflector --verbose --latest 10 --sort rate --save /etc/pacman.d/mirrorlist')
            print('Updating Mirrorlist Completed!')
            print('Updating Repository Database and System......')
            os.system('sudo pacman -Syu --noconfirm')
            print('Updating Repository Database and System Completed!')
            print('Cleaning Pacman and System......')
            os.system('sudo pacman -Sc --noconfirm')
            os.system('sudo pacman -Rs $(pacman -Qtdq) --noconfirm')
            print('Cleaning Pacman and System Completed!')
            MainMenu()

         if PacmanMenuInput == "3":
            clear()
            PacmanPackagesMenuUI()

def PowerMenu():
         clear()
         pyfiglet.print_figlet("Power Menu",font="slant")
         PowerMenuUI()
         PowerMenuInput = input("Select an option:")

         if PowerMenuInput == "1":
            os.system("shutdown now")
            exit()

         if PowerMenuInput == "2":
            os.system("reboot now")
            exit()

         if PowerMenuInput == "3":
            os.system("systemctl suspend")
            MainMenu()

layout.split(
   Layout(Align.center("RINDE's not Desktop Enviroment", style="bold red"), name="Title"),
   Layout(name="Up"),
   Layout(name="Down"),
)


layout["Up"].split(
   Layout(Align.center(HotKeysUI()), name="UpLeft"),
   Layout(Align.center(MainMenuUI()), name="UpRight"),
   direction="horizontal"
)

layout["Down"].split(
   Layout(name="DownLeft"),
   Layout(name="DownRight"),
   direction="horizontal"
)

layout["DownLeft"].size = 63

print(layout)
