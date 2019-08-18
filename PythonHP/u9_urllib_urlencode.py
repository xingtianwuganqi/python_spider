from urllib.parse import urlencode
from urllib.parse import parse_qs
from urllib.parse import parse_qsl
from urllib.parse import quote
from urllib.parse import unquote

params={
	'name':'germey',
	'age':22
}

base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

#反序列化
query = 'name=germey&age=22'
print(parse_qs(query))

#将参数转换成元组组成的列表
query = 'name=germey&age=22'
print(parse_qsl(query))

#将中文字符转换成url编码
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)

#进行url解码
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))


