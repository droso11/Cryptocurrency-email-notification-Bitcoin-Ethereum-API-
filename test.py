from config import SMTP_SERVER, PORT, LOGIN, PASSWORD, RECIPENTS, currencies
from mail import send_email


try:
    currencies[0].get_current_update_percent()

except Exception as e:
    print(str(e))


try:
    send_email(SMTP_SERVER, PORT, LOGIN, PASSWORD, RECIPENTS,
                       "Test message",
                       "All working brother!"
                       )
    print('Sent email!')
except Exception as e:
    print(str(e))