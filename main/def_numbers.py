import requests 
import colorama 

colorama.init() 

class numberss : 
    def __init__(self): 
        pass

    def number(): 
        user = int(input('Enter number : '))
        name = requests.get(f"https://api.codebazan.ir/adad/?text={user}").json()
        fa = name["result"]["fa"]
        fatext = name["result"]["fatext"]
        print(colorama.Fore.GREEN + "~~~~~~~~~~~~~~~~~~~~")
        return f"Fa : {fa}\ntext : {fatext}" 

