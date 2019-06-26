import MainController
import requests
import uuid

from getmac import get_mac_address



def run(userId):
    # url = get_url_config()
    mac_address = get_mac_address(interface="eth0")
    print(mac_address)
    mac_address = '00:0C:29:21:5C:D9'
    params = {'userid': userId, 'mac_address': mac_address}
    r = requests.get(url='https://erp.suffescom.com/modules/access/api', params=params)
    json = r.json()

    try:
        result = MainController.action_controller(json)
        return result
    except Exception as _:
        return "Something Gone Wrong!"


def get_url_config():
    f = open("API_Config.txt", "r")
    if f.mode == 'r':
        url = f.read()
        return url


# def get_mac_address():
#     mac_hex = iter(hex(uuid.getnode())[2:].zfill(12))
#     mac = ":".join(i + next(mac_hex) for i in mac_hex)
#     return mac
