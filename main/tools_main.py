import os
import pstats
# color in python 'colorama' Func in Windows 'init' !
from colorama import Fore, init
import gtts  # voice in python
# from pyfiglet import figlet_format # pyfiglet in python 'Tools'
from socket import gethostbyname, gethostname  # ip in socket '127.0.0.1'
import calendar  # calend in python '2021' , '4' , '23'
from time import time, localtime  # time 12 : 00
import wget  # dowanload in python link
import requests  # request api
from def_init_mine import my_req  # funck my_req
from define_font import font  # funck font
from def_danstny import Danstny  # funck danstny
from def_joke import joke  # funck joke
from def_numbers import numberss  # funck number
from meali import *  # funck True code malit
from verify_email import verify_email  # verfiy Eamil
from random import randrange  # random number
from tkinter import *  # GUL
import tkinter.messagebox  # GUL hanel Error
from os import system  # os madouls in system
from cryptography.fernet import Fernet  # Encode end decrypt
import platform
import sys
from pytube import YouTube

# clear system !
os.system("clear")

# {Knowledge in Persian}
# Developer : Ahura
# git hub : https://github.com/AhSiber

if sys.platform == "Linux":
    pass
else:
    init()  # windows

help_tools = ''' 
# [1] Dispute           [12] craet password                 [24] DDos
# [2] Bank              [13] Wikipedia                      [25] NootBok (GUL)
# [3] charge            [14] Convert text to Morse code     [26] encode 
# [4] ip                [15] ping site                      [27] decode 
# [5] Date              [16] qr code                        [28] Continue...
# [6] time              [17] Character  
# [7] req               [18] True Code Meli 
# [8] font              [19] Download  
# [9] des               [20] Email Verification  
# [10] joke             [21] Developer (GUL)
# [11] number           [22] voice 
                        [23] calculator (GUL)

'''
print(Fore.RED + help_tools)  # color

# print(figlet_format('Tools', font="standard")) # Figlet format 'Tools'
# print(Fore.GREEN) # color green
os.system("figlet Tools ")


user = input('enter Tools : ').lower()  # input "lower" -- user
if user == "1":
    try:
        def shop(Overall_profit, Total):  # defin inputs (Overall_profit) and (Total)
            return F"Overall profit : {Overall_profit - Total}"
        Dispute = input('type Overall_profit : ')
        Dispute2 = input('Enter Total : ')
        print(shop(Dispute, Dispute2))  # print (Overall_profit) and (Total)
    except:
        print(Fore.RED + "error tools Dispute ")  # Handel Error


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
        name = gethostname()  # get name host
        by_name = gethostbyname(name)  # get host by name
        os.system("clear")
        print(f"ip address : ", Fore.RED + by_name)  # red ip 127.0.0.1
    except:
        print(Fore.RED + "error tools host ")  # handel Error


elif user == "5":
    try:
        user_clender = int(input('Enter Yers : '))
        user_month = int(input('type manth : '))
        new_s_f = calendar.month(user_clender, user_month)  # clander 2021
        os.system("clear")
        print(Fore.RED + new_s_f)  # color red
    except:
        print(Fore.RED + "error Tools calender ")  # handel error


elif user == "6":
    try:
        user_time = time()  # time [272.9293827382]
        # local time tm_hour or tm_main or tm_sec
        my_time = localtime(user_time)
        os.system("clear")
        print(F"{my_time.tm_hour}:{my_time.tm_min}:{my_time.tm_sec}")
    except:
        print(Fore.RED + "error tools time ")  # handel Error

elif user == "7":
    try:
        os.system('clear')
        print(my_req.req())  # req
    except:
        print(Fore.RED + 'error tools req')  # handel eror


elif user == "8":
    try:
        os.system("clear")
        font.font_en()  # font =>  60
    except:
        print(Fore.RED + "eror tools font ")  # handel Error


elif user == "9":
    try:
        os.system("clear")
        print(Danstny.dnst())  # danstny funck == 5000 ==
    except:
        print(Fore.RED + "error tools des ")  # handel Error

elif user == "10":
    try:
        os.system('clear')
        print(joke.jokes())  # jocke == 7000 ===
    except:
        print(Fore.RED + "error tools joke")


elif user == "11":
    try:
        print(numberss.number())  # exchange number in str
    except:
        print(Fore.RED + "error Tools number ")  # handel error

elif user == "12":
    try:
        user_password = int(input('Enter len password : ')
                            )  # input len password
        name = requests.get(
            f"http://api.codebazan.ir/password/?length={user_password}").text  # api Create password
        os.system("clear")
        print(f"password : {Fore.YELLOW + name}")
    except:

        print(Fore.RED + "error password")


elif user == "13":
    try:
        Wikipedia_user = input('search in Wikipedia : ')  # input serach
        Wikipedia = requests.get(
            f"https://api.codebazan.ir/wiki/?search={Wikipedia_user}").text  # api seach in wikipadia
        os.system("clear")
        print(Wikipedia)
    except:
        print(Fore.RED + "error search Wikipedia")

elif user == "14":
    try:
        user_mours = input('type value : ')  # str
        lange = str(input('enter lange : '))  # lange
        nmours = requests.get(
            f"https://api.codebazan.ir/mourse/?lang={lange}&text={user_mours}").text  # mours
        print(nmours)
    except:
        print(Fore.RED + "error tools mours")

elif user == "15":
    try:
        user_ping = input('Enter site : ')  # input site
        ping = requests.get(
            f"https://api.codebazan.ir/ping/?url={user_ping}").text  # ping site
        os.system("clear")
        print(f"ping site : {Fore.LIGHTBLUE_EX + ping}")

    except:
        print(Fore.RED + "error tools ping")


elif user == "16":
    try:
        sname = input('Enter Address exs QR : ')  # iter code in QR code
        # api code RQ
        my = (f"https://api.codebazan.ir/qr/?size=500x500&text={sname}.png")
        dow = wget.download(my)  # download QR
        dow = f'{sname}.png'  # format '.png'
        print(dow)
    except:
        print(Fore.RED + "error tools qrCode ")  # handel Error

elif user == "17":
    try:
        # enter charchter === name == len(4)
        user_len = input('Enter Character : ')
        os.system("clear")
        print(F"Number of characters : {len(user_len)}")
    except:
        print(Fore.RED + "error tools Character ")

elif user == "18":
    try:
        user_code_maily = input('Enter Code meli : ')
        print(code_meali.mali(user_code_maily))  # funck code True end False
    except:
        print(Fore.RED + "error tools codemali")

elif user == "19":
    try:
        users_Download = input('Enter linke : ')  # enter linke
        Dosnm = wget.download(users_Download)  # download linke inputy !
        os.system("clear")
        print(Dosnm)
    except:
        print(Fore.RED + "error tools Download ")


elif user == "20":
    try:
        email = str(input('enter Email : '))  # Enter email
        os.system("clear")
        print(f"your email {verify_email(email)}")  # verfiy Emalit
    except:
        print(Fore.RED + "error tools email ")


elif user == "21":  # Developer
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

elif user == "23":
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

    top1 = Frame(root, width=1, height=200, bg=color)
    top1.pack(side="top")

    top2 = Frame(root, width=200, height=200, bg=color)
    top2.pack(side="top")

    top3 = Frame(root, width=200, height=200, bg=color)
    top3.pack(side="top")

    top4 = Frame(root, width=200, height=200, bg=color)
    top4.pack(side="top")

    # funcashan ---------------------------------------

    def msgbox(msi):
        if msi == "error":
            tkinter.messagebox.showerror('ERROR', 'Error inputs To clucter')

    def game():
        try:
            number = float(num1.get()) + float(num2.get())
            my.set(number)
        except:
            msgbox('error')

    def tg():
        try:
            ts = float(num1.get()) / float(num2.get())
            my.set(ts)
        except:
            msgbox('error')

    def zrb():
        try:
            t = float(num1.get()) * float(num2.get())
            my.set(t)
        except:
            msgbox('error')

    def mn():
        if num2.get() == "0":
            KeyError('error')
        try:
            m = float(num1.get()) - float(num2.get())
            my.set(m)
        except:
            msgbox('error')

    # Buttons ---------------------------------------

    but1 = Button(top2, text="+", width=4, height=2, command=lambda: game())
    but1.pack(side="left", padx=2, pady=2)

    but2 = Button(top2, text="/", width=4, height=2, command=lambda: tg())
    but2.pack(side="left", padx=2, pady=2)

    but3 = Button(top2, text="*", width=4, height=2, command=lambda: zrb())
    but3.pack(side="left", padx=2, pady=2)

    but4 = Button(top2, text="-", width=4, height=2, command=lambda: mn())
    but4.pack(side="left", padx=2, pady=1)

    # Entrys end labls  ---------------------------------------

    lb1 = Label(top1, text="Enter numbers :")
    lb1.pack(side="top", padx=1, pady=1)
    en = Entry(top1, background="WHITE", textvariable=num1)
    en.pack(side="top", padx=2, pady=2)

    lb2 = Label(top1, text=" raulat end :")
    lb2.pack(side="top", padx=1, pady=1)
    en2 = Entry(top1, background="WHITE", textvariable=num2)
    en2.pack(side="top", padx=2, pady=2)

    en2 = Entry(top3, background="#ECF0F1", textvariable=my)
    en2.pack(side="bottom", padx=4, pady=5)

    lb2 = Label(top3, text=" end in numbers :")
    lb2.pack(side="bottom", padx=1, pady=1)

    root.mainloop()

# ================================================ The End Gul ====================================

elif user == "24":
    try:
        en_link_addres = input('Enter linke site : ')  # linke DDos
        new_my = system(f"ping {en_link_addres}")  # ddos in Terminall
    except:
        print(Fore.RED + "error tools DDos ")


elif user == "25":  # notbook
    root = Tk()
    root.geometry("180x120")
    root.resizable(width=False, height=False)
    root.title("NOTBOOK")
    color = "#fcfbb2"
    root.configure(bg=color)

    tex = Text(root, width=120, height=120)
    tex.pack(side="top")

    root.mainloop()


# ==================================== Encode =========================================


elif user == "26":
    Crete = Fernet.generate_key()  # Crear key
    print(f"key :  {Crete} ")  # print 'key'
    user_enc = input('Enter path : ')  # input path

    with open(user_enc, "rb") as f:  # read in file  'user_enc'
        date = f.read()  # read

    nameStr = str(randrange(1, 100000000))  # name file_2

    file_2 = open(nameStr, "wb")  # open To file

    encd = Fernet(Crete)

    mnt = encd.encrypt(date)  # encrypt file
    file_2.write(mnt)  # write file encrpte


# ================================================ dec =============================
elif user == "27":
    key = Fernet.generate_key()

    user_filw = input('Enter patch : ')
    filew = open(user_filw, 'rb')
    data_10 = filew.read()

    filew.close()

    user_key = str(input("Enter key : "))
    f = Fernet(user_key)
    name_str = str(randrange(1, 100000))
    files = open(f'{name_str}.png', "wb")

    enc_2 = f.decrypt(data_10)
    files.write(enc_2)


# shut down ===========================================================

elif user == '28':
    # clear page
    clears_ = system("clear")
    # page 1 main
    page_1 = """
# [29] shutdown
# [30] show network - connected and disconnected
# [31] show UUID 
# [32] ipconfig
# [33] YouTube Downloads

    """
    print(Fore.GREEN + page_1)
    user_page_1 = int(input('enter tools : ').lower())  # input tools number

    # shutdown system
    if user_page_1 == 29:
        plat = platform.system()
        try:
            if plat == "Windows":
                system('shutdown -s -t 10')

            elif plat == "linux":
                system('shutdown -h 10 ')

            elif plat == "darwin":
                system("shutdown -h -t 10 ")
        except:
            print(Fore.RED + "error tools shutdown ")

    elif user_page_1 == 30 : 
        if platform.system() == "Linux":
            nmcli_dev = system("nmcli dev") 
            # show DEVICE  TYPE  STATE  CONNECTION
        elif platform.system() == "Windows": 
            net_use = system("net use")
        else: 
            print("❌support") 
    
    elif user_page_1 == 31: 
        # show network co...
        if platform.system() == "Linux": 
            nmcli_con = system("nmcli con") 
        else: 
            pass
    
    elif user_page_1 == 32: 
        # show network
        if platform.system() == "Linux":
            ifconifg = system("ifconfig")

        elif platform.system() == "Windows":
            ipconifg = system("ipconfig") 
        else: 
            pass
    
    elif user_page_1 == 33: 
        youtube_download = str(input('Enter Link Youtube : ')) 
        # https://youtu.be/prlaBaJm0rU
        try:
            video =YouTube(url=youtube_download) 
            streem = video.streams.get_highest_resolution()
            streem.download()
        except: 
            print(Fore.RED + "error download link " + Fore.BLUE + f"[{youtube_download}]")
    
# ======================================================= Time =======
Time_end_res = time()  # time
my_and_rews = localtime(Time_end_res)

De_time = (f"{my_and_rews.tm_hour}:{my_and_rews.tm_min}:{my_and_rews.tm_sec}")


# =========================================== Date =========================
Time_end = time()  # time
my_and_time = localtime(Time_end)
with open("./with.txt", mode='a') as files:  # write to txt
    files.write(
        F"\nTools : {user} \ntime : {De_time} \nplatform : {platform.system()}")  # Date
    files.write("\n--------------------")

# =========================================== Date =========================

if user == '19':
    with open("./with.txt", mode='a') as files:  # write to txt
        files.write(
            F"\nTools : {user} \ntime : {De_time} \nplatform : {platform.system()} \nlink : {users_Download}")  # Date
        files.write("\n--------------------")
else:
    exit()
