import requests

r = requests.get('https://www.baidu.com')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

# 使用其他请求
r = requests.post('http://httpbin.org/post')
r = requests.put('http://httpbin.org/put')

#get 请求
r = requests.get('http://httpbin.org/get')
print(r.text)

# 添加参数
data = {
	'name': 'getmey',
	'age': 22
}
r = requests.get('http://httpbin.org/get',params = data)
print(r.text) #返回的是str类型
print(r.json()) #返回的是dict类型
print(type(r.text))
print(type(r.json()))
