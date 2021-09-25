import requests 

# {Knowledge in Persian}
# Developer : Ahura 
# git hub : https://github.com/AhSiber 

class Danstny  : 

    def __init__(self) -> None:
        pass 

    def dnst() : 
        name = requests.get('https://api.codebazan.ir/danestani/').text 
        return name 


print(Danstny.dnst())
