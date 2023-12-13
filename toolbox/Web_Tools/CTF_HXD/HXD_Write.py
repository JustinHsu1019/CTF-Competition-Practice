filenames="python.txt"
filename=input("Filename: ")
f = open(filenames, "r")
fr=f.readlines()
str1=""
for i in fr:
    str1+=i
fe=bytes.fromhex(str1)
f.close()
ft = open(filename, "wb")
ft.write(fe)
ft.close()

