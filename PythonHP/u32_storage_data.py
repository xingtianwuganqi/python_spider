import requests
from pyquery import PyQuery as pq 
import json
import csv

# 爬取知乎热榜

# url = 'https://www.zhihu.com/explore'
# headers = {
# 	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
# }
# html = requests.get(url,headers=headers).text
# doc = pq(html)
# items = doc('.explore-tab .feed-item').items()
# for item in items:
# 	question = item.find('h2').text()
# 	author = item.find('.author-link').text()
# 	answer = pq(item.find('.content').html()).text()
# 	file = open('explore.text','a',encoding='utf-8')
# 	file.write('\n'.join([question,author,answer]))
# 	file.write('\n'+'=' * 50 + '\n')
# 	file.close()


# 读取 json
string = '''
[{
	"name": "baby",
	"gender": "male",
	"birthday": "1992-10-18"
},{
	"name": "Selina",
	"gender": "female",
	"birthday": "1995-3-4"
}]
'''
print(type(string))
data = json.loads(string)
print(type(data))
print(data)
print(data[0]["name"])
print(data[0].get('name'))
# print(data[0]["age"]) # 没有key的时候会报错
print(data[0].get('age',26)) # get 不会报错，还可以设置默认值

# 读取文件
with open('data.json','r') as file:
	json_str = file.read()
	data = json.loads(json_str)
	print(data)
	print(type(data))

# 输出json 

strings = '''
[{
	"name": "王伟",
	"gender": "男",
	"birthday": "1992-10-18"
},{
	"name": "Selina",
	"gender": "female",
	"birthday": "1995-3-4"
}]
'''
with open('jsonstr.json','w',encoding='utf-8') as file:
	file.write(json.dumps(strings,indent=2,ensure_ascii=False)) # indent 参数 表示 自动缩进2个字符 ensure_ascii 为false 还要设置文件输出的编码，才能显示为汉字

# csv 文件存储
with open('data.csv','w') as file:
	writer = csv.writer(file,delimiter=' ') #delimiter 用来修改分割符
	writer.writerow(['id','name','age'])
	writer.writerow(['100','bob','23'])
	writer.writerow(['101','tim','24'])
	writer.writerows([['102','a','25'],['103','b','26'],['104','c','27']])

# 写入字典
with open('datas.csv','w') as file:
	fieldnames = ['id','name','age']
	writer = csv.DictWriter(file,fieldnames=fieldnames)
	writer.writeheader()
	writer.writerow({'id': '101','name':'mike','age':'20'})
	writer.writerow({'id':'102','name':'jack','age':'22'})
	writer.writerows([{'id': '103','name':'a','age':'23'},{'id':'204','name':'b','age':'25'}])

# 读取
with open('data.csv','r') as file:
	reader = csv.reader(file)
	for row in reader:
		print(row)


