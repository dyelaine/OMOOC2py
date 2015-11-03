# -*- coding: utf-8 -*-
from datetime import datetime

import socket
import sys

HOST = '' # Symbolic name meaning all available interfaces
PORT = 1019 # Arbitary non-privileged port

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))

#print history

diaryFile = open('diary.txt')
diary = diaryFile.read()
print '============Dear Diary============'
print diary

while True:
    # receive data from client(data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    address = d[1]

    if not data:
        break

    today = datetime.now()
    diary = data.strip()
 
    diaryFile = open('diary.txt','a')
    diaryFile.write('\n'+today.strftime("%y/%m/%d")+' client['+str(address[1])+'] '+ diary)
    diaryFile.close()

    print (today.strftime("%y/%m/%d")+' client['+str(address[1])+'] '+ diary)  

    reply = 'Server Recevied!' +' client['+str(address[1])+'] '+ diary

    s.sendto(reply, address)

s.close()
