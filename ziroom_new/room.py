import requests
from lxml import etree
import re
import time

class room():

	def __init__(self):
		self.base_url = "http://www.ziroom.com/z/?qwd="

	def get_room_url(self,page,keyword):
		return "http://www.ziroom.com/z/z0-p" + page + "/?qwd=" + keyword

	def get_room_list(self,keyword):

		url = self.base_url + keyword
		header = {
			"Cookie": "gr_user_id=50a1f284-ab84-461f-a0b4-867c84bd2333; CURRENT_CITY_CODE=110000; CURRENT_CITY_NAME=%E5%8C%97%E4%BA%AC; _csrf=n07g6yW5fObcficAk5MpKBfrlduFngOg; Hm_lvt_4f083817a81bcb8eed537963fc1bbf10=1565276201,1565276302,1565623003; gr_session_id_8da2730aaedd7628=34514efc-4677-470e-990a-fd7dd9afa5ee; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216c71bb5f1c132-0efbe2ac915ae5-37657e03-1296000-16c71bb5f1d180%22%2C%22%24device_id%22%3A%2216c71bb5f1c132-0efbe2ac915ae5-37657e03-1296000-16c71bb5f1d180%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22cpc%22%2C%22%24latest_utm_campaign%22%3A%22PC-ZFJHBJ41%22%2C%22%24latest_utm_content%22%3A%22ZFDYBJ17721%22%2C%22%24latest_utm_term%22%3A%22%E8%87%AA%E5%A6%82%22%7D%7D; gr_session_id_8da2730aaedd7628_34514efc-4677-470e-990a-fd7dd9afa5ee=true; Hm_lpvt_4f083817a81bcb8eed537963fc1bbf10=1565623007",
			"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
		}
		print(url)
		request = requests.get(url,headers = header)
		if request.status_code == 200:
			# print(request.text)
			return request.text
		else:
			# print(request.status_code)
			return None

	def get_room_lists(self,url,keyword):

		url = url + keyword
		header = {
			"Cookie": "gr_user_id=50a1f284-ab84-461f-a0b4-867c84bd2333; CURRENT_CITY_CODE=110000; CURRENT_CITY_NAME=%E5%8C%97%E4%BA%AC; _csrf=n07g6yW5fObcficAk5MpKBfrlduFngOg; Hm_lvt_4f083817a81bcb8eed537963fc1bbf10=1565276201,1565276302,1565623003; gr_session_id_8da2730aaedd7628=34514efc-4677-470e-990a-fd7dd9afa5ee; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216c71bb5f1c132-0efbe2ac915ae5-37657e03-1296000-16c71bb5f1d180%22%2C%22%24device_id%22%3A%2216c71bb5f1c132-0efbe2ac915ae5-37657e03-1296000-16c71bb5f1d180%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22cpc%22%2C%22%24latest_utm_campaign%22%3A%22PC-ZFJHBJ41%22%2C%22%24latest_utm_content%22%3A%22ZFDYBJ17721%22%2C%22%24latest_utm_term%22%3A%22%E8%87%AA%E5%A6%82%22%7D%7D; gr_session_id_8da2730aaedd7628_34514efc-4677-470e-990a-fd7dd9afa5ee=true; Hm_lpvt_4f083817a81bcb8eed537963fc1bbf10=1565623007",
			"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
		}
		print(url)
		request = requests.get(url,headers = header)
		if request.status_code == 200:
			# print(request.text)
			return request.text
		else:
			# print(request.status_code)
			return None

	def get_page_number(self, html): # 获取页数
		room_page = '共(.*?)页'
		all_page = re.compile(room_page, re.S).findall(html)
		return all_page[0]

	def xpath_list(self,text):
		html = etree.HTML(text)
		# 选取了这一页全部的item
		hource_list = html.xpath("//div[@class='Z_list']/div[@class='Z_list-box']/div[@class='item']")
		# print(hource_list)
		items = item()
		for i in hource_list:
			pic = i.xpath("./div[@class='pic-box']/a/img/@data-original")
			if len(pic) > 0:
				items.pic = "http:"+pic[0]
			title = i.xpath("./div[@class='info-box']/h5/a/text()")
			if len(title) > 0:
				items.title_sign = title[0]
			desc = i.xpath("./div[@class='info-box']/div[@class='desc']/div[1]/text()")
			print(desc)
			description  = i.xpath("./div[@class='info-box']/div[@class='desc']/div[@class='location']/text()")
			if len(desc) > 0:
				descrip = desc[0] + "," + description[0]
				items.desc = descrip.replace(" ","").replace("\t","").replace("\n","")
			tag = i.xpath("./div[@class='info-box']/div[@class='tag']/span[1]/text()")
			tag2 = i.xpath("./div[@class='info-box']/div[@class='tag']/span[2]/text()")
			tag3 = i.xpath("./div[@class='info-box']/div[@class='tag']/span[3]/text()")
			if len(tag) > 0:
				items.tag = tag[0] + "、" + tag2[0] + "、" + tag3[0]

			tips = i.xpath("./div[@class='info-box']/div[contains(@class,'tips')]/text()")
			if len(tips) > 0 :
				tip_str = tips[0].replace(" ","").replace("\t","").replace("\n","")
				items.tips = tip_str
			price = i.xpath("./div[@class='info-box']/div[@class='price']/span[@class='num']/@style")
			if len(price) > 0:
				items.price = self.get_room_price(price[0])
			# 获取价格数字的像素
			all_num = i.xpath("./div[@class='info-box']/div[@class='price']/span[@class='num']")

			nums = ""
			for j in all_num:
				num = j.xpath("./@style")
				nums = nums + self.get_room_num(num[0]) + ","

			yield {
				'hource_img' : items.pic,
				'hource_title': items.title_sign,
				'hource_desc' : items.desc,
				'hource_tag'  : items.tag,
				'hource_tips' : items.tips,
				'hource_price_img' : items.price,
				'hource_price_num' : nums
			}

	def get_room_price(self,html):
		# 正则表达式
		room_price_pat= "background-image: url\((.*?)\);"
		price = re.compile(room_price_pat,re.S).findall(html)
		return "http:"+price[0]

	def get_room_num(self,html): # 房子的价格
		room_price_pat = 'background-position: (.*?)px'
		num = re.compile(room_price_pat,re.S).findall(html)
		return num[0]

class item():

	def __init__(self):
		self.pic = ""
		self.title_sign = ""
		self.desc = ""
		self.tag = ""
		self.tips = ""
		self.price = ""

if __name__ == "__main__":
	room = room()
	list_text = room.get_room_list('古城')
	room_page = room.get_page_number(list_text)
	print(type(room_page))

	for i in range(1,int(room_page)+1):
		time.sleep(5)
		room_url = room.get_room_url(str(i),"古城")
		room_list = room.get_room_lists(room_url,"古城")
		room_detail = room.xpath_list(list_text)
		# print(list(room_detail))
		for i in room_detail:
			print(i)