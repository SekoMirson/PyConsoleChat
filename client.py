import socket
import threading
import os
import requests
import platform
from colorama import init, Fore, Back, Style
init()

Menu = f"""
    {Fore.LIGHTCYAN_EX}=========================================
    =          {Fore.GREEN}Python Console Chat          {Fore.LIGHTCYAN_EX}=
    =         {Fore.GREEN}Developer: SekoMirson         {Fore.LIGHTCYAN_EX}=
    ========================================={Style.RESET_ALL}

    1) Install Plugins
    2) Start Chat
    
    0) Close Server
"""

def temizle():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

public_ip = requests.get('https://api.ipify.org?format=json').json()['ip']

temizle()

def start_client():
    host = 'localhost'
    port = 1995
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    receive_thread = threading.Thread(args=(client_socket,))
    receive_thread.start()

    with open("userdata.txt", 'r') as dosya:
        icerik = dosya.read()
        if icerik:
            name = icerik
        else:
            name = input("Kullanici adiniz: ")
            with open("userdata.txt", "w") as dosya:
                dosya.write(name)
                dosya.close()

    print(f"    Welcome {name}\n")
    while True:
        try:
            #random_number = random.randint(1, 1000)
            role = f"Guest" #{str(random_number)}
            message = input("Your message: ")
            fullmessage = f"""IP: {public_ip} | Role: {role} | Username: {name} | Message: {message}"""
            client_socket.send(fullmessage.encode('utf-8'))
        except:
            print("Connection closed.")
            quitMsg = f"- {name} is left!"
            client_socket.send(quitMsg.encode('utf-8'))
            client_socket.close()
            break

if __name__ == "__main__":

    print(Menu)
    secim = int(input("~# "))

    if (secim == 1):
        os.system("cls")
        print(Fore.LIGHTCYAN_EX + "Install Plugins")
        os.system("pip install requests")
        os.system("pip install colorama")
        os.system("pip install platform")
        print(Fore.LIGHTCYAN_EX + "Plugins Installed.")

    elif (secim == 2):
        start_client()

    else:
        print("Close Server...")