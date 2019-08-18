from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
from urllib.parse import urljoin




# url 的解析库， parse
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment',allow_fragments = False) #返回的是一个元组
print(type(result),result) 
print(result.scheme,result[0],result.netloc,result[1])


data = ['http','www.baidu.com','index.html','user','a=6','comment']#长度必须是6
print(urlunparse(data))

urlStr = 'http://www.baidu.com/index.html;user?id=5#comment'
response = urlsplit(urlStr) # 这个方法只会返回5个结果，也是元组
print(response)

date = ['http','www.baidu.com','index.html','a=6','comment'] # 长度必须为5
print(urlunsplit(date))

# urljoin
print(urljoin('http://www.baidu.com','FAQ.html'))
print(urljoin('http://www.baidu.com','https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com?wd=abc','https://cuiqingcai.com/index.html'))

