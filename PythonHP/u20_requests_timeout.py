import requests

r = requests.get('https://www.taobao.com',timeout = 1)
print(r.status_code)

#设置 连接和读取时间 时 可以传进去一个元组
s = requests.get('https://www.taobao.com',timeout = (5,11))
print(s.status_code)