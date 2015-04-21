#coding=utf-8
import string
import os
import threading
from time import ctime,sleep
lock=threading.Lock()
class FenLei():
    def __init__(self):
        self.a=[]
    def Fenlei(self,filename,xunlianji,ceshiji):
        f1=open(filename,'r')
        xulianji=open('xunlianji','a+')
        ceshiji=open('ceshiji','a+')
        for line in f1:
            #把line以逗号为区分，切割为列表
            line=line.split(',')
            #line[5]为时间，
            line[5]=line[5].replace('-','')#替换掉日期里的‘-’
            line[5]=line[5].replace(' ','')#替换掉小时那里的‘ ’
            date=line[5]
            if date<'2014121400':#这里是取的后五天为测试集，所以时间小于2014121400的就入训练集，反之入测试集，时间可自行更改
                lines=','.join(line)#将列表变为字符串，并加入 逗号间隔
                if lock.acquire():#线程锁，防止死锁
                    xulianji.write(lines)
                lock.release()
    
            else:
                lines=','.join(line)
                if lock.acquire():
                    ceshiji.write(lines)
                lock.release()
    
        f1.close()
if __name__ == "__main__":
    print "now is start %s" %ctime()
    ceshiji=open('ceshiji','w+')#以写入方式创建一个文件名叫ceshiji
    xunlianji=open('xunlianji','w+')
    ss=FenLei()
    for i in range(0,9):
        filename="output_%d"%i+'.txt'#文件名，在上个代码切割好文件的基础上，如果你有11个切割文件，就把10变为11
        #ss.Fenlei(filename,ceshiji,xunlianji)
        i = threading.Thread(target=ss.Fenlei,args=(filename,ceshiji,xunlianji))#多线程创建
        i.start()
    i.join()
    
    ceshiji.close()
    xulianji.close()
    print "all over %s" %ctime()

    
    
            
               
               
                
            
        