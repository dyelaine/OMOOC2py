# -*- coding: utf-8 -*-
import socket 
import sys 

# create dgram udp socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host = 'localhost'
port = 1019

print u'您好，欢迎进入日记系统，按"回车键"阅读以往记录，按q退出系统！'

while True:
    
	msg = raw_input('>>')

	if msg == '':
		diaryFile = open('diary.txt')
		diary = diaryFile.read()
		print '============Dear Diary============'
		print diary
		continue

	if msg == 'q':
		print u'谢谢使用，期待再见。'
		sys.exit()

	try:
		# Set the whole string to the server
		s.sendto(msg,(host,port))

		# receive data from client(data, address)
		d = s.recvfrom(1024)
		reply = d[0]
		address = d[1]

		print reply

	except socket.error , msg:
		print 'Error Code: '+str(msg[0])+' Message '+ msg[1]
		sys.exit()

