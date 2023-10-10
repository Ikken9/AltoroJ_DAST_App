import requests


def test(url, payload):
    for data in payload:
        url = url + "?query=" + data
        res = requests.get(url=url)
        if data in res.text:
            return 1
    return 0
