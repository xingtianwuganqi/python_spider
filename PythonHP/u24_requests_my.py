import requests
import re
import json
import time

# 目标： 抓取100页猫眼电影
# url = 'http://maoyan.com/board'
#登录，获取网页内容
def get_one_page(url):
	header = {
		# 'Cookie' : '__mta=256859444.1541947622216.1541947712801.1541947714153.8; uuid_n_v=v1; uuid=A559D6D0E5C011E885B597D201E961B66EC6ED6E849D4A13AE8D805C64F665A8; _csrf=903e94057626bd78e2be55af08c89ee06fdc0192576b8be1f5a86e067d60b577; _lxsdk_cuid=167033d80dac8-0e0bf878a9225f-1e396652-13c680-167033d80dac8; _lxsdk=A559D6D0E5C011E885B597D201E961B66EC6ED6E849D4A13AE8D805C64F665A8; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; lt=x3J0-_k2SS6EypEmBv304GyK-5oAAAAAbAcAALYYKAGUEs---nmwKfmZvQVVbCsFX2ZazjqYJt8PpxuGF_2yFZZwNuVRBtG2dpHpBQ; lt.sig=9y4o24UwE9Z-rwE1-_uAnq9lcQI; __mta=256859444.1541947622216.1541947714153.1542122629280.9; _lxsdk_s=1670d9db1ab-b8e-825-e3%7C%7C11',
		# 'Host': 'www.maoyan.com',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
	}
	# session = requests.session()
	response = requests.get(url,headers = header)
	if response.status_code == 200:
		return response.text
	return None
#获取字典
def pase_one_page(html):
	string = '<dd>.*?board-index.*?>(.*?)</i>.*?title="(.*?)".*?<img data-src="(.*?)".*?<p.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>'
	pattern = re.compile(string,re.S)
	items = re.findall(pattern,html)
	print(items)
	for item in items:
		yield {
			'index':item[0],
			'name': item[1],
			'img':item[2].strip(),
			'time':item[3] 
		}
#将内容写到文件中
def write_to_file(content):
	with open('moyan.txt','a',encoding='utf-8') as f:
		print(type(json.dumps(content)))
		f.write(json.dumps(content,ensure_ascii=False)+ '\n')

def main(offset):
	url = 'http://maoyan.com/board/4?offset='+str(offset)
	html = get_one_page(url)
	for item in pase_one_page(html):
		write_to_file(item)

if __name__ == '__main__':
	for i in range(10):
		main(offset=i * 10)
		time.sleep(1)

