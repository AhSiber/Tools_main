from colorama import Fore, init
from pyfiglet import figlet_format
from socket import gethostbyname, gethostname
import calendar
from time import time, localtime
from def_init_mine import my_req
from define_font import font
from def_danstny import Danstny
from def_joke import joke

# {Knowledge in Persian}
# Developer : Ahura
# git hub : https://github.com/AhSiber

init()  # windows

help_tools = ''' 
[+] Dispute 
[+] Bank
[+] charge
[+] ip
[+] Date
[+] time
[+] req
[+] font 
[+] des
[+] joke 
'''
print(Fore.RED + help_tools)

print(figlet_format('Tools', font="standard"))
print(Fore.GREEN)

user = input('enter Tools : ').lower()
if user == "Dispute":
    def shop(Overall_profit=int, Total=int):
        return F"Overall profit : {Overall_profit - Total}"
    Dispute = int(input('type Overall_profit : '))
    Dispute2 = int(input('Enter Total : '))
    print(shop(Dispute, Dispute2))


elif user == "Facilities":
    def Facilities(Debt, Percentage, manth):
        return F"Loan interest: {Debt * Percentage * manth * 1 /2400} "
    Debt_input = int(input('Type the loan amount :'))
    Pertage = int(input('Enter the loan percentage : '))
    month_in = int(input('Enter manth : '))
    print(Facilities(Debt_input, Pertage, month_in))


elif user == "charge":
    def charge(Amount, Taxation):
        return f"charge end : {Amount + Taxation}"
    Amounts = int(input('Enter Amount : '))
    Tax_mul = int(input('Enter tax : '))
    print(charge(Amounts, Tax_mul))

elif user == "ip":
    name = gethostname()
    by_name = gethostbyname(name)
    print(f"ip address : ", Fore.RED + by_name)

elif user == "month":
    user_clender = int(input('Enter Yers : '))
    user_month = int(input('type manth : '))
    new_s_f = calendar.month(user_clender, user_month)
    print(Fore.RED + new_s_f)

elif user == "time":
    user_time = time()
    my_time = localtime(user_time)
    print(F"{my_time.tm_hour}:{my_time.tm_min}:{my_time.tm_sec}")

elif user == "req":
    print(my_req.req())

elif user == "font":
    font.font_en()

elif user == "des":
    print(Danstny.dnst())

elif user == "joke" : 
    print(joke.jokes())
    
else:
    print(Fore.RED + "Error input !")

Time_end = time()
my_and_time = localtime(Time_end)
with open("C:\\Users\\ahoora\\AppData\\Desktop\\Tools_app\\main\\with.txt", mode='a') as files:
    files.write(
        F"Time_login : {my_and_time.tm_hour}:{my_and_time.tm_min}:{my_and_time.tm_sec} : {user} \n")
