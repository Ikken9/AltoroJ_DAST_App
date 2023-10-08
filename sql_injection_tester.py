import requests


def test(url, payload):
    for _ in payload:
        res = requests.post(url=url, data=payload)
        if res.status_code == 200:
            return 1
    return 0
