#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import sqlite3

from datetime import datetime

reload(sys)  
sys.setdefaultencoding('utf8')

def main():
    print 'Type "q" or "quit" to exit.'
    print 'Type "l" or "list" to view all the notes.'
    print 'Type anything else as a new diary.'

    while True:
        INPUT = raw_input('> ').strip()
        inp = INPUT.lower()
        if inp in ['quit','q']:
            break
        elif inp in ['list','l']:
            print listnotes()
        else:
            addnote(INPUT)

def addnote(note):
    conn = sqlite3.connect('diary.db')
    c = conn.cursor()

    today = datetime.now()
    t = today.strftime("%y/%m/%d")

    new = note.decode("utf8")
        
    c.execute("INSERT INTO diary (time, content) VALUES (?,?)", (t, note))

    conn.commit()
    c.close()

def listnotes():
    conn = sqlite3.connect('diary.db')  #连接已建立的数据库
    c = conn.cursor()
    c.execute("SELECT content FROM diary")
    result = c.fetchall()
    print result

if __name__ == '__main__':
    main()