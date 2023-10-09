import requests


def test(url, payload):
    res = requests.get(url=url)
    if payload in res.text:
        return 1
    else:
        return 0
