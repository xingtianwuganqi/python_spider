# encoding:utf-8
import requests
import json

# 找狗小程序
def getRescueList():
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
				if result['isFound'] == False and result['deleted'] == False:
					# print(result)
					content = {}
					content['title'] = result['title']
					content['id'] = result['id']
					content['content'] = result['description']
					content['imgs'] = result['images']
					content['address'] = result['address']
					content['updateTime'] = result['updateTime']
					url = "https://api.zuul.cuuhn.com/petsuu-gateway/find-pet-web/giveRise/getPlaceAdoptionDetail?id={}&sourceChannel=PLACE_ADOPTION_DETAIL&sourceChannelId=73886&find_pet_access_token=&loginPlugin=WEI_XIN_MINI_APP".format(result['id'])
					response = requests.get(url,headers=headers)
					detailInfo = json.loads(response.text)
					if detailInfo['success'] == True:
						content['weChatNumber'] = detailInfo['result']['weChatNumber']
					print(content)


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
		# print(dics)
		for dic in dics:
			# print(dic)
			# if dic['status'] == 0 and dic['price_status'] == 0:
			# 	print('==========-=========-----------')
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


'''
"is_deinsect" : true,
  "real_read_count" : 71,
  "is_immune" : false,
  "is_report" : false,
  "name" : "七一",
  "__v" : 0,
  "src_picture" : [

  ],
  "status" : 0,
  "avatar" : "https:\/\/thirdwx.qlogo.cn\/mmopen\/vi_32\/Q0j4TwGTfTIQS43ZoGWtCIsmEsDHZQ01pmlAY0ovu0xert1sTOertPwpavMZFz0SCDXibicAAVdDibiaf7AkmUia4mQ\/132",
  "city" : [
    "北京市",
    "北京市",
    "西城区"
  ],
  "is_sterilized" : false,
  "loc" : [
    116.40345764160156,
    39.898639678955078
  ],
  "recommand_count" : 0,
  "last_login" : "2021-07-25T06:06:09.952Z",
  "breeding" : "383977e8d8efd88cf33e71199cc37393",
  "desc" : "七一100周年救助于前门。\n所以取名为71 \n小姑娘，一摸就打呼噜。\n爱吃肉和主食罐，身体无敌健康。\n活泼可爱。",
  "openid" : "oxmi94lapAQJQ7026oAz6_VgBfVY",
  "gender" : 2,
  "age" : "0-3个月",
'''



if __name__ == "__main__":
	# getRescueList()
	dechongNetworking()













