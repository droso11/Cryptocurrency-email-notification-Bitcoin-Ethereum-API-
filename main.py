import datetime
import time

from mail import send_email
from btc import get_bitcoin_list
from eth import get_ethereum_list

# MAIL PROVIDER CONFIG
SMTP_SERVER = 'smtp.gmail.com'
PORT = 465

# MAIL LOGIN AND PASSWORD
LOGIN = 'drozduuuu@gmail.com'
PASSWORD = 'oC0\'R++5iZDSAmw"^"aP'

RECIPENTS = [
    'metin2x2@gmail.com'
]


last_time_send_mail=datetime.datetime.now()
last_send_bitcoin_list=get_bitcoin_list()
last_send_ethereum_list=get_ethereum_list()

sleep(300)

while True:
    title = []
    body = []

    timenow = datetime.datetime.now()

    try:
        bitcoin_list = get_bitcoin_list()       # Can be ValueError exception
        ethereum_list = get_ethereum_list()     # Can be ValueError exception

        percent_bitcoin = ((bitcoin_list[1]-last_send_bitcoin_list[1])/last_send_bitcoin_list[1])\
                          *100.0

        percent_ethereum = ((ethereum_list[1]-last_send_ethereum_list[1])/last_send_ethereum_list[1])\
                           *100.0

    except (TypeError, ValueError):
        if (timenow-last_time_send_mail).seconds//60 >= 111:
            send_email(SMTP_SERVER, PORT, LOGIN, PASSWORD, RECIPENTS,
                       ' '.join([title, '[BTC-ETH] [ERROR] TypeError/ValueError']),
                       'Problem with bitbay.net\nhttps://bitbay.net/'
                       )
            last_time_send_mail = time
            percent_bitcoin = 0.0
            percent_ethereum = 0.0

        time.sleep(300)
        continue



    body.append('From {} to {}'.format(str(last_time_send_mail.replace(microsecond=0)), str(timenow.replace(microsecond=0))))

    # BTC
    body.append('Bitcoin price: {0} USD [{1:+.2f} %]'.format(bitcoin_list[1], percent_bitcoin))

    BTC = False

    if abs(percent_bitcoin) >= 8:
        title.apend('BTC: {0:+.2f}%'.format(percent_bitcoin))
        BTC = True

    if last_send_bitcoin_list[0] > bitcoin_list[1]:
        title.append('BTC hit lowest 24h')
        body.append('Bitcoin hit the lowest value in 24h')
        BTC = True

    elif last_send_bitcoin_list[2] < bitcoin_list[1]:
        title.append('BTC hit highest 24h')
        body.append('Bitcoin hit the highest value in 24h')
        BTC = True

    # ETH
    body.append('\nEthereum price: {0} USD [{1:+.2f} %]'.format(ethereum_list[1], percent_ethereum))

    ETH = False

    if abs(percent_ethereum) >= 8:
        title.append('ETH: {0:+.2f}%'.format(percent_ethereum))
        ETH = True

    if last_send_ethereum_list[0] > ethereum_list[1]:
        title.append('ETH hit lowest 24h')
        body.append('Ethereum hit the lowest value in 24h')
        ETH = True

    elif last_send_ethereum_list[2] < ethereum_list[1]:
        title.append('ETH hit highest 24h')
        body.append('Ethereum hit the highest value in 24h')
        ETH = True

    body.append('\nhttps://bitbay.net/')

    if len(title):
        if BTC:
            last_send_bitcoin_list = bitcoin_list

        if ETH:
            last_send_ethereum_list = ethereum_list

        send_email(SMTP_SERVER, PORT, LOGIN, PASSWORD, RECIPENTS,
                   ' '.join(title),
                   '\n'.join(body)
                   )

        last_time_send_mail = timenow

    else:
        if (timenow-last_time_send_mail).seconds//60 >= 180:
            title.append('BTC: {0:+.2f}%'.format(percent_bitcoin))
            title.append('ETH: {0:+.2f}%'.format(percent_ethereum))

            send_email(SMTP_SERVER, PORT, LOGIN, PASSWORD, RECIPENTS,
                       ' '.join(title),
                       '\n'.join(body)
                       )

            last_time_send_mail = timenow
            last_send_bitcoin_list = bitcoin_list
            last_send_ethereum_list = ethereum_list


    time.sleep(600)
