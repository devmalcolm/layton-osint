#! /usr/bin/env python3

"""

Layton.py : Find information on a specific user 

SUBMODULE

"""

import time
import os
import requests
import re
import webbrowser as WB
from colorama import Fore, Back, Style

from config import __laytonVersion__
from config import __updateTrue__
from config import __updateFalse__
from config import ErrUpdate
from config import localhost
from config import github_lnk
from config import termsCond
from config import raw_github
from config import __updateTrueErr__


class laytonCheck:
    def __init__(self):
        self.LV = __laytonVersion__
        self.updateTrue = __updateTrue__
        self.updateFalse = __updateFalse__
        self.ErrorHandle = ErrUpdate
        self.github = github_lnk
        self.terms = termsCond
        self.RG = raw_github
        self.updateTrueErr = __updateTrueErr__
        # self.newer_Version = str(re.findall('__laytonVersion__ = "(.*)"', _r.text[0]))

    def terms_conditions(self):
        # print terms & condition of this script
        while True:
            os.system('cls')
            print("""

╦  ╔═╗╦ ╦╔╦╗╔═╗╔╗╔   ╔═╗╦ ╦
║  ╠═╣╚╦╝ ║ ║ ║║║║   ╠═╝╚╦╝
╩═╝╩ ╩ ╩  ╩ ╚═╝╝╚╝ o ╩   ╩ 

Github: @zaqoQLF
            """)
            print(Fore.RED + "{}".format(self.terms) + Style.RESET_ALL)
            print('\n')
            terms_input = input(
                f'[{Fore.GREEN}+{Style.RESET_ALL}] Do you agree with the terms & conditions ? y/n ~# ')
            print('\n')
            if terms_input == 'y':
                L = laytonCheck()
                L.check_versionParser()
                break
            elif terms_input == 'n':
                print("[-] Stopping Program...")
                break
            else:
                time.sleep(2)
                continue

    def check_versionParser(self):
        os.system('cls')
        # checking for newer version of Layton
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] - Retrieving Layton Version Informations...')
        time.sleep(3)
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] - Checking For Layton Updates...')
        time.sleep(3)
        try:
            r = requests.get(
                # Requesting the raw content of the script on github
                "{}".format(self.RG)
            )
            # request the version variable to compare to the local one
            __newerVersion__ = str(re.findall(
                '__laytonVersion__ = "(.*)"', r.text)[0])

            print(__newerVersion__)

            # compare them, if the local version is equal to he github (raw) version, then it will proceed, if not it will ask to update
            __localVersion__ = self.LV

            if __newerVersion__ != __localVersion__:
                # False so update the version of layton
                N = laytonCheck()
                N.update_package(__newerVersion__)
            else:
                # True so proceed
                print(self.updateFalse)
                O = laytonCheck()
                O.proceed_hover()
        # Handle the error
        except Exception as error:
            print(self.ErrorHandle + error)

    def proceed_hover(self):
        os.system('cls')
        print("{}".format(self.updateFalse))
        # sleeping 2 seconds cause im tired
        time.sleep(2)
        os.system('cls')
        print(f"[{Fore.YELLOW}+{Style.RESET_ALL}] Please Wait, Server Is Starting...")
        print(f"[{Fore.YELLOW}+{Style.RESET_ALL}] - Server Status : {Back.YELLOW} STARTING... {Style.RESET_ALL}\n")
        # proceed to app.py to initiate the flask application
        time.sleep(5)
        print("<-------->\n")
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] - Server Status : {Back.GREEN} ONLINE {Style.RESET_ALL}")
        time.sleep(3)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] If the window don't open automatically, open it manually : {Fore.WHITE} {Back.GREEN} http://127.0.0.1:5000/dashboard {Style.RESET_ALL} \n")
        print("<-------->\n")
        # open a new tab with the localhost url
        WB.open_new('{}'.format(localhost))
        # run the app.py file by running this flask command
        time.sleep(2)
        os.system('flask run')
    def update_package(self, __newerVersion__):
        # if the user need to update layton then execute this function
        while True:
            os.system('cls')
            time.sleep(3)
            print(" {} \n\n {}".format(self.updateTrueErr, self.updateTrue))
            print("\n")
            print("Current version : " + self.LV)
            print("Newest version : " + __newerVersion__)
            time.sleep(2)
            print("\n")
            x = input(
                f"[{Fore.GREEN}+{Style.RESET_ALL}] Do you want to get redirected to the github page ? y/n ~# ")
            if x == 'y':
                print("\n")
                print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Redirecting...")
                time.sleep(2)
                WB.open_new('{}'.format(self.github))
                break
            elif x == 'n':
                print("\n")
                print("[-] Stopping Program...")
                time.sleep(2)
                break
            else:
                time.sleep(2)
                continue


if __name__ == "__main__":
    K = laytonCheck()
    K.terms_conditions()
