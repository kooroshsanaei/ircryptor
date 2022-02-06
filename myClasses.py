import time, os
from colorama import Fore as Color


class Psentense:
    def printer(self, sentense): #Get a input from the user and Type print it out 
        sentense_len = len(sentense)
        for letter in range(sentense_len):
            print(Color.CYAN + sentense[letter], end='', flush = True);time.sleep(0.1) #print it  out word by word


class Introduce(Psentense):
    def __init__(self):
        os.system('clear')
        self.printer("[!] Hello Friend :)")
        time.sleep(0.6)








	    	    


    