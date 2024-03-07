import smtplib
from common.notification_service.templates import generete_email_body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common.config import GMAIL_CONFIG

class Notifications:

    @staticmethod
    def send_email(template_id, email_data, email_metadata):
        gmail_server = GMAIL_CONFIG["gmail_server"]
        gmail_port = GMAIL_CONFIG["gmail_port"]
        gmail_user = GMAIL_CONFIG["gmail_user"]
        gmail_password = GMAIL_CONFIG["gmail_password"]
        email_content = generete_email_body(template_id, email_data)

        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = email_metadata["to"]
        msg['Subject'] = email_metadata["subject"]

        msg.attach(MIMEText(email_content, 'html'))

        with smtplib.SMTP_SSL(gmail_server, gmail_port) as server:
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, email_metadata["to"], msg.as_string())
            
