from flask import Flask, render_template, request
from discord_webhook import DiscordWebhook, DiscordEmbed
import socket
import requests
import os

try:
    os.remove("data_save.txt")
except:
    print("An Error occured")
# Put your webhook url here 
discord_webhookURL = DiscordWebhook("https://raw.githubusercontent.com/zaqoQLF/layton/main/src/layton/config.py?token=GHSAT0AAAAAABYUUJWW5ZFKQ2GEFVRCJ4FMYZSFLLQ")

__data__ = Flask(__name__)

@__data__.route('/dashboard')
def home():
    return render_template('home.html')

@__data__.route('/dashboard/webhook')
def initializeWebhook():
    discord_webhook()
    return render_template('sent-webhook.html')

@__data__.route('/dashboard/lookup')
def searchUser():
    return render_template('lookup.html')

@__data__.route('/dashboard/lookup', methods=['POST'])
def lookup_value():
    username_value = request.form['Username']

    # Website list, feel free to add yours
    Instagam = ['Instagram', f"https://www.instagram.com/{username_value}"]
    Twitter = ['Twitter', f'https://www.twitter.com/{username_value}']
    Youtube = ['Youtube', f'https://www.youtube.com/{username_value}']
    Github = ['Github', f'https://www.github.com/{username_value}']
    Facebook = ['Facebook', f'https://www.facebook.com/{username_value}']
    Roblox = ['Roblox', f'https://www.roblox.com/search/users?keyword={username_value}']
    Paypal = ['Paypal', f'https://www.paypal.com/paypalme/{username_value}']
    Steam = ['Steam', f'https://steamcommunity.com/id/{username_value}']

    # List of all website (might need to add sum but lazy)
    STATUS_POSITIVE_LIST = [
        Instagam, 
        Twitter, 
        Youtube, 
        Github,
        Facebook,
        Roblox,
        Paypal,
        Steam,
        ]

    __count__ = 0
    __matching__ = True

    # Append website that contains the username in it
    # STATUS_REMOVE_FROM_LIST = []

    for i in STATUS_POSITIVE_LIST:
        r = requests.get(i[1])
        if r.status_code == 200:
            if __matching__ == True:
                __matching__ == False
            # print(f"{i[1]} - {r.status_code} - OK")
            if username_value in r.text:
                print("[+] POSITIVE {}".format(i[1]))
                with open("data_save.txt", "a") as f:
                    f.write(f'{i[1]} \n')
            else:
                print("[-] NO MATCH {}".format(i[1]))
                # If username is not in the r.text, so remove it from the list
                STATUS_POSITIVE_LIST.remove(i)
    # Get the total positiv list
    __count__ += 1
    # Get Len of LIST
    total_len = len(STATUS_POSITIVE_LIST)

    # print(STATUS_REMOVE_FROM_LIST)
    return render_template('lookup.html', lenPOS=total_len, LIST=STATUS_POSITIVE_LIST, UsernameText=username_value)

def discord_webhook():
    # Send result by Discord webhook
    
    DC_LIST = []
    NEW_DC_LIST_CLEAR = []
    CLEARPARA = []

    readFile = "data_save.txt"

    rFile = open(readFile, 'r')

    for __txtValue__ in rFile:
        DC_LIST.append(__txtValue__)

    for i in DC_LIST:
        NEW_DC_LIST_CLEAR.append(i.replace("\n" , ""))

    for i in NEW_DC_LIST_CLEAR:
        CLEARPARA.append(i.replace("'", ""))


    print(DC_LIST) 
    print("_____")
    print(NEW_DC_LIST_CLEAR)
    embed = DiscordEmbed(description=f'> {CLEARPARA}', color='1b1b22')
    embed.set_author(name='Layton -  Website List')
    embed.set_footer(text='Layton - Python By Zaqo')
    embed.set_thumbnail(url='https://i.ibb.co/sC4gmcJ/Background-15.png')
    discord_webhookURL.add_embed(embed)
    reponse = discord_webhookURL.execute()  
    rFile.close()
    os.remove("data_save.txt")


