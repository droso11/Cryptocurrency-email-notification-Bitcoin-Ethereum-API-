from config import SMTP_SERVER, PORT, LOGIN, PASSWORD, RECIPENTS
from mail import send_email
import smtplib

try:
    send_email(SMTP_SERVER, PORT, LOGIN, PASSWORD, RECIPENTS,
                       "Test message",
                       "All working brother!"
                       )
except smtplib.SMTPAuthenticationError:
    print("Can't authenticate user!")