# -*-coding:utf-8-*-
import socket;

fp=[];
def Prepare():
    re=input("域名: ");
    filename="dic.txt";
    f=open(filename,'r');
    fr=f.readlines();
    fe=[];
    for i in fr:
        s,q=i.split("\n");
        fe.append(s);
    for d in fe:
        d=d+"."+re;
        fp.append(d);

def Num_2():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(1.0)
    for e in fp:
        try:
            result = socket.getaddrinfo(e, None);
            ip=result[0][4][0];
            print(e+' : {0} is open.'.format(ip))
        except:
            continue;
        finally:
            server.close()
    

if __name__ == '__main__':
    Prepare();
    Num_2();  
