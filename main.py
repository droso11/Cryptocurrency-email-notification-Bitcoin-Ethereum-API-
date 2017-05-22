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

time.sleep(300)

while True:
    TITLE = ''
    BODY = ''''''

    timenow = datetime.datetime.now()

    try:
        bitcoin_list = get_bitcoin_list()
        ethereum_list = get_ethereum_list()

        percent_bitcoin = ((bitcoin_list[1]-last_send_bitcoin_list[1])/last_send_bitcoin_list[1])\
                          *100.0

        percent_ethereum = ((ethereum_list[1]-last_send_ethereum_list[1])/last_send_ethereum_list[1])\
                           *100.0

    except (TypeError, ValueError):
        if (timenow-last_time_send_mail).seconds//60 >= 90:
            send_email(SMTP_SERVER, PORT, LOGIN, PASSWORD, RECIPENTS,
                       ' '.join([TITLE, '[BTC-ETH] [ERROR] TypeError/ValueError']),
                       'Problem with bitbay.net\nhttps://bitbay.net/'
                       )
            last_time_send_mail = time
            percent_bitcoin = 0.0
            percent_ethereum = 0.0

        time.sleep(300)
        continue

    # BTC
    BODY += 'Bitcoin price: {0} USD [{1:.2f} %]\n'.format(bitcoin_list[1], percent_bitcoin)

    if abs(percent_bitcoin) >= 11.11:
        TITLE += '[BTC: {0:.2f}%]'.format(percent_bitcoin)

    if last_send_bitcoin_list[0] > bitcoin_list[1]:
        TITLE += '[BTC hit lowest 24h]'
        BODY += 'Bitcoin hit the lowest value in 24h\n'

    elif last_send_bitcoin_list[2] < bitcoin_list[1]:
        TITLE += '[BTC hit highest 24h]'
        BODY += 'Bitcoin hit the highest value in 24h\n'


    # ETH
    BODY += '\n\nEthereum price: {0} USD [{1:.2f} %]\n'.format(ethereum_list[1], percent_ethereum)

    if abs(percent_ethereum) >= 11.11:
        TITLE += '[ETH: {0:.2f}%]'.format(percent_ethereum)

    if last_send_ethereum_list[0] > ethereum_list[1]:
        TITLE += '[ETH hit lowest 24h]'
        BODY += 'Ethereum hit the lowest value in 24h\n'

    elif last_send_ethereum_list[2] < ethereum_list[1]:
        TITLE += '[ETH hit highest 24h]'
        BODY += 'Ethereum hit the highest value in 24h\n'

    BODY += '\nhttps://bitbay.net/'

    if(len(TITLE)):
        if 'BTC' in TITLE:
            last_send_bitcoin_list = bitcoin_list

        if 'ETH' in TITLE:
            last_send_ethereum_list = ethereum_list


        send_email(SMTP_SERVER, PORT, LOGIN, PASSWORD, RECIPENTS,
                   TITLE,
                   BODY
                   )

        last_time_send_mail = timenow

    else:
        if (timenow-last_time_send_mail).seconds//60 >= 60:
            TITLE += '[BTC: {0:.2f}%]'.format(percent_bitcoin)
            TITLE += '[ETH: {0:.2f}%]'.format(percent_ethereum)

            send_email(SMTP_SERVER, PORT, LOGIN, PASSWORD, RECIPENTS,
                       TITLE,
                       BODY
                       )

            last_time_send_mail = timenow



    time.sleep(600)