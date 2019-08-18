import requests 

#上传文件
file = {
	'file': open('favicon.ico','rb')
}
r = requests.post('http://httpbin.org/post',files = file)
print(r.text)