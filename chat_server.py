import socket as s
import threading as thd
import os

skt = s.socket(s.AF_INET, s.SOCK_DGRAM)
localIP = input("Enter Your IP: ")
skt.bind((localIP, 5253))

usrIP = input("Enter Partner IP: ")
print()

def recv_msg():
    while True:
        msgRcv = skt.recvfrom(1024)
        if msgRcv[0].decode() == "quit":
            print("Partner is Offline!")
            os._exit(1)
        print(msgRcv[1][0] + ": " + msgRcv[0].decode())

def send_msg():
    while True:
        data = input().encode()
        msgSent = skt.sendto(data, (usrIP, 5253))
        if data.decode() == "quit":
            os._exit(1)

send_thd = thd.Thread(target=send_msg)

rcv_thd = thd.Thread(target=recv_msg)

send_thd.start()
rcv_thd.start()
