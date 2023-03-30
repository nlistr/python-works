import requests


def get_infoby_ip(ip):
    url = 'http://ip-api.com/json/{}'.format(ip)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None