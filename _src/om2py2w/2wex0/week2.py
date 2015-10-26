#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from Tkinter import *           # 导入 Tkinter 库

root = Tk()                     # 创建窗口对象的背景色
                                
root.title("Dear Diary")   
#root.geometry('600x400')                           
frm = Frame(root)               #创建主窗口，主体窗口分为上下两个部分


#############窗口部件初始化#################
# Top Frame：包括文本输入和保存按钮
frm_t = Frame(frm)                   
Label(frm_t, text='请输入日记', font=('宋体', 20)).pack(side=LEFT)                                        
var = StringVar(frm_t)
text_input = Entry(frm_t, textvariable = var, font=("宋体", 20, "normal"), width=36)                            #文本输入框  
                                    
saveb = Button(frm_t, text = '保存', font = '宋体 -20 bold')            #保存按钮

saveb.pack(side = RIGHT)                                                 # 将小部件放置到主窗口中
text_input.pack(side = LEFT)
frm_t.pack(side = TOP)

#Bottom Frame：包括展示文档和滚动条
frm_b = Frame(frm)

text_shown = Text(frm_b, background = 'grey', font=("宋体", 18), width='60', height='20')
sbar = Scrollbar(frm_b)
########读取历史记录################
diaryFile = open('diary.txt','r')
text_shown.config(state = NORMAL)
text_shown.insert(END, diaryFile.read())
text_shown.see(END)
text_shown.config(state = DISABLED)
diaryFile.close()

text_shown.pack(side = LEFT)
sbar.pack(side = RIGHT, fill = Y)

frm_b.pack(side = BOTTOM)

############窗口部件初始化完成################


############按钮功能化#############
def printvar():
    line = text_input.get()

    text_shown.config(state = NORMAL)
    text_shown.insert(END, line+'\n')
    text_shown.see(END)
    text_shown.config(state = DISABLED)

    diaryFile = open('diary.txt','a')
    diaryFile.write(line + '\n')
    diaryFile.close()

    text_input.delete(0,END) # 保存后清空文字框

saveb['command'] = printvar
############按钮功能化完成#########

frm.pack()

root.mainloop()                 # 进入消息循环