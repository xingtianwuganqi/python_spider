# encoding:utf-8
import requests
import json
import time


# 找狗小程序
def zhaogouNetworking():
	'''
	https://api.zuul.cuuhn.com/petsuu-gateway/find-pet-web/giveRise/getPlaceAdoptionDetail?id=73886&sourceChannel=PLACE_ADOPTION_DETAIL&sourceChannelId=73886&find_pet_access_token=&loginPlugin=WEI_XIN_MINI_APP
	标题，内容，图片，联系方式，位置
	'''
	headers = {'Content-Type': 'application/json'}
	# 列表
	list_url = 'https://api.zuul.cuuhn.com/petsuu-gateway/find-pet-web/giveRise/searchPlaceAdoptionList?location=&page=1&pageSize=10&screenCondition=0&petType=0&areaId=52&find_pet_access_token=&loginPlugin=WEI_XIN_MINI_APP'
	list_res = requests.get(list_url,headers=headers)
	if list_res.status_code == 200:
		dic = json.loads(list_res.text)
		# print(dic)
		if dic['success'] == True:
			results = dic['result']['content']
			# print(results)
			for result in results:
				detail_url='https://api.zuul.cuuhn.com/petsuu-gateway/find-pet-web/giveRise/getPlaceAdoptionDetail?id={}&sourceChannel=PLACE_ADOPTION_DETAIL&sourceChannelId={}&find_pet_access_token=&loginPlugin=WEI_XIN_MINI_APP'.format(result['id'],result['id'])
				detail_res = requests.get(detail_url)
				if detail_res.status_code == 200:
					detail_dic = json.loads(detail_res.text)['result']
					if detail_dic['requireMaintenanceLabelName'] == '无偿领养':
						content = {}
						content['nickname'] = detail_dic['name'] 
						content['age'] = detail_dic['age']
						content['petBreedType'] = detail_dic['petBreedType']
						content["putTime"] = detail_dic['putTime']
						content['title'] = detail_dic['title']
						content['description'] = detail_dic['description']
						content['address'] = detail_dic['address']
						content['weChatNumber'] = detail_dic['weChatNumber']
						content['cityMaintenanceLabelName'] = detail_dic['cityMaintenanceLabelName']
						content['requireMaintenanceLabelName'] = detail_dic['requireMaintenanceLabelName']
						print(content)
					

# 得宠小程序
def dechongNetworking():
	url = 'https://app.dechongtech.com/api/publish'
	data = {
		'price_status': 0,
		'city': ['北京市'],
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
					if 'is_immune' in detailDic.keys():
						content['is_immune'] = detailDic['is_immune'] # 免疫
					if 'is_sterilized' in detailDic.keys():
						content['is_sterilized'] = detailDic['is_sterilized'] # 绝育
			print(content)

def chongwubangNetworking():
	url = 'https://app.petbang2014.com/adopt-api/adopt/page'
	data = {
	  "pageIndex" : 1,
	  "pageSize" : "10",
	  "city" : "北京市",
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
				time.sleep(5)
				print('petttttttttttttttid',arr[i]['id'])
				id = arr[i]['id']
				detail_url = 'https://app.petbang2014.com/adopt-api/adopt/detail?id={}'.format(id)
				detail_res = requests.get(detail_url)
				if detail_res.status_code == 200:
					detail_dic = json.loads(detail_res.text)['data']
					if detail_dic['price'] is None and detail_dic['status'] == 0:
						content = {}
						content['nickName'] = detail_dic['nickName']
						content['sex'] = detail_dic['sex']
						content['age'] = detail_dic['age']
						content['isBorn'] = detail_dic['isBorn'] # 已绝育
						content['isVaccine'] = detail_dic['isVaccine'] # 已免疫
						content['isParasite'] = detail_dic['isParasite'] # 已驱虫
						content['content'] = detail_dic['description']
						content['city'] = detail_dic['city']
						content['address'] = detail_dic['address']
						content['img'] = detail_dic['img']
						content['img1'] = detail_dic['img1']
						content['img2'] = detail_dic['img2']
						content['createTime'] = detail_dic['createTime']
						content['mobile'] = detail_dic['user']['mobile']
						content['weixin'] = detail_dic['user']['weixin']
						adoptConditions = ''
						adopts = detail_dic['adoptConditions']
						if len(adopts) > 0:
							for j in range(0,len(adopts)):
								ad = adopts[j]
								adoptConditions = adoptConditions + ad['condition']
						content['adoptConditions'] = adoptConditions
						print(content)
				else:
					print(detail_res)
		else:
			print('============-----------=============')
				# if pet['isFree'] == 0 and pet['']



if __name__ == "__main__":
	zhaogouNetworking()
	# dechongNetworking()
	# chongwubangNetworking()













