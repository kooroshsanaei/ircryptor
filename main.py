''' 
Creator => Koorosh sanaei
Telegram Channel => ultrasecurity
YouTube => ultraamooz
Telegram =>legol4sx
Email => legol4sx@gmail.com

Version => 1.0 , 2022
DATE:6-02-2022
TIME: 09:44 AM

#MadeIniran
      _____ _____    _____                  _             
    |_   _|  __ \  / ____|                | |            
      | | | |__) || |     _ __ _   _ _ __ | |_ ___  _ __ 
      | | |  _  / | |    | '__| | | | '_ \| __/ _ \| '__|
     _| |_| | \ \ | |____| |  | |_| | |_) | || (_) | |   
    |_____|_|  \_(_)_____|_|   \__, | .__/ \__\___/|_|   
                                __/ | |                  
                               |___/|_|                  base64 | hex | rot13

'''

from colorama import Fore as color
from time import sleep
import os, sys
import myClasses, banner, decoder


bold = '\033[1m'
endbold = '\033[0m'

#Create a module for needed libraries
def needs(module):
    module = str(module);os.system('clear')
    print(color.GREEN+"Please install% library\n pip3 install %s" %(module))
    sleep(0.3);sys.exit()

#Import needed Modules

try:
    from colorama import Fore as color
except:
    needs(colorama)

#####################

myClasses.Introduce()


while True:
    os.system('clear')
    try:
        banner.banner();banner.menu()
        option = int(input(color.RED+"\n[⚡] "+color.RED+"ir.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ⇒ " ))
        
        #check for the option
        if (option == 1):
            os.system('clear');banner.banner()
            print(color.WHITE+"Enter Your Text:")
            user_option = input(color.RED+"\n[⚡] "+color.RED+"ir.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"base64"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ⇒ " )
            print(bold+color.WHITE+"Encrypted ⚶\n \t ")
            os.system(f'echo {user_option} | base64')
            input('\n press any key...'+endbold)
            continue
        
        elif (option == 2):
            os.system('clear');banner.banner()
            print(color.WHITE+"Enter Your Text:")
            user_option = input(color.RED+"\n[⚡] "+color.RED+"ir.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"hex"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ⇒ " )
            print(bold+color.WHITE+"Encrypted ⚶\n \t")
            os.system(f"echo {user_option} | xxd -p")
            input('\n press any key...'+endbold)
            continue
        elif (option == 3):
            os.system('clear');banner.banner()
            print(color.WHITE+"Enter Your Text:")
            user_option = input(color.RED+"\n[⚡] "+color.RED+"ir.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"rot13"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ⇒ " )
            print(bold+color.WHITE+"Encrypted ⚶\n \t")
            os.system(f"echo {user_option} | tr 'A-Za-z' 'N-ZA-Mn-za-m'")
            
            input('\n press any key...'+endbold)
            continue

        ##################DECODER
        
        elif (option == 4):
            os.system('clear');banner.banner();banner.decoder_menu()
            option = int(input(color.RED+"\n[⚡] "+color.RED+"ir.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ⇒ " ))
            decoder.decoder_menu(option)
            continue
            
        elif (option == 0):
            os.system('clear')
            sys.exit()


    except KeyboardInterrupt:
        sys.exit()