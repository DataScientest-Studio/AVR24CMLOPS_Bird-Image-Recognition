import smtplib
from email.mime.text import MIMEText
import os


class AlertSystem:
    def __init__(self):
        self.from_email = os.getenv("ALERT_EMAIL")
        self.password = os.getenv("EMAIL_PASSWORD")
        self.to_email = os.getenv("RECIPIENT_EMAIL")
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 465  # Port pour SSL

    def send_alert(self, subject, message):
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = self.from_email
        msg["To"] = self.to_email

        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.from_email, self.password)
                server.sendmail(self.from_email, self.to_email, msg.as_string())
            return True
        except Exception:
            return False
