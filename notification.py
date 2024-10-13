import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
load_dotenv()


class Notification:
    def __init__(self):
        self.email_address = os.getenv('MY_EMAIL')
        self.password = os.getenv('EMAIL_PASSWORD')
        self.SMTP = os.getenv('SMTP_ADDRESS')
        self.port = 587


    def email(self, body):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = self.email_address
            msg['Subject'] = 'Low price Alert!!'

            # Attach the email body with proper encoding
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
            with smtplib.SMTP(self.SMTP, self.port) as connection:
                connection.starttls()
                connection.login(user=self.email_address, password=self.password)
                connection.sendmail(from_addr=self.email_address, to_addrs=self.email_address, msg=msg.as_string())
            print('Email sent successfully')
        except (smtplib.SMTPException, smtplib.SMTPAuthenticationError) as error:
            print(f'Authentication failed: {error}')