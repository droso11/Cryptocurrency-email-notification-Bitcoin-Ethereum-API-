import time

from currency import Currency
from mail import send_email
from btc import get_bitcoin_list
from eth import get_ethereum_list

# MAIL PROVIDER CONFIG (SENDER)
SMTP_SERVER = 'smtp.gmail.com'
PORT = 465

# MAIL LOGIN AND PASSWORD (SENDER)
LOGIN = 'drozduuuu@gmail.com'
PASSWORD = 'oC0\'R++5iZDSAmw"^"aP'

RECIPENTS = [
    'metin2x2@gmail.com'
]


currencies = [
                Currency('Bitcoin', 'BTC', 8, 180, get_bitcoin_list),
                        # long_name, short_name, min_percent, minutes to update, function to get list
                Currency('Ethereum', 'ETH', 8, 180, get_ethereum_list),
             ]




time.sleep(300)

while True:
    title = []
    body = []

    for currency in currencies:
        temp_title, temp_body = currency.generate_mail_lists()
        title.extend(temp_title)
        body.extend(temp_body)
        body.append('</br>\n')           # make line between currencies


    if len(title) > 0:
        send_email(SMTP_SERVER, PORT, LOGIN, PASSWORD, RECIPENTS,
                       ' '.join(title),
                       '</br>\n'.join(body)
                       )

    time.sleep(600)
