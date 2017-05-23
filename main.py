import time

from currency import Currency
from mail import send_email

from currencies_api import btc_usd, eth_usd         # IMPORT API !

# CONFIGURE THIS

# MAIL PROVIDER CONFIG (SENDER)
SMTP_SERVER = 'smtp.gmail.com'
PORT = 465

# MAIL LOGIN AND PASSWORD (SENDER)
LOGIN = 'MAIL_FROM@gmail.com'
PASSWORD = 'PASSWORD'

RECIPENTS = [
    'MAIL_TO@gmail.com'
]


currencies = [
                #Currency('Bitcoin', 'BTC', 'PLN', 8, 180, btc_pln.get_bitcoin_list),         # PLN
                        # long_name, short_name, currency, min_percent, minutes to update, function to get list
                #Currency('Ethereum', 'ETH', 'PLN', 8, 180, eth_pln.get_ethereum_list),       # PLN


                Currency('Bitcoin', 'BTC', 'USD', 8, 180, btc_usd.get_bitcoin_list),         # USD
                # How to:
                # Create Bitcoin cryptocurrency (BTC) from USD (currency), send message if change is more or equal 8%
                # force sending message after 180minutes if nothing was sent in that time


                Currency('Ethereum', 'ETH', 'USD', 8, 180, eth_usd.get_ethereum_list),       # USD
             ]

# END

#time.sleep(300)

while True:
    title = []
    body = []

    for currency in currencies:
        temp_title, temp_body = currency.generate_mail_lists()
        title.extend(temp_title)
        body.extend(temp_body)
        body.append('</br>\n')           # make line between currencies

    print(title,body)

    if len(title) > 0:
        send_email(SMTP_SERVER, PORT, LOGIN, PASSWORD, RECIPENTS,
                       ' '.join(title),
                       '</br>\n'.join(body)
                       )

    time.sleep(600)
