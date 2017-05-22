import requests

def get_json(url):
    response = requests.get(url)
    response.raise_for_status()

    return response.json()
