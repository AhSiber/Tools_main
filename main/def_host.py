from colorama.initialise import init
import requests
import colorama

init()

class host:

    def __init__(self) -> None:
        pass

    def who():
        user = input('Enter host : ')
        name = requests.get(
            f"https://api.codebazan.ir/whois/index.php?type=json&domain={user}").json()
        ip = name['ip']
        address = name['address']
        dns = name['dns']["1"]

        return f"IP : {ip} \nadress : {address} \ndns : {dns}"

