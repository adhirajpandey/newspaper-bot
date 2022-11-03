# newspaper-bot

# Description

Script to fetch The Hindu Newspaper pdf daily and send it through mail and discord.

This Program uses : 
- Datetime to get formatted date
- Beautiful Soup to extract pdf link from website
- Smtplib to send mail
- SSL to secure the mail tunnel
- Discord Webhook to send message to particular channel
- Requests to trigger and send message request through webhoook

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

# Sample Demonstration

- Clone and Install Requirements

  ![installation](https://user-images.githubusercontent.com/87516052/199808153-97565f6e-9700-4f88-b42b-323577a7f3a7.png)
  
  
- Edit Configuration Segemnent and Run main.py

  ![run](https://user-images.githubusercontent.com/87516052/199808915-4b7f41d8-8abd-492c-a11e-fe6a6c29a853.png)
  
  
- Output Sample : Discord Message and Email

  ![discord_message](https://user-images.githubusercontent.com/87516052/199809121-3523aa25-ea64-4730-aef7-0dc8c09b1c5d.png)
  
  ![mail](https://user-images.githubusercontent.com/87516052/199809155-8d951de9-a24a-48f8-826c-87e27f00b4bf.png)
