#coding:utf-8
import threading
from PIL import Image
from lsb import extract
import re
with open('darkweb2017-top10000.txt','r+') as f:
    f=f.readlines()
filename='flag.png'

def to_decode():
    for i in f:
        i=i.replace('\n','')
        if len(i)==7 and re.search('[0-9!?]',i)==None:
            out_file=i+'.txt'
            extract(filename,out_file,i)
to_decode()
