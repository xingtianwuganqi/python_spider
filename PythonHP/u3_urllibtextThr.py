from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler,build_opener
from urllib.error import URLError

#验证登录名与密码

username = 'username'
password = 'password'
url = 'http://localhost:500/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
author_handler = HTTPBasicAuthHandler(p)
opener = build_opener(author_handler)

try:
	result = opener.open(url)
	html = result.read().decode('utf-8')
	print(html)
except URLError as e:
	print(e.reason)
