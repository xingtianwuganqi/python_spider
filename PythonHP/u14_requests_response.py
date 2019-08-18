import requests

r = requests.get('http://www.jianshu.com')
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)
print(type(r.history),r.history)

#内置的状态码查询对象
exit() if not r.status_code == requests.codes.ok else print("Request Successfully")