#Import

import os
import rich

#Rich
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.panel import Panel
from rich.layout import Layout
from rich.align import Align

#Readchar - Key Reading Without Enter
import readchar

#UI Modules
from Layout.menu_ui import *
from Layout.info import *


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
current = set()
layout = Layout()

def MainMenu():
      clear()
      MainMenuLayout()
      MainMenuInput = readchar.readkey()
      if MainMenuInput == "1":
         PacmanMenu()

      if MainMenuInput == "2":
         YayMenu()

      if MainMenuInput == "3":
         AppsConfigsMenu()

      if MainMenuInput == "4":
         ExtraToolsMenu()

      if MainMenuInput == "5":
         SettingsMenu()

      if MainMenuInput == "6":
         RindeSettingsMenu()

      if MainMenuInput == "p":
         PowerMenu()
      
      if MainMenuInput == "r":
         MainMenu()

      if MainMenuInput == "q":
         clear()
         exit()

      else:
         MainMenu()

def PacmanMenu():
      clear()
      PacmanMenuLayout()
      PacmanMenuInput = readchar.readkey()
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
      
      if PacmanMenuInput == "b":
         MainMenu()

      if PacmanMenuInput == "q":
         clear()
         exit()
         
      else:
         PacmanMenu()


def PowerMenu():
         clear()
         PowerMenuLayout()
         PowerMenuInput = readchar.readkey()

         if PowerMenuInput == "1":
            os.system("shutdown now")
            exit()

         if PowerMenuInput == "2":
            os.system("reboot now")
            exit()

         if PowerMenuInput == "3":
            os.system("systemctl suspend")
            MainMenu()
         
         if PowerMenuInput == "b":
            MainMenu()

         if PowerMenuInput == "q":
            clear()
            exit()

         else:
            PowerMenu()


def ExtraToolsMenu():
         clear()
         console.print(Align.center(ExtraToolsMenuUI()))


MainMenu()


