import urllib.parse
import urllib.request
import socket
import urllib.error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#urlopen 方法

# get 请求
# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

# post 请求

try:
	data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding="utf8")
	response = urllib.request.urlopen('http://httpbin.org/post',data = data,timeout=2)
	print(response.read())
except urllib.error.URLError as e:
	if isinstance(e.reason,socket.timeout):
		print("Time Out")

# Request 方法
request = urllib.request.Request('https://www.python.org')
responses = urllib.request.urlopen(request)
print(responses.read().decode('utf-8'))

