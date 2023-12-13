import requests

def Prepare():
    re=input("網址: ");
    filename="dic.txt";
    f=open(filename,'r',encoding="utf-8");
    fr=f.readlines();
    fe=[];
    for i in fr:
        s,q=i.split("\n");
        fe.append(re+s)
    for url in fe:
        try:
            html = requests.get(url);
            if html.status_code == requests.codes.ok:
                print(url+": is open.")
        except:
            continue;

if __name__ == '__main__':
    Prepare();


