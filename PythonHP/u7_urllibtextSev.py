from urllib import request,error
import ssl

# 错误异常处理
try:
	ssl._create_default_https_context = ssl._create_unverified_context
	response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
	print(e.reason,e.code,e.headers)
except error.URLError as e:
	print(e.reason)
else:
	print('Request successfully')
