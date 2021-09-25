import requests 

# {Knowledge in Persian}
# Developer : Ahura 
# git hub : https://github.com/AhSiber 

class my_req : 
    def __init__(self): 
        pass

    def req():
        Date = requests.get("https://api.codebazan.ir/time-date/?json=en").json()
        Time =  Date['result']['time']
        date = Date['result']['date'] 
        fasl = Date['result']['fasl']
        return f'time iran : {Time} \nDate iran : {date} \nfasl : {fasl}' 