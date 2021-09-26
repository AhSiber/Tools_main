from os import execlp
from colorama import Fore, init
from pyfiglet import figlet_format
from tkinter import EXCEPTION, font
from socket import gethostbyname, gethostname
import calendar
from time import time, localtime
from def_init_mine import my_req
from define_font import font
from def_danstny import Danstny
from def_joke import joke
from def_numbers import numberss

# {Knowledge in Persian}
# Developer : Ahura
# git hub : https://github.com/AhSiber

init()  # windows

help_tools = ''' 
# [1] Dispute 
# [2] Bank
# [3] charge
# [4] ip
# [5] Date
# [6] time
# [7] req
# [8] font 
# [9] des
# [10] joke 
# [11] Convert numbers from English to Persian  

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


else:
    print(Fore.RED + "Error input !")

Time_end = time()
my_and_time = localtime(Time_end)
with open("./with.txt", mode='a') as files:
    files.write(
        F"Time_login : {my_and_time.tm_hour}:{my_and_time.tm_min}:{my_and_time.tm_sec} : Tools :  {user} \n")
