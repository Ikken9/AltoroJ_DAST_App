import requests


def test(url, payload):
    res = requests.get(url=url)
    if res.status_code == 200:
        return 1
    else:
        return 0
