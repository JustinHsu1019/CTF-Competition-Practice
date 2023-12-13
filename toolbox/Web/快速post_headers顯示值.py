import requests
import base64
url="http://123.206.87.240:8002/web6/"
r=requests.session()
headers=r.get(url).headers#因为flag在消息头里
 
mid=base64.b64decode(headers['flag'])
print(mid)
mid=mid.decode()#为了下一步用split不报错，b64decode后操作的对象是byte类型的字符串，而split函数要用str类型的
print(mid)
flag = base64.b64decode(mid.split(':')[1])#获得flag:后的值
flag=flag.decode()
print(flag)
data={'margin':flag}
print (r.post(url,data).text)#post方法传上去
