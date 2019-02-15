import smtplib
import ssl

USERNAME = '71c223345a89f9b8f3eecb365d0530b0'
PASSWORD = '19f96d36a3edbe126c5d0f2fe8e02aa6'


class EmailHandler(object):
    """Email sender"""
    def __init__(self, port=465, smtp_server='in-v3.mailjet.com', sender_email="pavlukhinm@gmail.com"):
        self.port = port
        self.smtp_server = smtp_server
        self.sender_email = sender_email
        self.username = USERNAME
        self.password = PASSWORD

    def send_email(self, receiver_email, message):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.username, self.password)
            server.sendmail(self.sender_email, receiver_email, message)
