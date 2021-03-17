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
from modules.menu_ui import *

#Commands
from modules.custom_commands import *

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

def MainMenu():
      clear()
      console.print(Align.center(MainMenuUI()))
      MainMenuInput = input("Select an option:")
      if MainMenuInput == "1":
         PacmanMenu()

      if MainMenuInput == "2":
         YayMenu()

      if MainMenuInput == "3":
         AppsConfigsMenu()

      if MainMenuInput == "4":
         ExtratoolsMenu()

      if MainMenuInput == "5":
         SettingsMenu()

      if MainMenuInput == "6":
         RindeSettingsMenu()

      if MainMenuInput == "P":
         PowerMenu()

      if MainMenuInput == "S":
         RindeShell()

      if MainMenuInput == "E":
         clear()
         exit()

def PacmanMenu():
         clear()
         console.print(Align.center(PacmanMenuUI()))
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
         console.print(Align.center(PowerMenuUI()))
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



MainMenu()


