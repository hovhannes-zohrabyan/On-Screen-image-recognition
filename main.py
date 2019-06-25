import MainController
import requests


def run(userId):
    url = get_url_config()
    userId = 'sunny'
    mac_address = '00:0C:29:21:5C:D9'
    params = {'userid': userId, 'mac_address': mac_address}
    r = requests.get(url=url, params=params)
    json = r.json()

    MainController.action_controller(json)


def get_url_config():
    f = open("API_Config.txt", "r")
    if f.mode == 'r':
        url = f.read()
        return url
