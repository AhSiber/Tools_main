import os 
from time import sleep

print("Package installation may take 20 and 25 minutes.")
print("Please do not look at the bottom of the tool installation if the tool has a problem installing it manually")
print('--------------------------------------------------------------------------------')
try: 
    sleep(10.0)
    print("Start installing the color package")
    os.system("pip install colorama")
    sleep(20.0) 
    print('--------------------------------------------------------------------------------')
    print('Start installing gTTS package')
    os.system("pip install gTTS")
    sleep(120.0) 

    print('--------------------------------------------------------------------------------')

    print('Start installing the package pyfiglet ')
    os.system("pip install pyfiglet")
    sleep(120.0) 

    print('--------------------------------------------------------------------------------')

    print('Start installing the socket package')
    os.system("pip install socket ")
    sleep(120.0) 

    print('--------------------------------------------------------------------------------')

    print('Start installing Weiss package')
    os.system("pip install gTTS")
    sleep(120.0) 
    print('--------------------------------------------------------------------------------')

    print('Start installing calendar  ')
    os.system("pip install calendar")
    sleep(120.0) 
    print('--------------------------------------------------------------------------------')

    print('Start installing wget  ')
    os.system("pip install wget")
    sleep(120.0) 
    print('--------------------------------------------------------------------------------')

    print('Start installing requests  ')
    os.system("pip install requests")
    sleep(120.0) 
    print('--------------------------------------------------------------------------------')

    print('Start installing verify_email  ')
    os.system("pip install verify_email")
    sleep(120.0) 
    print('--------------------------------------------------------------------------------')

    print('Start installing random  ')
    os.system("pip install random")
    sleep(120.0) 
    print('--------------------------------------------------------------------------------')

    print('Start installing tkinter  ')
    os.system("pip install tkinter")
    sleep(120.0) 
    print("----------------------------------------------------------------------------------") 
    os.system('pip install cryptography')
except :
    print('There is a problem with the installation')
