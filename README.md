# newspaper-bot

# Description

Script to fetch The Hindu Newspaper pdf daily and send it through mail and discord.

This Program uses : 
- Datatime to get formatted date
- Beautiful Soup to extract pdf link from website
- Smtplib to send mail
- SSL to send secure the mail tunnel
- Discord Webhook to send message to particular channel
- Requests to trigger and send request to webhoook

# Requirements

- python3
- pip3
- requests
- beautifulsoup4
- smtplib
- datetime

# Usage

1. Clone this project `git clone https://github.com/adhirajpandey/newspaper-bot` and cd into it `cd newspaper-bot`
2. Install Requirements `pip install -r requirements.txt`
3. Edit `USER CONFIGURATION` segment in `main.py` file
4. Execute `main.py` and check pdf link in mailbox and discord channel.

