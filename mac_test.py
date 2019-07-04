import uuid


def get_mac_address():
    mac_hex = iter(hex(uuid.getnode())[2:].zfill(12))
    mac = ":".join(i + next(mac_hex) for i in mac_hex)
    return mac

if __name__ == '__main__':
    print(get_mac_address())