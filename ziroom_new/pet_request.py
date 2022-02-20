# encoding:utf-8
import requests
import json
import time


# 找狗小程序
def zhaogouNetworking(city):
	'''
	https://api.zuul.cuuhn.com/petsuu-gateway/find-pet-web/giveRise/getPlaceAdoptionDetail?id=73886&sourceChannel=PLACE_ADOPTION_DETAIL&sourceChannelId=73886&find_pet_access_token=&loginPlugin=WEI_XIN_MINI_APP
	标题，内容，图片，联系方式，位置
	'''

	'''
	areaId: 
	52 北京
	321 上海
	76 广州
	西安 311
	深圳 77
	'''
	areaId = ''
	if city == '北京市':
		areaId = 52

	if city == '上海市':
		areaId = 321

	if city == '广州市':
		areaId = 76

	if city == '西安市':
		areaId = 311

	headers = {'Content-Type': 'application/json'}
	# 列表
	list_url = 'https://api.zuul.cuuhn.com/petsuu-gateway/find-pet-web/giveRise/searchPlaceAdoptionList?location=&page=1&pageSize=10&screenCondition=0&petType=0&areaId={}&find_pet_access_token=&loginPlugin=WEI_XIN_MINI_APP'.format(areaId)
	list_res = requests.get(list_url,headers=headers)
	if list_res.status_code == 200:
		dic = json.loads(list_res.text)
		# print(dic)
		if dic['success'] == True:
			results = dic['result']['content']
			for result in results:
				detail_url='https://api.zuul.cuuhn.com/petsuu-gateway/find-pet-web/giveRise/getPlaceAdoptionDetail?id={}&sourceChannel=PLACE_ADOPTION_DETAIL&sourceChannelId={}&find_pet_access_token=&loginPlugin=WEI_XIN_MINI_APP'.format(result['id'],result['id'])
				detail_res = requests.get(detail_url)
				if detail_res.status_code == 200:
					detail_dic = json.loads(detail_res.text)['result']
					if detail_dic['requireMaintenanceLabelName'] == '无偿领养':
						content = {}
						content['name'] = detail_dic['name'] 
						content['age'] = detail_dic['age']
						content['gender'] = detail_dic['sex']
						content['petBreedType'] = detail_dic['petBreedType']
						content["putTime"] = detail_dic['putTime']
						content['title'] = detail_dic['title']
						content['content'] = detail_dic['title'] + detail_dic['description']
						content['address'] = detail_dic['address']
						content['wechat'] = detail_dic['weChatNumber']
						content['cityMaintenanceLabelName'] = detail_dic['cityMaintenanceLabelName']
						content['requireMaintenanceLabelName'] = detail_dic['requireMaintenanceLabelName']
						content['require'] = detail_dic['cityMaintenanceLabelName'] + detail_dic['requireMaintenanceLabelName']
						content['phone'] = ''
						content['imgs'] = detail_dic['images']
						content['is_deinsect'] = False
						content['is_immune'] = False
						content['is_sterilized'] = False
						content['address_info'] =  detail_dic['cityMaintenanceLabelName'] + "." + detail_dic['requireMaintenanceLabelName']
						print('create_time',detail_dic['putTime'])
						print(content)
						time.sleep(3)
						createMarkDown(content)

# 得宠小程序
def dechongNetworking(text):
	url = 'https://app.dechongtech.com/api/publish'
	data = {
		'price_status': 0,
		'city': [text],
		'page': 1
	}
	headers = {"Host": "app.dechongtech.com",
		"Connection": "keep-alive",
		"Content-Length": "48",
		"content-type": "application/json",
		"authorization": "Jy1nY+JIPf94jYGzyjr7cPxLIkdJXcTuLcQ+fpBR/Gnsigbd+2C50qHr1Tv2CV87NbL7bJhReVqEG7yaI0njjHsEuTDR7Xdhx3OhDtOZ6tK1WZLP3zR5r7J8SiSA1QI2xBuPSMlgWW7XPFKVKaDI1Q==",
		"Accept-Encoding": "gzip,compress,br,deflate",
		"User-Agent":"Mozilla/5.0(iPhone;CPUiPhoneOS14_7likeMacOSX)AppleWebKit/605.1.15(KHTML,likeGecko)Mobile/15E148MicroMessenger/8.0.9(0x18000927)NetType/4GLanguage/zh_CN",
		"Referer": "https://servicewechat.com/wxe4967ef8dbd8d13b/55/page-frame.html",
	}
	response = requests.post(url,data=json.dumps(data),headers=headers)
	# print(response.text)
	if response.status_code == 200: 
		dics = json.loads(response.text)
		for dic in dics:
			content = {}
			if dic['status'] == 0 and dic['price_status'] == 0:
				content['content'] = dic['desc']
				content['imgs'] = dic['picture']
				address=''
				for i in dic['city']:
					address = address+i
				content['address'] = address
				content['wechat'] = dic['wechat']
				content['phone'] = dic['phone']
				content['createTime'] = dic['create_at'] 
				detail_url = 'https://app.dechongtech.com/api/publish/detail/{}'.format(dic['item_id'])
				detail_res = requests.get(detail_url)
				if detail_res.status_code == 200:
					detailDic = json.loads(detail_res.text)
					content['require'] = detailDic['require'] # 要求
					content['name'] = detailDic['name']
					if 'gender' in detailDic.keys():
						content['gender'] = detailDic['gender'] # 1公 2母
					if 'is_deinsect' in detailDic.keys():
						content['is_deinsect'] = detailDic['is_deinsect'] # 驱虫
					else:
						content['is_deinsect'] = False

					if 'is_immune' in detailDic.keys():
						content['is_immune'] = detailDic['is_immune'] # 免疫
					else:
						content['is_immune'] = False
					if 'is_sterilized' in detailDic.keys():
						content['is_sterilized'] = detailDic['is_sterilized'] # 绝育
					else:
						content['is_sterilized'] = False

				print('create_time',dic['create_at'])
				print(content)
				time.sleep(3)
				createMarkDown(content)

def chongwubangNetworking(city):
	url = 'https://app.petbang2014.com/adopt-api/adopt/page'
	data = {
	  "pageIndex" : 1,
	  "pageSize" : "10",
	  "city" : city,
	  "type" : ""
	}
	headers = {
		'Host': 'app.petbang2014.com',
		# 'Connection': 'keep-alive',
		'Connection': 'close',
		'Content-Length': '120',
		'thirdSession': '1d9eb21a-d3be-4a10-a2a2-0fa5d50926e6',
		'content-type': 'application/json',
		'Accept-Encoding': 'gzip,compress,br,deflate',
		# 'User-Agent': 'User-Agent:Mozilla/5.0',
		# 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.9(0x1800092c) NetType/WIFI Language/zh_CN',
		# 'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
		'User-Agent': 'Mozilla/5.0(iPhone;CPUiPhoneOS14_7_1likeMacOSX)AppleWebKit/605.1.15(KHTML,likeGecko)Mobile/15E148MicroMessenger/8.0.9(0x1800092c)NetType/WIFILanguage/zh_CN',
		'Referer': 'https://servicewechat.com/wxa027f226179d34a5/226/page-frame.html'
	}
	response = requests.post(url,data=json.dumps(data),headers=headers)
	if response.status_code == 200:
		dics = json.loads(response.text)
		arr = dics['data']['records']
		print(len(arr))
		if len(arr) > 0:
			for i in range(0,len(arr)):
				print('petttttttttttttttid',arr[i]['id'])
				id = arr[i]['id']
				detail_url = 'https://app.petbang2014.com/adopt-api/adopt/detail?id={}'.format(id)
				detail_res = requests.get(detail_url)
				if detail_res.status_code == 200:
					detail_dic = json.loads(detail_res.text)['data']
					if detail_dic['price'] is None and detail_dic['status'] == 0:
						content = {}
						content['name'] = detail_dic['nickName']
						content['gender'] = 1 if detail_dic['sex'] == "男孩" else 2
						content['age'] = detail_dic['age']
						content['is_sterilized'] = True if detail_dic['isBorn'] == 1 else False # 已绝育
						content['is_deinsect'] = True if detail_dic['isVaccine'] == 1 else False # 已免疫
						content['is_immune'] = True if detail_dic['isParasite'] == 1 else False # 已驱虫
						content['content'] = detail_dic['description']
						content['address'] = detail_dic['city'] + detail_dic['address']
						content['city'] = detail_dic['city']
						content['location'] = detail_dic['address']
						content['img'] = detail_dic['img']
						content['img1'] = detail_dic['img1']
						content['img2'] = detail_dic['img2']
						content['createTime'] = detail_dic['createTime']
						content['phone'] = detail_dic['user']['mobile']
						content['wechat'] = detail_dic['user']['weixin']
						content['address'] = detail_dic['city'] + "." + detail_dic['address']
						adoptConditions = ''
						adopts = detail_dic['adoptConditions']
						if len(adopts) > 0:
							for j in range(0,len(adopts)):
								ad = adopts[j]
								adoptConditions = adoptConditions + ad['condition']
						content['require'] = adoptConditions
						imgs = []
						if len(detail_dic['img']) > 0:
							imgs.append(detail_dic['img'])
						if detail_dic['img1'] != None:
							imgs.append(detail_dic['img1'])
						if detail_dic['img2'] != None:
							imgs.append(detail_dic['img2'])
						content['imgs'] = imgs
						print('create_time',detail_dic['createTime'])
						print(content)
						createMarkDown(content)
						time.sleep(5)
				else:
					print(detail_res)
		else:
			print('============-----------=============')
				# if pet['isFree'] == 0 and pet['']

def jiuzhuquan(city):
	header = {'Content-Type': 'application/json'}
	list_url = "https://www.jzqlyptall.com/api/adopts/index?page=1&pageSize=10&city={}&category_id=0&pet_sex=0&age_stage=0&body_id=0&hair_id=0&vaccine_id=0&sterilize_id=0&expelling_parasite_id=0".format(city)
	response = requests.get(list_url,headers=header)
	if response.status_code == 200:
		dic = json.loads(response.text)
		if dic['code'] == 1:
			list_data = dic['data']['list']
			if len(list_data) > 0:
				for first in list_data:
					id = first['id']
					print(id)
					detail_head={
						'Host': 'www.jzqlyptall.com',
						'Connection': 'keep-alive',
						'content-type': 'application/json',
						'access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo4MTYyLCJpc3MiOiJodHRwOlwvXC93d3cubGluZ3Nlci5jblwvIiwiYXVkIjoicWlhb2hhbyIsImlhdCI6MTY0MDMzMjg2MiwibmJmIjoxNjQwMzMyODYyLCJleHAiOjE2NDA5Mzc2NjJ9.x0Jmns-MpHcV0hH6hGLz-cii6ZPzb1KddcDx6eQqY_s',
						'Accept-Encoding': 'gzip,compress,br,deflate',
						'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.16(0x1800102c) NetType/WIFI Language/zh_CN',
						'Referer': 'https://servicewechat.com/wx6a6c625ab3a2bc10/24/page-frame.html'
					}
					detail_url = 'https://www.jzqlyptall.com/api/adopts/detail?id={}'.format(id)
					detail_response = requests.get(detail_url,headers=detail_head)
					if detail_response.status_code == 200:
						detail_detail = json.loads(detail_response.text)
						if detail_detail['code'] == 1:
							print(detail_detail['msg'])
							detail_data = detail_detail['data']
							if detail_data['status'] == 1 and detail_data['pay_or_free'] == 1:
								content = {}
								content['name'] = detail_data['pet_nickname']
								content['gender'] = detail_data['pet_sex']
								content['age'] = detail_data['age']
								content['address'] = detail_data['location']
								content['province'] = detail_data['province']
								content['city'] = detail_data['city']
								content['location'] = detail_data['location']
								content['district'] = detail_data['district']
								content['content'] = detail_data['story']
								content['phone'] = detail_data['mobile']
								content['wechat'] = detail_data['wechat']
								content['create_time'] = detail_data['create_time']
								content['vaccine'] = detail_data['vaccine']
								content['is_deinsect'] = True if detail_data['vaccine_id'] == 1 else False
								content['is_immune'] = True if detail_data['expelling_parasite_id'] == 1 else False
								content['is_sterilized'] = True if detail_data['sterilize_id'] == 1 else False
								content['sterilize'] = detail_data['sterilize']
								content['expelling_parasite'] = detail_data['expelling_parasite']
								content['body'] =  detail_data['body']
								content['hair'] = detail_data['hair']
								content['require'] = '，'.join(detail_data['adopt_requirements_list'])
								# print('--------',content['carousel'])
								imgUrls = []
								for img in detail_data['carousel']:
									url = img['attachment']
									if len(url) > 0:
										imgUrls.append(url)
								content['imgs'] = imgUrls
								print('create_time',detail_data['create_time'])
								print(content)
								createMarkDown(content)
								time.sleep(5)
						else:
							print(detail_detail['msg'])
							time.sleep(5)


def createMarkDown(dic):

	img_str = ''
	for i in dic['imgs']:
		img_url = '![]({})'.format(i) + '  '
		img_str = img_str + img_url
	mark_str = '''
## 猫咪找领养！ 坐标{}
>名字：{}  
性别：{}  
{}、{}、{}  
{}  
领养要求：{}  
坐标：{}  
微信：{}  
请备注领养  
电话：{}  
**回复1396获取联系方式**  
{}
'''.format(
		dic['address'],
		dic['name'],
		("公" if dic['gender'] == 1 else "母"),
		('已免疫' if dic['is_deinsect'] == True else '未免疫'),
		("已驱虫" if dic['is_immune'] == True else "未驱虫"),
		('已绝育' if dic['is_sterilized'] == True else '未绝育'),
		dic['content'],
		dic['require'],
		dic['address'],
		dic['wechat'],
		dic['phone'],
		img_str)
	print(mark_str)
	print('uploadData is ========================')
	# 更新到服务器

	upload_content = '''
名字：{}  
性别：{}  
{}、{}、{}  
{}  
领养要求：{}  
坐标：{}'''.format(
		dic['name'],
		("公" if dic['gender'] == 1 else "母"),
		('已免疫' if dic['is_deinsect'] == True else '未免疫'),
		("已驱虫" if dic['is_immune'] == True else "未驱虫"),
		('已绝育' if dic['is_sterilized'] == True else '未绝育'),
		dic['content'],
		dic['require'],
		dic['address'],
		)

	upload_contact = '微信：{}，请备注领养'.format(dic['wechat'])
	upload_img = ",".join(dic['imgs'])
	upload_address = dic['address']
	upload_dic = {
		'content': upload_content,
		'imgs': upload_img,
		'address_info': upload_address,
		'contact': upload_contact
	}
	print(upload_dic)
	print('=====================================')

if __name__ == "__main__":
	# zhaogouNetworking('北京市')
	# zhaogouNetworking('广州市')
	# chongwubangNetworking('北京市')
	# chongwubangNetworking('上海市')
	# chongwubangNetworking('广州市')
	dechongNetworking('北京市')
	# dechongNetworking('上海市')
	# dechongNetworking('广州市')
	# dechongNetworking('昆明市')
	# jiuzhuquan('北京市')
	# jiuzhuquan('上海市')
	# jiuzhuquan('广州市')




	













