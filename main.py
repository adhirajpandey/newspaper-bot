#USER CONFIGURABLE VARIABLES

gmail_id = "[your_gmail_id]"
gmail_pass = "[your_gmail_password]"
mailing_list = ["pandey.adhiraj02@gmail.com", "add_more_here@xyz.com"]
webhook_url = "add your discord webhook url here"  

#Example of discord webhook url : https://discord.com/api/webhooks/1234567890/abcdefghijklmnopqrstuvwxyz


#IMPORTING LIBRARIRES

import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import date as dt
import smtplib
import ssl


#DEFINING FUNCTIONS

#funtion to get the html content of the page using requests and bs module
def scrape(url):
    URL = link
    #defining headers
    header ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

    #getting page using requests module
    page = requests.get(URL, headers=header)

    #getting html content with proper formatting using BeautifulSoup
    soup1 = BeautifulSoup(page.content, "html.parser")

    return soup1

#funtion to transform link for the specified date
def transform_link(date):
    link = "https://www.gkgsca.com/2022/11/the-hindu-pdf-" + date + "-free.html#AT-downloadPop"
    return link

#funtion to mail the link
def send_mail():
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = gmail_id
        receiver_email = mailing_list
        password = gmail_pass      
        FROM = f"Adhiraj's Bot"
        SUBJECT = f"{fdate} : The Hindu Newspaper PDF"
        TEXT = f"""
Hey User,

Please check the below link for The Hindu Newspaper for {fdate}.

{gdrive_link}

Prepare Well and Have a nice day.

Regards,
Adhiraj's Bot"""
        
        message = 'From: {}\nSubject: {}\n\n{}'.format(FROM,SUBJECT, TEXT)
        

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

#send discord message
def send_discord_message():
    discord_webhook_url = webhook_url
    Message = {
        "content": f"Google Drive Link for The Hindu Newspaper for {fdate} : \n{gdrive_link}"
    }
    requests.post(discord_webhook_url, data=Message)


#OPERATOR CODE

#get today's date in two formats (date = 10-october-2022 and fdate = 10-10-2022)
date = date.today().strftime("%d-%B-%Y").lower()
fdate = dt.today().strftime("%d-%m-%Y")

#transform link for today's date
link = transform_link(date)

#scrape the page
a = (scrape(link))

#find the download link
gdrive_link = a.find("a", class_="button").get('href')

#send mail with the link
send_mail()

#send discord message with the link
send_discord_message()


