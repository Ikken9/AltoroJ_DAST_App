import requests
import json


def test_api(url, payload):
    for data in payload:
        body = {"username": data.replace("\n", ""), "password": "PASSWORD_PLACEHOLDER"}
        headers = {
            "Content-Type": "application/json"
        }
        json_data = json.dumps(body)
        res = requests.post(url=url, data=json_data, headers=headers)
        if res.status_code == 200:
            return 1
    return 0


def test_ui(url, payload):
    for data in payload:
        url = url + "?uid=" + data + "&passw=PASSWORD_PLACEHOLDER"
        expected_response = ("Login Failed: We're sorry, but this username or password was not found in our system. "
                             "Please try again.")
        res = requests.post(url=url)
        if expected_response in res.text:
            return 0
    return 1
