str1="gndk€rlqhmtkwwp}z"
str2=""
t=1
for i in str1:
    str2+=chr(ord(i)-t)
    t+=1
print(str2)
