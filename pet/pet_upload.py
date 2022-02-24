# -*- coding: utf-8 -*-
import requests
import json
import time

class petcity:
	bj = 'f3db5cb47b4d3d72dd664ccb00b0bf4d'
	sh = '1f256c188f41a114e7139faab3c38581'
	gz = '3f21b9934bfc2e38d81b52b9cb4aed75'
	sz = '774bbea00449957c7591ed6929f52fd7'

def petUploadNetworking(citytoken,text):
	data = {
		'tags': '1,9',
		'content': text['content'],
		'imgs': text['imgs'],
		'address_info': text['address_info'],
		'contact': text['contact'],
		'token': citytoken
	}
	headers = {'Content-Type': 'application/json'}
	url = 'https://rescue.rxswift.cn/api/v1/releasetopic/'
	print('data',json.dumps(data))
	response = requests.post(url,headers=headers,data=json.dumps(data))
	if response.status_code == 200:
		print('success')
	else:
		print(response.status_code)
		print('error')


if __name__ == "__main__":
	## 确保修改 城市 address_info 字段
	## 图片不能太长
	citytoken = petcity.sh
	text = {'content': '\n名字：长毛美美  \n性别：母  \n已免疫、已驱虫、已绝育  \n长毛三花妹妹，1岁，粉鼻粉爪，浓郁的长毛，毛色柔软，极漂亮，极其亲人，超喜欢撸撸！已经驱虫、刚绝育（照片是绝育术后），身体健康！非常乖，粘人精，有眼缘的赶紧把她带回家吧。\n领养要求：有病就治、按时驱虫、打疫苗，科学喂养，不离不弃，接受回访。限上海无偿领养。有意加微信。  \n领养要求：有病就治、按时驱虫、打疫苗，科学喂养，不离不弃，接受回访。限上海无偿领养。有意加微信。  \n坐标：上海市上海市黄浦区', 'imgs': 'https://dechong.oss-cn-qingdao.aliyuncs.com/publish_pic/oxmi94g8LCAL-irAzeGN9VKqZXKg_1645709819596_1affc114963f.jpg,https://dechong.oss-cn-qingdao.aliyuncs.com/publish_pic/oxmi94g8LCAL-irAzeGN9VKqZXKg_1645709820877_8ebbddfc9b58.jpg', 'address_info': '上海.上海市.黄浦区', 'contact': '微信：13601619440，请备注领养'}
	petUploadNetworking(citytoken, text)










