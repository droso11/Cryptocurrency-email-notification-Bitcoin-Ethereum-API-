# https://bitbay.net/API/Public/ETHUSD/ticker.json
'''

@json return:
max
min
last
bid
ask
vwmap
average
volume
'''

from request_helper import get_json

def get_bitcoin_price():
    json_dictionary = get_json('https://bitbay.net/API/Public/BTCPLN/ticker.json')

    return json_dictionary.get('last', None)


def get_bitcoin_list():
    # return [min price within 24h, last, max price within 24h]
    json_dictionary = get_json('https://bitbay.net/API/Public/BTCPLN/ticker.json')

    return [json_dictionary.get('min', None),json_dictionary.get('last', None),json_dictionary.get('max', None)]

