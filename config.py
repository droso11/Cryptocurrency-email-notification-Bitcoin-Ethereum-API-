from currencies_api import btc_pln, eth_pln, btc_usd, eth_usd         # IMPORT API !
from currency import Currency

# CONFIGURE THIS

# MAIL PROVIDER CONFIG (SENDER)
SMTP_SERVER = 'smtp.gmail.com'
PORT = 465

# MAIL LOGIN AND PASSWORD (SENDER)
LOGIN = 'USER@mail.com'
PASSWORD = '****passwordhere****'



RECIPENTS = [
    'MAIL_TO@gmail.com'
]


currencies = [
                #Currency('Bitcoin', 'BTC', 'PLN', 8, 180, btc_pln.get_bitcoin_list),         # PLN
                        # long_name, short_name, currency, min_percent, minutes to update, function to get list
                #Currency('Ethereum', 'ETH', 'PLN', 8, 180, eth_pln.get_ethereum_list),       # PLN


                Currency('Bitcoin', 'BTC', 'USD', 8, 0, btc_usd.get_bitcoin_list),         # USD
                # How to:
                # Create Bitcoin cryptocurrency (BTC) from USD (currency), send message if change is more or equal 8%
                # force sending message after 180minutes if nothing was sent in that time


                Currency('Ethereum', 'ETH', 'USD', 8, 0, eth_usd.get_ethereum_list),       # USD
             ]
