import requests
import re
import json


url = 'https://bbs.hupu.com/selfie'
def get_number_page(number):
	url_arr = []
	for i in range(0,10):
		url_str = url + '-' + str(i)
		url_arr.append(url_str)

	return url_arr

# 获取html
def get_one_page(url):
	response = requests.get(url)
	if response.status_code == 200:
		return response.text
	return None

# 正则表达式删选出帖子名称与id
def get_name(html):
	#创建正则对象
	zz_str = '<li>.*?<div class="titlelink box".*?<a  href="(.*?)".*?>(.*?)</a>.*?<div class="author box".*?<a class="aulink".*?>(.*?)</a>.*?<span class="endauthor ">(.*?)<.*?</li>'
	pattern = re.compile(zz_str,re.S)
	items = re.findall(pattern,html)
	# print(items)

	for item in items:
		yield {
			'url':item[0],
			'name':item[1],
			'author':item[2],
			'endauthor': item[3]
		}


def write_file(content):
	# print(content)
	with open('hp.txt','a',encoding='utf-8') as f:
		f.write(json.dumps(content,ensure_ascii=False)+ '\n')

def main():
	html = get_one_page()
	# get_name(html)
	for item in get_name(html):
		write_file(item)

# main()