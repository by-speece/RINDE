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
from layout.rinde_ui import *
from layout.info import *
from layout.custom_commands import *


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
         ExtraScrips()

      if MainMenuInput == "5":
         SettingsMenu()

      if MainMenuInput == "6":
         RindeSettingsMenu()
#Hotkeys-start
      if MainMenuInput == "p":
         PowerMenu()
      
      if MainMenuInput == "b":
         MainMenu()

      if MainMenuInput == "q":
         clear()
         exit()
#Hotkeys-end
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

#Hotkeys-start
      if PacmanMenuInput == "p":
         PowerMenu()
      
      if PacmanMenuInput == "b":
         MainMenu()

      if PacmanMenuInput == "q":
         clear()
         exit()
#Hotkeys-end
      else:
         PacmanMenu()

def YayMenu():
      clear()
      YayMenuLayout()
      YayMenuInput = readchar.readkey()
      if YayMenuInput == "1":
         clear()
         os.system('yay -Syu --noconfirm')
         print('Update Complete')
         MainMenu()

      if YayMenuInput == "2":
         clear()
         os.system('yay -Syu --noconfirm')
         os.system('yay -Sc --noconfirm')
         os.system('yay -Rs $(yay -Qtdq) --noconfirm')
         MainMenu()

#Hotkeys-start
      if YayMenuInput == "p":
         PowerMenu()
      
      if YayMenuInput == "b":
         MainMenu()

      if YayMenuInput == "q":
         clear()
         exit()
#Hotkeys-end
      else:
         YayMenu()

def AppsConfigsMenu():
      clear()
      AppsConfigsMenuLayout()
      AppsConfigsMenuInput = readchar.readkey()
      if AppsConfigsMenuInput == "1":
         clear()
         os.system('sudo pacman -Syu samba --needed --noconfirm')
         os.system('sudo cp -rf /etc/rinde/data/samba  /etc/samba')
         os.system('sudo systemctl enable smb.service')
         print("Please create samba user using command: smbpasswd -a user_name")
         input("Press any key to continue...(pls dont press power button ;)")
         MainMenu()

      if AppsConfigsMenuInput == "2":
         clear()
         MainMenu()

#Hotkeys-start
      if AppsConfigsMenuInput == "p":
         PowerMenu()
      
      if AppsConfigsMenuInput == "b":
         MainMenu()

      if AppsConfigsMenuInput == "q":
         clear()
         exit()
#Hotkeys-end
      else:
         AppsConfigsMenu()

def ExtraScrips():
         clear()

def SettingsMenu():
         clear()

def RindeSettingsMenu():
         clear()

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
#Hotkeys-start
      if PowerMenuInput == "p":
         PowerMenu()
      
      if PowerMenuInput == "b":
         MainMenu()

      if PowerMenuInput == "q":
         clear()
         exit()
#Hotkeys-end
      else:
         PowerMenu()


MainMenu()


