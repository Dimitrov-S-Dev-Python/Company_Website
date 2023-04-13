import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    user = "dimitrov.s.dev@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "dimitrov.s.dev@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user=user, password=password)
        server.sendmail(user, receiver, message)