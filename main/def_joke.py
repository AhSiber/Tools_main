import requests 

# {Knowledge in Persian}
# Developer : Ahura 
# git hub : https://github.com/AhSiber 

class joke : 

    def __init__(self) -> None:
        pass

    def jokes(): 
        name = requests.get("http://api.codebazan.ir/jok/").text 
        return name 


