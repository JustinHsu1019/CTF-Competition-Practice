import os 
import binascii 
import struct

misc = open("148a3ba22b8541f48f354f3e27f0aa4c.png","rb").read()

for i in range(1024): 
    data = misc[12:16] + struct.pack('>i',i)+ misc[20:29]
    crc32 = binascii.crc32(data) & 0xffffffff 
    if crc32 == 0x932f8a6b: 
        print (i) 
