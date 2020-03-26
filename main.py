import requests
from bs4 import BeautifulSoup
import os.path
from os import path
import smtplib , ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

with open('email.json') as email_file:
    credentials = json.load(email_file)
email = credentials['email']
password = credentials['password']
port = int(credentials['port'])
server = credentials['server']
receiver_email = '' #or you can place it with email varibale to send it to you


# get the news page source
source = requests.get("https://www.who.int/news-room/headlines").text

soup = BeautifulSoup(source,'lxml')
# grap the whole first news article content
article = soup.find('div', class_='list-view--item vertical-list-item')
# get head line
headline = article.p.text
# get article date
date = article.span.text
# getting out the link from the a tag with class link-container
link = article.find('a',class_='link-container')['href']
# create the new article full link
full_link = 'https://www.who.int'+link


# new article email function
def send_new_email():
    message = MIMEMultipart("alternative")
    message["Subject"] = "NEW ARTICLE FROM WHO"
    message["From"] = email
    message["To"] = receiver_email
    text = f"check this new article from WHO and be safe\nDate:{date}\n\n " + full_link
    message.attach(MIMEText(text, "plain"))
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(server,port,context=context) as smtp:
        smtp.login(email, password)
        smtp.sendmail(
            email, receiver_email, message.as_string()
        )

# not new article email function
def send_old_email():
    message = MIMEMultipart("alternative")
    message["Subject"] = "BE SAFE AND STAY AT HOME"
    message["From"] = email
    message["To"] = receiver_email
    text = "Hi\n\nThere is no new articles at the moment but please\nbe safe and wash your hands."
    message.attach(MIMEText(text, "plain"))
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(server,port,context=context) as smtp:
        smtp.login(email, password)
        smtp.sendmail(
            email, receiver_email, message.as_string()
        )


# write that article link to a txt file
# check if file exist
def file_exist():
    return(path.exists('article-link.txt'))
#return true if exist and false if not

if file_exist() != True:
    #if file not exist create a new .txt file
        with open('article-link.txt','w+') as file:
            #write the full link
            file.write(full_link)
            # skip chechking and send new email
            send_new_email()

else:
     #function to check the link if its the same link from an earlier article or its a new link
    def check_link():
        with open('article-link.txt','r+') as file :
            #check if the link is old or new
            #new = false
            #old = true  
            pre_link = file.read()
            if full_link == pre_link:
                    
                return True
            else:
                # if its there is a new artcile 
                # replace the old link with the new one 
                file.truncate(0)
                file.seek(0)
                file.write(full_link)
                return False                    
# send email
# if there is a new article

    if check_link() != True:
        send_new_email()
# if there is an old article
    else:
        send_old_email()


