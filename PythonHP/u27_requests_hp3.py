import requests
import re
import json
from PIL import Image
import os
import u25_requests_hp
import u26_requests_hp2



def down_image(url):
	u25 = u25_requests_hp.get_one_page(url)
	nameList = u25_requests_hp.get_name(u25)
	for name in nameList:
		url = 'https://bbs.hupu.com'+name['url']
		print(url)
		u26 = u26_requests_hp2.get_html(url)
		img_arr = u26_requests_hp2.get_image(u26) + u26_requests_hp2.get_twoImg(u26)
		if len(img_arr) > 0:
			for img in img_arr:
				u26_requests_hp2.download_img(img)
		else:
			print('没有图片')

def mains(number):

	url_arr = u25_requests_hp.get_number_page(number)
	for url in url_arr:
		down_image(url)
			





mains(10)