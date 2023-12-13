import re

filename=input("Filename: ")
f = open(filename, "rb")
str1 = f.read()
f.close()
fr=open('python.txt', 'w')
fre=open('python-2.txt', 'w')
str2=str1.hex()
#num = re.findall('\w{32}' ,str2)
n=0
for i in str2:
    if n%70==0 and n!=0:
        fr.write("\n")
    fr.write(i)
    n+=1
    
#for i in num:
    #fr.write(i+"\n")
fr.close()

#wb rb
