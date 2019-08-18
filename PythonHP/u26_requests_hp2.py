import requests
import re
import json
import random
import time

url = "https://bbs.hupu.com/24447294.html"
def get_html(url):
	response = requests.get(url)
	if response.status_code == 200:
		return response.text
	return None

# 创建正则表达式


#获取前两个图片
def get_twoImg(html):
	 #"<p><img src="https://i11.hoopchina.com.cn/hupuapp/bbs/215626891194387/thread_215626891194387_20181120161801_s_302137_w_1080_h_1350_54668.jpg?x-oss-process=image/resize,w_800/format,webp" data-w="1080" data-h="1350"/ data-imgid="e69d1ab81a3a2e66f64073c0f80e1517"></p>"
	zz_str = '<p><img src="(.*?)".*?></p>'
	pattern = re.compile(zz_str,re.S)
	items = re.findall(pattern,html)
	# print(type(items))
	# print(items)
	arr = []
	if len(items) > 0:
		for item in items:
			arr.append(item)
		# print(arr)
		return arr
	else:
		print('没有图片')
		return []

def get_image(html):
	print('get_image++++++++')
	#<p><img src="https://i1.hoopchina.com.cn/hupuapp/bbs/215626891194387/thread_215626891194387_20181120161802_s_360577_w_1200_h_1500_80803.jpg?x-oss-process=image/resize,w_800/format,webp" data-w="1200" data-h="1500"/ data-imgid="579ca5b7e9c32935a49a37c61bb9c888"></p>
	zz_str = '<p><img src="(.*?)" data-original="(.*?)".*?</p>'
	pattern = re.compile(zz_str,re.S)
	items = re.findall(pattern,html)
	# print(type(items))
	# print(items)
	arr = []
	if len(items) > 0:
		for item in items:
			arr.append(item[1])
		# print(arr)
		return arr
	else:
		print('没有图片')
		return []


def download_img(img_url):
	try:
		if 'webp' in img_url:
			img_url = img_url.split('?')[0]
		if 'placeholder' in img_url:
			return

		img = requests.get(img_url)
		if img.status_code == 200:

			root = 'image//'
			path = img_url.split("/")[-1]
			with open(root+path,'wb') as f:
				f.write(img.content)
		else:
			print(img.status_code)
	except Exception as ex:
		print('---出错继续---')
		pass

def main():
	html = get_html(url)
	# print(html)
	arr = get_twoImg(html)
	array = arr + get_image(html)
	# print(array)
	for i in array:
		download_img(i)
	
# main()