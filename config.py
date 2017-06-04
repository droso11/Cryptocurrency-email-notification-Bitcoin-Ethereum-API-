import os

from currencies_api import btc_pln, eth_pln, btc_usd, eth_usd         # IMPORT API !
from currency import Currency

# CONFIGURE THIS
# PATH TO LOG FILE
PATH = os.path.dirname(os.path.abspath(__file__))+'/logs'

ErrorAttemps = 3    # How much time should app try to send the email if encounters error (it waits 10 min)

# MAIL PROVIDER CONFIG (SENDER)
SMTP_SERVER = 'smtp.gmail.com'			# configure this if you don't want gmail!
PORT = 465

# MAIL LOGIN AND PASSWORD (SENDER)
LOGIN = 'mail@gmail.com'
PASSWORD = 'password'

RECIPENTS = [
    'ADDRES_TO_SEND@gmail.com'
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
