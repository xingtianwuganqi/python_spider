import requests
from lxml import etree

# url = 'https://bbs.hupu.com/wallpaper'
# detail_url = 'https://bbs.hupu.com/24288562.html'
def get_ten_page():
	arr = []
	for i in range(0,10):
		arr.append('https://bbs.hupu.com/wallpaper-'+str(i))
	return arr

def get_one_page(url):
	r = requests.get(url)
	if r.status_code == 200:
		return r.text
	return None

#xpath 取值
def xpath_message(text):
	# etree.HTML 将text 转成xpath 解析对象
	html = etree.HTML(text)
	# 获取 url, 帖子名称，帖子作者
	title = html.xpath('//li/div[@class="titlelink box"]/a/text()')
	title_url = html.xpath('//li/div[@class="titlelink box"]/a/@href')
	# author = html.xpath('//li/div[@class="author box"]/a[1]/text()')
	for i in range(0,len(title)):
		yield {
			'url': title_url[i],
			'title': title[i]
			# 'author': author[i]
		}

def get_detail(detail_urls):
	r = requests.get(detail_urls)
	if r.status_code == 200:
		return r.text
	return None

def get_detaile_message(html):
	html = etree.HTML(html)
	# 获取图片信息
	image = html.xpath('//p/img/@data-original')

	return image

def down_loadImg(img_url):
	try:
		img = ''
		if 'webp' in img_url:
			img = img_url.split('?')[0]
		else:
			img = img_url
		root = 'img//'
		path = img.split('/')[-1]
		response = requests.get(img)
		with open(root+path,'wb') as f:
			f.write(response.content)
	except Exception as e:
		print('下载失败')
		pass
	
	

def main():

	#  获取前十页的url
	arr_url = get_ten_page()
	for url in arr_url:
		print(url)
		html = get_one_page(url)
		messages = xpath_message(html)
		for article_url in messages:
			print(article_url)
			url = 'https://bbs.hupu.com'+article_url['url']
			detail_article = get_detail(url)
			images = get_detaile_message(detail_article)
			if len(images) > 0:
				for img in images:
					down_loadImg(img)
			else:
				print("没有图片")

if __name__ == "__main__":
	main()
