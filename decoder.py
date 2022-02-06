import os, sys
from colorama import Fore as color
from time import sleep
import banner

bold = '\033[1m'
endbold = '\033[0m'

def decoder_menu(user_inp):
    if (user_inp == 1):
        os.system('clear');banner.banner()
        print(color.WHITE+"Enter Your Encrypted text in base64:")
        user_option = input(color.RED+"\n[⚡] "+color.RED+"ir.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"base64-Dcryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ⇒ " )
        os.system(f'echo {user_option} | base64 -d')
        input('\n press any key...'+endbold)
    elif (user_inp == 2):
        os.system('clear');banner.banner()
        print(color.WHITE+"Enter Your Encrypted text in Hex:")
        user_option = input(color.RED+"\n[⚡] "+color.RED+"ir.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"Hex-Dcryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ⇒ " )
        os.system(f'echo {user_option} | xxd -p -r')
        input('\n press any key...'+endbold)

    elif (user_inp == 3):
        os.system('clear');banner.banner()
        print(color.WHITE+"Enter Your Encrypted text in Rot13:")
        user_option = input(color.RED+"\n[⚡] "+color.RED+"ir.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"Rot13-Dcryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ⇒ " )
        os.system(f"echo {user_option} | tr 'A-Za-z' 'N-ZA-Mn-za-m'")
        input('\n press any key...'+endbold)
    elif (user_inp == 0):
        pass

    else:
        print("print Bad input...")
        sleep(2)
        sys.exit()