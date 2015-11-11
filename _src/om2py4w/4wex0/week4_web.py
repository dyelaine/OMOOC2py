#encoding:utf-8
from datetime import datetime

import sqlite3
from bottle import route, run, debug, template, request, static_file, error


@route('/mydiary')

def review_diary():
    conn = sqlite3.connect('diary.db')  #连接已建立的数据库
    c = conn.cursor()
    c.execute("SELECT content FROM diary")
    result = c.fetchall()
    c.close()
    output = template('web_diary', rows=result)
    return output



@route('/mydiary', method='GET')
def add_diary():

    if request.GET.get('save', '').strip():

        new = request.GET.get('content','').strip()
        conn = sqlite3.connect('diary.db')
        c = conn.cursor()

        today = datetime.now()
        t = today.strftime("%y/%m/%d")

        new = new.decode('utf-8')  #将中文进行正确编码！
        
        c.execute("INSERT INTO diary (time, content) VALUES (?,?)", (t, new))
        new_id = c.lastrowid

        conn.commit()
        c.close()

#        return '<p>已经保存下来啦, 日期是 %s</p>' % today
    conn = sqlite3.connect('diary.db')  #连接已建立的数据库
    c = conn.cursor()
    c.execute("SELECT content FROM diary")
    result = c.fetchall()
    c.close()
    output = template('web_diary', rows=result)
    return output


@route('/help')
def help():
    return static_file('help.html', root='/path/to/file')

@error(403)
def mistake403(code):
    return 'The content you sumbmitted has the wrong format'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


debug(True)
run(host = 'localhost', port = 8080, reloader = True)
