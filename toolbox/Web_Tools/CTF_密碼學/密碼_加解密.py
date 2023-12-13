import base64
import codecs

def ascii1():
    a1=input("值: ")
    try:
        a11=a1.encode()
        a11=int.from_bytes(a11, "big")
        print("Binary: "+bin(a11))
    except:
        print("Binary: None")
    #
    try:
        a12=''.join([hex(ord(x))[2:] for x in a1])
        print("Hex: "+a12)
    except:
        print("Hex: None")
    #
    try:
        a13=a1.encode('ascii')
        a13=base64.b64encode(a13)
        a13 = a13.decode('ascii')
        print("Base64: "+str(a13))
    except:
        print("Base64: None")
    #
    try:
        a14=""
        for i in a1:
            a14=a14+str(ord(i))+" "
        print("Dec: "+str(a14))
    except:
        print("Dec: None")
    #
    try:  
        a15=codecs.encode(a1, 'rot_13')
        print("Rot13: "+str(a15))
    except:
        print("Rot13: None")
    #
    
def binary1():
    a1=input("值: ")
    try:
        n = int(a1, 2)
        n=n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        print("ASCII: "+n)
    except:
        print("ASCII: None")
    #
    try:
        n2=hex(int(a1, 2))
        print("Hex: "+n2)
    except:
        print("Hex: None")
    #
    try:
        n3=int(a1, 2)
        n3=n3.to_bytes((n3.bit_length() + 7) // 8, 'big').decode()
        n3=n3.encode('ascii')
        n3=base64.b64encode(n3)
        n3 = n3.decode('ascii')
        print("Base64: "+str(n3))
    except:
        print("Base64: None")
    #
    try:
        n4 = int(a1, 2)
        n4=n4.to_bytes((n4.bit_length() + 7) // 8, 'big').decode()
        n14=""
        for i in n4:
            n14=n14+str(ord(i))+" "
        print("Dec: "+str(n14))
    except:
        print("Dec: None")
    #
    try:
        n5 = int(a1, 2)
        n5=n5.to_bytes((n5.bit_length() + 7) // 8, 'big').decode()
        n15=codecs.encode(n5, 'rot_13')
        print("Rot13: "+str(n15))
    except:
        print("Rot13: None")
    #
        
def hex1():
    a1=input("值: ")
    try:
        n5=bytearray.fromhex(a1).decode()
        print("ASCII: "+str(n5))    
    except:
        print("ASCII: None")
    #
    try:
        n6=bytearray.fromhex(a1).decode()
        a11=n6.encode()
        a11=int.from_bytes(a11, "big")
        print("Binary: "+bin(a11))
    except:
        print("Binary: None")
    #   
    try:
        n7=bytearray.fromhex(a1).decode()
        a13=n7.encode('ascii')
        a13=base64.b64encode(a13)
        a13 = a13.decode('ascii')
        print("Base64: "+str(a13))
    except:
        print("Base64: None")
    #
    try:
        n5=bytearray.fromhex(a1).decode()
        a14=""
        for i in n5:
            a14=a14+str(ord(i))+" "
        print("Dec: "+str(a14))
    except:
        print("Dec: None")
    #
    try:
        n5=bytearray.fromhex(a1).decode()
        a15=codecs.encode(n5, 'rot_13')
        print("Rot13: "+str(a15))
    except:
        print("Rot13: None")
    #
def base641():
    a1=input("值: ")
    try:
        m = a1.encode('ascii')
        m = base64.b64decode(m)
        m = m.decode('ascii')
        print("ASCII: "+str(m))
    except:
        print("ASCII: None")
    #
    try:
        m = a1.encode('ascii')
        m = base64.b64decode(m)
        m = m.decode('ascii')
        a11=m.encode()
        a11=int.from_bytes(a11, "big")
        print("Binary: "+bin(a11))
    except:
        print("Binary: None")
    #
    try:
        m = a1.encode('ascii')
        m = base64.b64decode(m)
        m = m.decode('ascii')
        a12=''.join([hex(ord(x))[2:] for x in m])
        print("Hex: "+a12)
    except:
        print("Hex: None")
    #
    try:
        m = a1.encode('ascii')
        m = base64.b64decode(m)
        m = m.decode('ascii')
        a14=""
        for i in m:
            a14=a14+str(ord(i))+" "
        print("Dec: "+str(a14))
    except:
        print("Dec: None")
    #
    try:
        m = a1.encode('ascii')
        m = base64.b64decode(m)
        m = m.decode('ascii')
        a15=codecs.encode(m, 'rot_13')
        print("Rot13: "+str(a15))
    except:
        print("Rot13: None")
    #
def dec1():
    a1=input("值: ")
    try:
        ae=""
        for i in a1.split(" "):
            i=int(i)
            ae+=chr(i)
        print("ASCII: "+ae)
    except:
        print("ASCII: None")
    #
    try:
        ae=""
        for i in a1.split(" "):
            i=int(i)
            ae+=chr(i)
        a11=ae.encode()
        a11=int.from_bytes(a11, "big")
        print("Binary: "+bin(a11))
    except:
        print("Binary: None")
    #
    try:
        ae=""
        for i in a1.split(" "):
            i=int(i)
            ae+=chr(i)
        a12=''.join([hex(ord(x))[2:] for x in ae])
        print("Hex: "+a12)
    except:
        print("Hex: None")
    #
    try:
        ae=""
        for i in a1.split(" "):
            i=int(i)
            ae+=chr(i)
        a13=ae.encode('ascii')
        a13=base64.b64encode(a13)
        a13 = a13.decode('ascii')
        print("Base64: "+str(a13))
    except:
        print("Base64: None")
    #
    try:
        ae=""
        for i in a1.split(" "):
            i=int(i)
            ae+=chr(i)
        a15=codecs.encode(ae, 'rot_13')
        print("Rot13: "+str(a15))
    except:
        print("Rot13: None")
    #
def rot131():
    a1=input("值: ")
    try:
        n15=codecs.decode(a1, 'rot_13')
        print("ASCII: "+n15)
    except:
        print("ASCII: None")
    #
    try:
        n15=codecs.decode(a1, 'rot_13')
        a11=n15.encode()
        a11=int.from_bytes(a11, "big")
        print("Binary: "+bin(a11))
    except:
        print("Binary: None")
    #
    try:
        n15=codecs.decode(a1, 'rot_13')
        a12=''.join([hex(ord(x))[2:] for x in n15])
        print("Hex: "+a12)
    except:
        print("Hex: None")
    #
    try:
        n15=codecs.decode(a1, 'rot_13')
        a13=n15.encode('ascii')
        a13=base64.b64encode(a13)
        a13 = a13.decode('ascii')
        print("Base64: "+str(a13))
    except:
        print("Base64: None")
    #
    try:
        n15=codecs.decode(a1, 'rot_13')
        a14=""
        for i in n15:
            a14=a14+str(ord(i))+" "
        print("Dec: "+str(a14))
    except:
        print("Dec: None")
    #

while True:
    print("\n\nASCII or Binary or Hex or\nBase64 or Dec or Rot13 ? (Lower case)\n")
    a=input("類別: ")
    print("\n")
    if a=="ascii":
        ascii1()
    
    if a=="binary":
        binary1()
   
    if a=="hex":
        hex1()
        
    if a=="base64":
        base641()
    
    if a=="dec":
        dec1()

    if a=="rot13":
        rot131()
