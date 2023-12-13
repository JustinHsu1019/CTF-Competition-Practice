from pwn import *
p = remote('60.250.197.227',10000)
p= process('/bin/sh')
p.sendline('ls')
p.interactive()
