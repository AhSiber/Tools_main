
from colorama import Fore, init # color in python 'colorama' Func in Windows 'init' !
import gtts # voice in python 
from pyfiglet import figlet_format # pyfiglet in python 'Tools' 
from socket import gethostbyname, gethostname # ip in socket '127.0.0.1'
import calendar # calend in python '2021' , '4' , '23'
from time import time, localtime # time 12 : 00 
import wget # dowanload in python link 
import requests # request api 
from def_init_mine import my_req # funck my_req
from define_font import font # funck font 
from def_danstny import Danstny # funck danstny 
from def_joke import joke # funck joke 
from def_numbers import numberss # funck number 
from meali import * # funck True code malit 
from verify_email import verify_email # verfiy Eamil 
from random import randrange # random number 
from tkinter import * # GUL 
import tkinter.messagebox # GUL hanel Error 
from os import system # os madouls in system 
from cryptography.fernet import Fernet # Encode end decrypt 

# {Knowledge in Persian}
# Developer : Ahura
# git hub : https://github.com/AhSiber

init()  # windows

help_tools = ''' 
# [1] Dispute           [12] craet password                 [24] DDos
# [2] Bank              [13] Wikipedia                      [25] NootBok (GUL)
# [3] charge            [14] Convert text to Morse code     [26] encode 
# [4] ip                [15] ping site                      [27] decode 
# [5] Date              [16] qr code
# [6] time              [17] Character  
# [7] req               [18] True Code Meli 
# [8] font              [19] Download  
# [9] des               [20] Email Verification  
# [10] joke             [21] Developer (GUL)
# [11] number           [22] voice 
                        [23] calculator (GUL)

'''
print(Fore.RED + help_tools) # color 

print(figlet_format('Tools', font="standard")) # Figlet format 'Tools'
print(Fore.GREEN) # color green 

user = input('enter Tools : ').lower() # input "lower" -- user 
if user == "1":
    try:
        def shop(Overall_profit, Total): # defin inputs (Overall_profit) and (Total)
            return F"Overall profit : {Overall_profit - Total}"
        Dispute = input('type Overall_profit : ')
        Dispute2 = input('Enter Total : ')
        print(shop(Dispute, Dispute2)) # print (Overall_profit) and (Total)  
    except:
        print(Fore.RED + "error tools Dispute ") # Handel Error 


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
        name = gethostname() # get name host 
        by_name = gethostbyname(name) # get host by name 
        print(f"ip address : ", Fore.RED + by_name) # red ip 127.0.0.1
    except:
        print(Fore.RED + "error tools host ") # handel Error 


elif user == "5":
    try:
        user_clender = int(input('Enter Yers : '))
        user_month = int(input('type manth : '))
        new_s_f = calendar.month(user_clender, user_month) # clander 2021 
        print(Fore.RED + new_s_f) # color red 
    except:
        print(Fore.RED + "error Tools calender ") # handel error 


elif user == "6":
    try:
        user_time = time() # time [272.9293827382] 
        my_time = localtime(user_time) # local time tm_hour or tm_main or tm_sec 
        print(F"{my_time.tm_hour}:{my_time.tm_min}:{my_time.tm_sec}") 
    except:
        print(Fore.RED + "error tools time ") # handel Error 

elif user == "7":
    try:
        print(my_req.req()) # req
    except:
        print(Fore.RED + 'error tools req') # handel eror 


elif user == "8":
    try:
        font.font_en() # font =>  60 
    except:
        print(Fore.RED + "eror tools font ") # handel Error 


elif user == "9":
    try:
        print(Danstny.dnst()) # danstny funck == 5000 == 
    except:
        print(Fore.RED + "error tools des ") # handel Error 

elif user == "10":
    try:
        print(joke.jokes()) # jocke == 7000 === 
    except:
        print(Fore.RED + "error tools joke")


elif user == "11":
    try:
        print(numberss.number()) # exchange number in str 
    except:
        print(Fore.RED + "error Tools number ") # handel error 

elif user == "12":
    try:
        user_password = int(input('Enter len password : ')) # input len password 
        name = requests.get(
            f"http://api.codebazan.ir/password/?length={user_password}").text # api Create password 
        print(f"password : {Fore.YELLOW + name}") 
    except:

        print(Fore.RED + "error password")


elif user == "13":
    try:
        Wikipedia_user = input('search in Wikipedia : ') # input serach 
        Wikipedia = requests.get(
            f"https://api.codebazan.ir/wiki/?search={Wikipedia_user}").text # api seach in wikipadia 
        print(Wikipedia)
    except:
        print(Fore.RED + "error search Wikipedia")

elif user == "14":
    try:
        user_mours = input('type value : ') # str 
        lange = str(input('enter lange : ')) # lange 
        nmours = requests.get(
            f"https://api.codebazan.ir/mourse/?lang={lange}&text={user_mours}").text # mours 
        print(nmours)
    except:
        print(Fore.RED + "error tools mours")

elif user == "15":
    try:
        user_ping = input('Enter site : ') # input site 
        ping = requests.get(
            f"https://api.codebazan.ir/ping/?url={user_ping}").text # ping site 
        print(f"ping site : {Fore.LIGHTBLUE_EX + ping}")

    except:
        print(Fore.RED + "error tools ping")


elif user == "16":
    try:
        sname = input('Enter Address exs QR : ') # iter code in QR code 
        my = (f"https://api.codebazan.ir/qr/?size=500x500&text={sname}.png") # api code RQ
        dow = wget.download(my) # download QR 
        dow = f'{sname}.png' # format '.png'
        print(dow)
    except:
        print(Fore.RED + "error tools qrCode ") # handel Error 

elif user == "17":
    try:

        user_len = input('Enter Character : ') # enter charchter === name == len(4) 
        print(F"Number of characters : {len(user_len)}") 
    except:
        print(Fore.RED + "error tools Character ")

elif user == "18":
    try:
        user_code_maily = input('Enter Code meli : ')
        print(code_meali.mali(user_code_maily)) # funck code True end False 
    except:
        print(Fore.RED + "error tools codemali")

elif user == "19":
    try:
        users_Download = input('Enter linke : ') # enter linke 
        Dosnm = wget.download(users_Download) # download linke inputy !  
        print(Dosnm)
    except:
        print(Fore.RED + "error tools Download ")


elif user == "20":
    try:
        email = str(input('enter Email : ')) # Enter email 
        print(f"your email {verify_email(email)}") # verfiy Emalit 
    except:
        print(Fore.RED + "error tools email ")


elif user == "21": # Developer 
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
        en_link_addres = input('Enter linke site : ') # linke DDos 
        new_my = system(f"ping {en_link_addres}") # ddos in Terminall  
    except:
        print(Fore.RED + "error tools DDos ")


elif user == "25": # notbook 
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
    Crete = Fernet.generate_key() # Crear key  
    print(f"key :  {Crete} ") # print 'key'
    user_enc = input('Enter path : ') # input path

    with open(user_enc, "rb") as f: # read in file  'user_enc' 
        date = f.read() # read 

    nameStr = str(randrange(1, 100000000)) # name file_2 

    file_2 = open(nameStr, "wb") # open To file 

    encd = Fernet(Crete) 

    mnt = encd.encrypt(date) #encrypt file 
    file_2.write(mnt) # write file encrpte 


# ================================================ dec ============================= 
elif user == "27":
    key = Fernet.generate_key() 

    user_filw = input('Enter patch : ')
    filew = open(user_filw , 'rb')  
    data_10 = filew.read()  

    filew.close() 

    user_key = str(input("Enter key : "))
    f = Fernet(user_key) 
    name_str = str(randrange(1,100000))
    files = open(f'{name_str}.png' , "wb")

    enc_2 = f.decrypt(data_10) 
    files.write(enc_2) 

else:
    print(Fore.RED + "Error input !")

Time_end = time() # time 
my_and_time = localtime(Time_end)
with open("./with.txt", mode='a') as files: # write to txt 
    files.write(
        F"Time_login : {my_and_time.tm_hour}:{my_and_time.tm_min}:{my_and_time.tm_sec} : Tools :  {user} \n") # Date 



Time_end = time() # time Download 
my_and_time = localtime(Time_end)
with open("./link_dow.txt", mode='a') as files: # write to txt 
    if user == "19" : 
        files.write(
            F"Time_login : {my_and_time.tm_hour}:{my_and_time.tm_min}:{my_and_time.tm_sec} : link :  {users_Download} \n") # Date 

