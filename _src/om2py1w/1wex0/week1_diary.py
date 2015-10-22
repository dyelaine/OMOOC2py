# -*- coding: utf-8 -*-
import time

print 'Welcome to the Dear Diary'

leave = 0

while leave == 0:

    print u'主人好，输入record记录心情，输入review阅读之前的心情，输入quit退出系统。'

    option = raw_input('>>')


                                                    # ----用户做出选择，查看已有记录----
    
    
    if option == 'review':  
        diaryFile = open('diary.txt','r')                       
        diary = diaryFile.read()
        print u'============Dear Diary============'
        print diary


                                                    # ----输入文字，记录日记 ----   
    if option == 'record':
        diaryFile = open('diary.txt','a')
        write = 'y'
        while write =='y':
            diary = raw_input('>>')
            localtime = time.asctime(time.localtime(time.time()))
            diaryFile.write('\n' + localtime + '  ' + diary)

                                                    # ----是否继续写日记----        
            print u'是否继续记录呢(y/n)'
            write = raw_input()

                                                    # ----不继续写日记，是否退出系统----        
            if write != 'y':
                print u'是否退出系统呢(y/n)'
                write = raw_input()
                if write == 'y':
                    leave = 1
                    write = 'n'
                    continue


                                                    #----退出系统----

    if option == 'quit':
        diaryFile = open('diary.txt','r')
        leave = 1
        print u'谢谢使用，期待再见。'
        diaryFile.close()
