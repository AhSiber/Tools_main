from os import execlp
from colorama import Fore, init
from pyfiglet import figlet_format
from socket import gethostbyname, gethostname
import calendar
from time import time, localtime
import wget 
import requests
from def_init_mine import my_req
from define_font import font
from def_danstny import Danstny
from def_joke import joke
from def_numbers import numberss
from meali import code_meali
from verify_email import verify_email 


# {Knowledge in Persian}
# Developer : Ahura
# git hub : https://github.com/AhSiber

init()  # windows

help_tools = ''' 
# [1] Dispute           [12] craet password 
# [2] Bank              [13] Wikipedia  
# [3] charge            [14] Convert text to Morse code  
# [4] ip                [15] ping site 
# [5] Date              [16] qr code
# [6] time              [17] Character  
# [7] req               [18] True Code Meli 
# [8] font              [19] Download  
# [9] des               [20] Email Verification  
# [10] joke             [21] Developer 
# [11] number 

'''
print(Fore.RED + help_tools)

print(figlet_format('Tools', font="standard"))
print(Fore.GREEN)

user = input('enter Tools : ').lower()
if user == "1":
    try:

        def shop(Overall_profit, Total):
            return F"Overall profit : {Overall_profit - Total}"
        Dispute = input('type Overall_profit : ')
        Dispute2 = input('Enter Total : ')
        print(shop(Dispute, Dispute2))
    except:
        print(Fore.RED + "error tools Dispute ")


elif user == "2":
    try:
        def Facilities(Debt, Percentage, manth):
            return F"Loan interest: {Debt * Percentage * manth * 1 /2400} "
        Debt_input = int(input('Type the loan amount :'))
        Pertage = int(input('Enter the loan percentage : '))
        month_in = int(input('Enter manth : '))
        print(Facilities(Debt_input, Pertage, month_in))
    except:
        print(Fore.RED + "error Tools bank ")


elif user == "3":
    try:

        def charge(Amount, Taxation):
            return f"charge end : {Amount + Taxation}"
        Amounts = int(input('Enter Amount : '))
        Tax_mul = int(input('Enter tax : '))
        print(charge(Amounts, Tax_mul))
    except:
        print(Fore.RED + "error Tools charg")


elif user == "4":
    try:
        name = gethostname()
        by_name = gethostbyname(name)
        print(f"ip address : ", Fore.RED + by_name)
    except:
        print(Fore.RED + "error tools host ")


elif user == "5":
    try:
        user_clender = int(input('Enter Yers : '))
        user_month = int(input('type manth : '))
        new_s_f = calendar.month(user_clender, user_month)
        print(Fore.RED + new_s_f)
    except:
        print(Fore.RED + "error Tools calender ")


elif user == "6":
    try:
        user_time = time()
        my_time = localtime(user_time)
        print(F"{my_time.tm_hour}:{my_time.tm_min}:{my_time.tm_sec}")
    except:
        print(Fore.RED + "error tools time ")

elif user == "7":
    try:
        print(my_req.req())
    except:
        print(Fore.RED + 'error tools req')


elif user == "8":
    try:
        font.font_en()
    except:
        print(Fore.RED + "eror tools font ")


elif user == "9":
    try:
        print(Danstny.dnst())
    except:
        print(Fore.RED + "error tools des ")

elif user == "10":
    try:
        print(joke.jokes())
    except:
        print(Fore.RED + "error tools joke")


elif user == "11":
    try:
        print(numberss.number())
    except:
        print(Fore.RED + "error Tools number ")

elif user == "12" : 
    try:
        user_password = int(input('Enter len password : '))
        name = requests.get(f"http://api.codebazan.ir/password/?length={user_password}").text 
        print(f"password : {Fore.YELLOW + name}") 
    except : 

        print(Fore.RED + "error password") 


elif user == "13" : 
    try: 
        Wikipedia_user= input('search in Wikipedia : ')
        Wikipedia = requests.get(f"https://api.codebazan.ir/wiki/?search={Wikipedia_user}").text
        print(Wikipedia) 
    except:
        print(Fore.RED + "error search Wikipedia") 

elif user == "14" : 
    try : 
        user_mours = input('type value : ')
        lange = str(input('enter lange : '))
        nmours = requests.get(f"https://api.codebazan.ir/mourse/?lang={lange}&text={user_mours}").text
        print(nmours) 
    except:
        print(Fore.RED + "error tools mours")  

elif user == "15" : 
    try : 
        user_ping = input('Enter site : ')
        ping = requests.get(f"https://api.codebazan.ir/ping/?url={user_ping}").text
        print(f"ping site : {Fore.LIGHTBLUE_EX + ping}")

    except : 
        print(Fore.RED + "error tools ping")  



elif user == "16" :
    try: 
        sname = input('Enter Address exs QU : ')
        my = (f"https://api.codebazan.ir/qr/?size=500x500&text={sname}.png") 
        dow = wget.download(my)  
        dow = f'{sname}.png'
        print(dow)
    except : 
        print(Fore.RED + "error tools qrCode ")  

elif user == "17" : 
    try : 

        user_len = input('Enter Character : ')
        print(F"Number of characters : {len(user_len)}" )
    except : 
        print(Fore.RED + "error tools Character ")  

elif user == "18" : 
    try: 
        user_code_maily = int(input('Enter Code meli : '))
        print(code_meali.nano(user_code_maily)) 
    except: 
        print(Fore.RED + "error tools codemali")  

elif user == "19" : 
    try: 
        users_Download = input('Enter linke : ') 
        Dosnm = wget.download(users_Download) 
        print(Dosnm) 
    except:
        print(Fore.RED + "error tools Download ")  


elif user == "20" : 
    try: 
        email = str(input('enter Email : '))
        print(f"your email {verify_email(email)}")
    except: 
        print(Fore.RED + "error tools email ")  


elif user == "21" : 
    new = f''' 
{Fore.LIGHTCYAN_EX}

            (Knowledge in Persian)
            Developer : Ahura
            git hub : https://github.com/AhSiber

    ''' 
    print(new) 

else:   
    print(Fore.RED + "Error input !")

Time_end = time()
my_and_time = localtime(Time_end)
with open("./with.txt", mode='a') as files:
    files.write(
        F"Time_login : {my_and_time.tm_hour}:{my_and_time.tm_min}:{my_and_time.tm_sec} : Tools :  {user} \n")
