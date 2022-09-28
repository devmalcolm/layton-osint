
![Logo](https://i.ibb.co/716shyn/16-Fc-JJ-Shape-2-1.png)

<h1 align="center">LAYTON.PY</h1>

<div align="center">
  <strong>Lookup information software, open-source project made with Python3 - Flask</strong>
  <br>
  <br>

  <a href="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Travis" />
  </a>
  
  <a href="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white">
    <img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" alt="Documentation Status" />
  </a>

  <a href="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="Py Versions" />
  </a>

  <a href="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="PyPi" />
  </a>

  <a href="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="LICENSE" />
  </a>

  <a href="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="LICENSE" />
  </a>

</div>
<br>

Open-source project to easily find information about a specific user (Social Media Hunt) made with Python3, Flask(HTML5, CSS3)

Please use this program only on consenting people, I remind you that it is only for educational purposes and that I am not responsible for your actions

<br>


`Table of contents :` <br><br>
⚙️ · [Installation](#-installation)
<br>
🚀 · [Running](#-running-program)
<br>
🪝 · [Discord Webhook](#-discord-webhook)
<br>
📸 · [Screenshot](#-screenshot-program)
<br>
🖋 · [Author](#-author)
<br>
🌐 · [Dashboard Links](#-dashboard-links)
<br>
👨‍💻 · [Supported Website](#-supported-website)



<br>

<div align="center">
    <strong>If you want to support me and the project, put a star on it, thanks ❤️</strong>
</div>



## 🛠 Installation


![Logo](https://i.ibb.co/kcJVSSs/Shape-2-7.png)

Important, you should have the version 3.x of Python installed

**There's few ways to install dependencies, here a few of them :**

- Clone this repository
```sh
git clone https://github.com/zaqoQLF/layton-osint.git
```

- Install the requirements
```sh
pip3 install -r requirements.txt
```

*You can also run this file, it will automatically install all dependencies :*
```sh
python3 setup.py
```
*Or you can install all dependencies manually :*
```sh
pip install os
pip install time
pip install flask
pip install requests
pip install re
pip install webbrowser
pip install discord_webhook
```

## 🚀 Running Program

![Logo](https://i.ibb.co/q0q3k35/161v6-Y-Shape-2-4.png)


Once all dependencies installed, you can run the program !

This program works with flask, it means that the main panel will be a dashboard hosted on your localhost (http://127.0.0.1:5000/)

Once `layton.py` executed, it will check for updates and if all is good your going to self-host the program on your localhost.

To access it, just wait after the `layton.py` script, then it will automatically open the webpage for you

*Here a little screenshot of it [click](https://www.google.com) here to view*

<br>

- Run `layton.py`
```
python3 layton.py
```

## 🌐 Dashboard Links
Here is all links of the dashboard (Layton Dashboard)

This program will mainly run locally but you can host it for free with heroku or other VPS

Main Dashboard (home)
- https://127.0.0.1:5000/dashboard

Lookup information panel
- https://127.0.0.1:5000/dashboard/lookup

Sending Discord webhook panel
- https://127.0.0.1:5000/dashboard/webhook

## 👨‍💻 Supported Website

Here is the list of all the website already setup

- [Layton Website List](https://github.com/zaqoQLF/layton/blob/main/site.md)

**How can i add website ?**
  - Its simple, go to the `app.py` file, once done search for the function `def lookup_value`, and add a website, example :
  ```py
  ...
  Instagram = ['Instagram', 'https://www.instagram.com/{username_value}']
  
  # Add your website list here
  
  ExampleWebsite = ['Name Of The Website', 'Link of the website + add {username_value} at the end']
  
  # Once done, add your website to the list
  
  STATUS_POSITIVE_LIST = [
  ...
  ExampleWebsite,
  ]
  ```



## 🪝 Discord Webhook

![LOGO](https://i.ibb.co/61TnrVC/162f-RT-Shape-2-5.png)

With this script you got the possibility to export your result into `.txt` file and into `Discord Webhook` (Discord embed)

For this you need to setup your own webhook.

- **How to get my webhook URL ?**
Here a quick tutorial on how to get your webhook URL (don't share the link to avoid spam)

Tutorial link : [Watch](https://www.youtube.com/watch?v=K8vgRWZnSZw&ab_channel=ThomasBnt)

**Export System Status :**

- [x] Discord Webhook
- [ ] Txt File


Setup your own Discord webhook URL
- Go to `app.py` at the top of the script, there is a variable called `discord_webhookURL`, change it with your own url
```py
discord_webhookURL = DiscordWebhook(" Your Discord Webhook URL")
```

![Screen](https://i.ibb.co/rbRN2bZ/w2i312.png)

## 🕺🏻 Screenshot Program

![Logo](https://i.ibb.co/s64Dnxj/Shape-2-8.png)

- Here a few screenshot / preview of the Dashboard / Lookup Panel 
(Reminder, that's a open-source project, if you want to clone it and modify it you can !)

- Webhook Panel

![Screen](https://i.ibb.co/HqswD3S/webhook-Dashboard.png)

- Home Dashboard

![Screen](https://i.ibb.co/wSfBZv4/dashboard.png)

- Lookup Panel

![Screen](https://i.ibb.co/C0hC8XL/lookup-Dash.png)


## 🖋 Author

![Logo](https://i.ibb.co/WsJc30f/Shape-2-6.png)

<div align="center">
    <strong><a href="https://www.github.com/zaqoQLF">@zaqoQLF</a></strong>
    <br>
    Follow me if you want to support my project ❤️
</div>



