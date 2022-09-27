"""

Layton.py : SUBMODULE

Setup project, installing all different dependencies

"""

import os
import time


def Initialize():
    while True:
        os.system('clear')

        print("""

                 ╦  ╔═╗╦ ╦╔╦╗╔═╗╔╗╔   ╔═╗╦ ╦
                 ║  ╠═╣╚╦╝ ║ ║ ║║║║   ╠═╝╚╦╝
                 ╩═╝╩ ╩ ╩  ╩ ╚═╝╝╚╝ o ╩   ╩ 

                      Github: @zaqoQLF

            [1] - Install Dependencies with PIP3
            [2] - Install Dependencies with PIP

            """)

        __initializeInput__ = int(input("╔═══[setup@Layton]\n╚══ # "))

        if __initializeInput__ == 1:
            print("[MODE - PIP3] - Installing...")
            time.sleep(2)
            Initialize_pip3()
            break
        elif __initializeInput__ == 2:
            print("[MODE - PIP] - Installing...")
            time.sleep(2)
            Initialize_pip()
            break
        else:
            print(
                "[ERROR] - An error occured while selecting the installation mode, please try again.")
            time.sleep(3)
            continue

def Initialize_pip():
    os.system('clear')
    print("Installing...")
    # Installing all modules
    os.system('pip install time')
    os.system('pip install Flask')
    os.system('pip install webbrowser')
    os.system('pip install requests')
    os.system('pip install re')
    os.system('pip install discord_webhook')
    os.system('pip install socket')
    os.system('pip intall colorama')
    os.system('clear')
    print('[+] All modules are installed, please run layton.py file to run the program !')
        
def Initialize_pip3():
    os.system('clear')
    print("Installing...")
    # Installing all modules
    os.system('pip3 install time')
    os.system('pip3 install flask')
    os.system('pip3 install webbrowser')
    os.system('pip3 install requests')
    os.system('pip3 install re')
    os.system('pip3 install discord_webhook')
    os.system('pip3 install socket')
    os.system('pip3 intall colorama')
    os.system('clear')
    print('[+] All modules are installed, please run layton.py file to run the program !')


if __name__ == "__main__":
    Initialize()
