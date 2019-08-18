import requests
import re


#抓取网页
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'
}

r = requests.get('https://www.zhihu.com/explore',headers = headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*)</a>',re.S)
titles = re.findall(pattern,r.text)
print(titles)

#抓取二进制数据
r = requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)
# 保存数据
with open('favicon.ico','wb') as f: #第一个参数是文件名称，第二个参数代表以二进制写的形式打开，可以向文件里写入二进制数据
	f.write(r.content)
