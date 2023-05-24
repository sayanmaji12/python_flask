import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
SMTP_DETAILS = {'smtp_server_address': os.getenv('smtp_server_address'), 'username': os.getenv('username'), 'password': os.getenv('password'), 'enp_type': os.getenv('enp_type'), 'sender': os.getenv('sender'), 'sender_name': os.getenv('sender_name'), 'port_no': os.getenv('port_no')}

class MailSending:
    def __init__(self):
        self.smtpDtl = SMTP_DETAILS

    #send Mail to user
    def sendEmail(self, subject, toaddr, message):
        try:
            
            sender = self.smtpDtl['username']
            passKey = self.smtpDtl['password']
            # instance of MIMEMultipart
            msg = MIMEMultipart()

            # storing the senders email address
            msg['From'] = self.smtpDtl['sender_name'] + " <" + self.smtpDtl['username'] + ">"

            # storing the receivers email address
            msg['To'] = toaddr

            # storing the subject
            msg['Subject'] = subject
            #The body and the attachments for the mail
            msg.attach(MIMEText(message, 'html'))
            #Create SMTP session for sending the mail
            print(self.smtpDtl['port_no'])
            session = smtplib.SMTP_SSL(self.smtpDtl['smtp_server_address'], self.smtpDtl['port_no']) #use gmail with port
            # session.starttls() #enable security
            
            session.login(sender, passKey) #login with mail_id and password
            text = msg.as_string()
            session.sendmail(sender, toaddr, text)
            session.quit()
            print('Mail Sent')
        except Exception as e:
            print(e)