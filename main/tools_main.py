
from colorama import Fore, init
import gtts
from pyfiglet import figlet_format
from socket import gethostbyname, gethostname
import calendar
from time import time, localtime
from pytube.__main__ import YouTube
import wget
import requests
from def_init_mine import my_req
from define_font import font
from def_danstny import Danstny
from def_joke import joke
from def_numbers import numberss
from meali import *
from verify_email import verify_email
from random import randrange
from tkinter import * 
import tkinter.messagebox
from os import system 


# {Knowledge in Persian}
# Developer : Ahura
# git hub : https://github.com/AhSiber

init()  # windows

help_tools = ''' 
# [1] Dispute           [12] craet password                 [24] DDos 
# [2] Bank              [13] Wikipedia  
# [3] charge            [14] Convert text to Morse code  
# [4] ip                [15] ping site 
# [5] Date              [16] qr code
# [6] time              [17] Character  
# [7] req               [18] True Code Meli 
# [8] font              [19] Download  
# [9] des               [20] Email Verification  
# [10] joke             [21] Developer (GUL)
# [11] number           [22] voice 
                        [23] calculator (GUL)

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

elif user == "12":
    try:
        user_password = int(input('Enter len password : '))
        name = requests.get(
            f"http://api.codebazan.ir/password/?length={user_password}").text
        print(f"password : {Fore.YELLOW + name}")
    except:

        print(Fore.RED + "error password")


elif user == "13":
    try:
        Wikipedia_user = input('search in Wikipedia : ')
        Wikipedia = requests.get(
            f"https://api.codebazan.ir/wiki/?search={Wikipedia_user}").text
        print(Wikipedia)
    except:
        print(Fore.RED + "error search Wikipedia")

elif user == "14":
    try:
        user_mours = input('type value : ')
        lange = str(input('enter lange : '))
        nmours = requests.get(
            f"https://api.codebazan.ir/mourse/?lang={lange}&text={user_mours}").text
        print(nmours)
    except:
        print(Fore.RED + "error tools mours")

elif user == "15":
    try:
        user_ping = input('Enter site : ')
        ping = requests.get(
            f"https://api.codebazan.ir/ping/?url={user_ping}").text
        print(f"ping site : {Fore.LIGHTBLUE_EX + ping}")

    except:
        print(Fore.RED + "error tools ping")


elif user == "16":
    try:
        sname = input('Enter Address exs QU : ')
        my = (f"https://api.codebazan.ir/qr/?size=500x500&text={sname}.png")
        dow = wget.download(my)
        dow = f'{sname}.png'
        print(dow)
    except:
        print(Fore.RED + "error tools qrCode ")

elif user == "17":
    try:

        user_len = input('Enter Character : ')
        print(F"Number of characters : {len(user_len)}")
    except:
        print(Fore.RED + "error tools Character ")

elif user == "18":
    try:
        user_code_maily = input('Enter Code meli : ')
        print(code_meali.mali(user_code_maily))
    except:
        print(Fore.RED + "error tools codemali")

elif user == "19":
    try:
        users_Download = input('Enter linke : ')
        Dosnm = wget.download(users_Download)
        print(Dosnm)
    except:
        print(Fore.RED + "error tools Download ")


elif user == "20":
    try:
        email = str(input('enter Email : '))
        print(f"your email {verify_email(email)}")
    except:
        print(Fore.RED + "error tools email ")


elif user == "21":
    num = Tk()
    num.title("Developer")
    num.geometry("300x200")
    num.resizable(width=False, height=False)
    num.configure(bg="#F5F6FA")

    new_lab = Label(num, text="(Knowledge in Persian)")
    new_lab.place(x=40, y=40)

    Developer = Label(num, text="Developer : Ahura")
    Developer.place(x=40, y=60)

    github = Label(num, text="git hub : https://github.com/AhSiber")
    github.place(x=40, y=80)

    new = f''' 
    {Fore.LIGHTCYAN_EX}

            (Knowledge in Persian)
            Developer : Ahura
            git hub : https://github.com/AhSiber

    '''
    print(new)

    num.mainloop()

elif user == "22":
    try:
        user_mp3 = str(input('Enter string : '))
        tts = gtts.gTTS(user_mp3)
        name_mp3 = str(randrange(1, 10000))
        tts.save(f"{name_mp3}.mp3")

    except:
        print(Fore.RED + "error tools voice ")
 
# ============================================== Gul ================================ 

elif user == "23" : 
    root = Tk()
    root.geometry("200x200")
    root.title('claucar')
    root.resizable(width=False, height=False)
    color = "#DFE4EA"
    root.configure(bg=color)

    num1 = StringVar() 
    num2 = StringVar() 
    my = StringVar()


    # Frames ---------------------------------------

    top1 = Frame(root , width=1 , height=200 , bg=color) 
    top1.pack(side="top") 

    top2 = Frame(root , width=200 , height=200 , bg=color) 
    top2.pack(side="top")  

    top3 = Frame(root , width=200 , height=200 , bg=color) 
    top3.pack(side="top") 

    top4 = Frame(root , width=200 , height=200 , bg=color) 
    top4.pack(side="top" ) 

    # funcashan ---------------------------------------


    def msgbox(msi) :
        if msi == "error": 
            tkinter.messagebox.showerror('ERROR' , 'Error inputs To clucter') 


    def game() : 
        try:    
            number = float(num1.get()) + float(num2.get())
            my.set(number) 
        except: 
            msgbox('error')


    def tg() : 
        try : 
            ts = float(num1.get()) /  float(num2.get()) 
            my.set(ts) 
        except : 
            msgbox('error')


    def zrb() : 
        try : 
            t = float(num1.get()) *  float(num2.get()) 
            my.set(t) 
        except : 
            msgbox('error')



    def mn() : 
        if num2.get() == "0" :
            KeyError('error')
        try : 
            m = float(num1.get()) - float(num2.get()) 
            my.set(m) 
        except :
            msgbox('error')

        
    

    # Buttons ---------------------------------------

    but1 = Button(top2 , text="+" , width=4 , height=2 , command= lambda : game()) 
    but1.pack(side="left" , padx=2 , pady=2)

    but2 = Button(top2 , text="/", width=4 , height=2 , command= lambda : tg()) 
    but2.pack(side="left" , padx=2 , pady=2)

    but3 = Button(top2 , text="*", width=4 , height=2 , command = lambda : zrb()) 
    but3.pack(side="left" , padx=2 , pady=2)

    but4 = Button(top2 , text="-", width=4 , height=2 , command= lambda : mn()) 
    but4.pack(side="left" , padx=2 , pady=1)

    # Entrys end labls  ---------------------------------------

    lb1 = Label(top1 , text="Enter numbers :") 
    lb1.pack(side="top" , padx=1 , pady=1) 
    en = Entry(top1 , background="WHITE" , textvariable=num1)
    en.pack(side="top" , padx=2 , pady=2) 


    lb2 = Label(top1 , text=" raulat end :") 
    lb2.pack(side="top" , padx=1 , pady=1) 
    en2 = Entry(top1 , background="WHITE" , textvariable=num2)
    en2.pack(side="top" , padx=2 , pady=2) 



    en2 = Entry(top3 , background="#ECF0F1" , textvariable=my)
    en2.pack(side="bottom" , padx=4 , pady=5) 


    lb2 = Label(top3 , text=" end in numbers :") 
    lb2.pack(side="bottom" , padx=1 , pady=1) 


    root.mainloop()

# ================================================ The End Gul ====================================

elif user == "24" : 
    try : 
        en_link_addres = input('Enter linke site : ')
        new_my = system(f"ping {en_link_addres}") 
    except : 
        print(Fore.RED + "error tools DDos ") 

else : 
    print(Fore.RED + "Error input !")



Time_end = time()
my_and_time = localtime(Time_end)
with open("./with.txt", mode='a') as files:
    files.write(
        F"Time_login : {my_and_time.tm_hour}:{my_and_time.tm_min}:{my_and_time.tm_sec} : Tools :  {user} \n")

