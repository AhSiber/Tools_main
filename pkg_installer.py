import os  # moduls os system
from time import sleep  # time --?> sleep

print("Package installation may take 20 and 25 minutes.")
print("Please do not look at the bottom of the tool installation if the tool has a problem installing it manually")

# Necessary explanati
# ons for installing packages in two lines from this line onwards, all 
# packages are installed in 120 seconds difference in installation. You can use this shortcut to stop this process.

print('--------------------------------------------------------------------------------')
try:
    sleep(10.0)
    print("Start installing the color package")

# Necessary explanations for installing packages in two lines from this line onwards
# all packages are installed in 120 seconds difference in installation. You can use this shortcut to stop this process.

    os.system("pip install colorama")
    sleep(20.0)
    print('--------------------------------------------------------------------------------')
    print('Start installing gTTS package')

# This module is for creating sound with string and. . .
# Many other things, this module is mostly used to identify robots, and we put this feature as a fan for our tools. And how to install it

    os.system("pip install gTTS")
    sleep(120.0)

    print('--------------------------------------------------------------------------------')

    print('Start installing the package pyfiglet ')

# This module is used for design and beautification. If you want to see how this tool works 
# after installing the required modules and executing the file, you can see this module and how it works.

    os.system("pip install pyfiglet")
    sleep(120.0)

    print('--------------------------------------------------------------------------------')

    print('Start installing the socket package')

# This module is more involved in web scripting and we have used it safely in one of the tools

    os.system("pip install socket ")
    sleep(120.0)

    print('Start installing calendar  ')

#  With the help of this module, you can see the Gregorian dates

    os.system("pip install calendar")
    sleep(120.0)
    print('--------------------------------------------------------------------------------')

    print('Start installing wget  ')

# Is a module for download from the Internet 

    os.system("pip install wget")
    sleep(120.0)
    print('--------------------------------------------------------------------------------')

    print('Start installing requests  ')

# Is a module in the field of network and web in Python language 

    os.system("pip install requests")
    sleep(120.0)
    print('--------------------------------------------------------------------------------')

    print('Start installing verify_email  ')

# With this powerful module you can detect whether an email exists or not? Which is very useful in the field of web! 

    os.system("pip install verify_email")
    sleep(120.0)
    print('--------------------------------------------------------------------------------')

    print('Start installing random  ')

#  There is a module for random values 

    os.system("pip install random")
    sleep(120.0)
    print('--------------------------------------------------------------------------------')

    print('Start installing tkinter  ')

# Is a graphical relation module 

    os.system("pip install tkinter")
    sleep(120.0)
    print("----------------------------------------------------------------------------------")
    print("install cryptography . . . ")

# Is a module in the field of cryptography  

    os.system('pip install cryptography')
except:
    print('There is a problem with the installation')
