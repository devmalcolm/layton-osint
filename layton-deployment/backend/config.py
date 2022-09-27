import os
import time
from colorama import Fore, Style, Back

# version of layton (to compare to the built-in one)
__laytonVersion__ = "0.0.2"

# message for update
__updateTrueErr__ = f"[{Fore.RED}-{Style.RESET_ALL}] {Fore.WHITE}{Back.RED} INVALID VERSION OF LAYTON {Style.RESET_ALL}"

__updateTrue__ = f" \r\r [{Fore.RED}!{Style.RESET_ALL}] Please update the latest version of layton !"

# message for update
__updateFalse__ = f"[{Fore.GREEN}+{Style.RESET_ALL}] Layton has been successfully updated !"

# error update message
ErrUpdate = "A problem occurred while checking for an update"

# github package link
github_lnk = "https://github.com/zaqoQLF/layton-osint"

# localhost / server link 
localhost = 'http://127.0.0.1:5000/dashboard'

# Github Raw Version of the config file (To compare version)
raw_github = "https://raw.githubusercontent.com/zaqoQLF/layton-osint/master/layton-deployment/backend/config.py?token=GHSAT0AAAAAABYUUJWXNHJJP4HD5KP2O5XOYZTRLEQ"

termsCond = """

I remind you that this script is for educational purposes only, please run this script on consenting people

By continuing, you agree to the terms above.
"""
