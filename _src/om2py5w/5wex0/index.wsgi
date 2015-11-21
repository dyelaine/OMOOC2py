# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
from bottle import *
import sae
import sae.kvdb



count = 0

kv = sae.kvdb.Client()

def write_diary(post):
    global count
    count += 1
    ctime = time.ctime()
    key = 'key' + str(count)
    value = {'time':ctime,'content':post}
    kv.set(key,value)

def get_diary():
    results = []
    for item in kv.get_by_prefix('key'):
        results.append(item[1])
    r = results[::-1]
    return r   

app = Bottle()

@app.route('/')
def write():
    mydiary = get_diary() 
    return template('webdiary', rows=mydiary)

@app.route('/', method='POST')
def do_write():
    new_diary = request.forms.get('content') 
    write_diary(new_diary) 
    mydiary = get_diary()
    return template('webdiary', rows=mydiary)

@app.route('/hello')
def hello():
    return 'hello world---from bottle'
#    return template('webdiary', rows=mydiary);

application = sae.create_wsgi_app(app)