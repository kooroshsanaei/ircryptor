from colorama import Fore as color
from time import sleep 

bold = '\033[1m'
endbold = '\033[0m'

def banner():
    print(bold+color.RED+'''
        
      _____ _____    _____                  _             
    |_   _|  __ \  / ____|                | |            
      | | | |__) || |     _ __ _   _ _ __ | |_ ___  _ __ 
      | | |  _  / | |    | '__| | | | '_ \| __/ _ \| '__|
     _| |_| | \ \ | |____| |  | |_| | |_) | || (_) | |   
    |_____|_|  \_(_)_____|_|   \__, | .__/ \__\___/|_|   
                                __/ | |                  
                               |___/|_|                  base64 | hex | rot13
     '''+endbold)

    print(bold+color.WHITE+'''
    ----------------------------------
    ⚒  Programmer: koorosh sanaei    ⚒
    ⚒  Lable : Ultraamooz            ⚒
    ⚒  IG : zero_Dey                 ⚒
    ----------------------------------
     '''+endbold)  
    sleep(1)
def menu():

    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Base64")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[2]"+color.LIGHTYELLOW_EX+" Hex")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[3]"+color.LIGHTYELLOW_EX+" Rot13")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[4]"+color.LIGHTYELLOW_EX+" Decoder")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[0]"+color.LIGHTYELLOW_EX+" exit"+endbold)



def decoder_menu():
    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Base64")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[2]"+color.LIGHTYELLOW_EX+" Hex")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[3]"+color.LIGHTYELLOW_EX+" Rot13")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[0]"+color.LIGHTYELLOW_EX+" back"+endbold)