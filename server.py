import socket
import threading
import requests
import sqlite3
import os
from colorama import init, Fore, Back, Style
init()

Menu = f"""
    {Fore.LIGHTCYAN_EX}=========================================
    =          {Fore.GREEN}Python Console Chat          {Fore.LIGHTCYAN_EX}=
    =         {Fore.GREEN}Developer: SekoMirson         {Fore.LIGHTCYAN_EX}=
    ========================================={Style.RESET_ALL}
    
    1) Install Plugins
    2) Start Server
    3) Stop Server - (CTRL+C)
    
    0) Close Server
"""

def create_table(conn):
    # Tablo yapısını tanımlayın (gerekirse değiştirin).
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        role TEXT,
        username TEXT,
        message TEXT
    );
    """
    conn.execute(create_table_sql)

def main():
    conn = sqlite3.connect(export_data_db)
    cursor = conn.cursor()
    create_table(conn)
    conn.commit()
    conn.close()

export_data_db = "veritabani.db"
export_data_log = "log.txt"

public_ip = requests.get('https://api.ipify.org?format=json').json()['ip']

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(Fore.GREEN+message)
            msg = message
            split_msg = msg.split('|')

            result = {}
            for part in split_msg:
                key, value = part.split(':')
                key = key.strip()
                value = value.strip()
                result[key] = value

            conn = sqlite3.connect(export_data_db)
            cursor = conn.cursor()

            insert_data_sql = "INSERT INTO messages (ip, role, username, message) VALUES (?, ?, ?, ?)"

            conn.execute(insert_data_sql, (result['IP'], result['Role'], result['Username'], result['Message']))
            conn.commit()
            conn.close()

        except:
            break

    client_socket.close()

def start_server():
    host = f"localhost"
    port = 1995

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"""
    {Fore.LIGHTCYAN_EX}=========================================
    =              {Fore.RED}S E R V E R              {Fore.LIGHTCYAN_EX}=
    =          {Fore.BLUE}===================          {Fore.LIGHTCYAN_EX}=
    =          {Fore.GREEN}Python Console Chat          {Fore.LIGHTCYAN_EX}=
    =         {Fore.MAGENTA}Developer: SekoMirson         {Fore.LIGHTCYAN_EX}=
    ========================================={Style.RESET_ALL}
""")

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"{Fore.GREEN}+ {client_addr[0]}:{client_addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":

    print(Menu)
    secim = int(input("~# "))

    if (secim == 1):
        os.system("cls")
        print(Fore.LIGHTCYAN_EX + "Install Plugins")
        os.system("pip install requests")
        os.system("pip install colorama")
        os.system("pip install sqlite3")
        print(Fore.LIGHTCYAN_EX + "Plugins Installed.")

    elif (secim == 2):
        main()
        start_server()

    else:
        print("Close Server...")