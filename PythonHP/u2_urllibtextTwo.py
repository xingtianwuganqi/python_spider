from urllib import request,parse 

url = 'http://httpbin.org/post'
header = {
	'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5; Windows NT)',
	'Host':'httpbin.org'
}
dicts = {
	'name': 'Germey'
}
data = bytes(parse.urlencode(dicts),encoding = 'utf8')
req = request.Request(url=url,data=data,headers=header,method='POST')#注意大小写
response = request.urlopen(req)
print(response.read().decode('utf-8'))