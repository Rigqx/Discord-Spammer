import pyautogui
import random
import os, requests, time, random, sys
from time import sleep
from time import *
import pprint
from os import system
from subprocess import call
from subprocess import Popen
import ctypes
from colorama import init, Fore
from colorama import Fore, Back, Style
import socket
import json
import asyncio
import time
import threading
import traceback
from os import system
from random import randint
from discord.ext import commands
import re
import httpx
from colorama import Fore, init
import platform
import getpass
import smtplib

def Spam(command):
	print ("""

	You have 5 Seconds to go into minecraft ;)

	""")
	sleep(5)
	start_time = time.time()
	seconds = 20

	pyautogui.press('esc')

	while True:
		current_time = time.time()
		elapsed_time = current_time - start_time

		ctypes.windll.kernel32.SetConsoleTitleW("Minecraft Command Spammer | Stopping in 20 Secondst | MCS")

		pyautogui.press('t')
		pyautogui.write(command)
		pyautogui.press('enter')		

		if elapsed_time > seconds:
			break	
	main()	

def main():	
	os.system("cls")
	os.system("color c")
	ctypes.windll.kernel32.SetConsoleTitleW("Minecraft Command Spammer | MCS")	
	print("""

	 ███▄ ▄███▓ ▄████▄	██████ 
	▓██▒▀█▀ ██▒▒██▀ ▀█  ▒██	▒ 
	▓██	▓██░▒▓█	▄ ░ ▓██▄   
	▒██	▒██ ▒▓▓▄ ▄██▒  ▒   ██▒
	▒██▒   ░██▒▒ ▓███▀ ░▒██████▒▒
	░ ▒░   ░  ░░ ░▒ ▒  ░▒ ▒▓▒ ▒ ░
	░  ░	  ░  ░  ▒   ░ ░▒  ░ ░
	░	  ░   ░		░  ░  ░  
		   ░   ░ ░			░  
			   ░				 		
	
		Make sure your minecraft is open!	
	
	""")
	print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + "\033[1;37;40m| " + Fore.MAGENTA + 'MCS' + Fore.WHITE + ' | ' + Fore.RED +  "\033[1;31;40mCOMMAND:")
	a = input(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + "\033[1;37;40m| " + "\033[0;35;40mMCS \033[1;37;40m| \033[1;31;40m» ")  
	Spam(a)

main()	