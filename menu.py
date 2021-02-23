#Import
import pyfiglet
import os
import rich

#Rich
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown

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

def MainMenu():
      clear()
      pyfiglet.print_figlet("RINDE Menu",font="slant")
      MainMenuUI()
      MainMenuInput = input("Select an option:")
      if MainMenuInput == "1":
         PacmanMenu()

def PacmanMenu():
         clear()
         pyfiglet.print_figlet("Pacman Settings",font="slant")
         PacmanMenuUI()
         PacmanMenuInput = input("Select an option:")
         if  PacmanMenuInput == "1":
            os.system('sudo pacman -Syu --noconfirm')
            print('Update Complete')
            MainMenu()
         if  PacmanMenuInput == "2":
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

MainMenu()
