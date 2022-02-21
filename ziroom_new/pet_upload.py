import requests
import json
import time

class petcity:
	bj = 'f3db5cb47b4d3d72dd664ccb00b0bf4d'
	sh = '1f256c188f41a114e7139faab3c38581'
	gz = '3f21b9934bfc2e38d81b52b9cb4aed75'
	sz = '774bbea00449957c7591ed6929f52fd7'

def petUploadNetworking(text):
	data = {
		'content': text['content'],
		'imgs': text['imgs'],
		'address_info': text['address_info'],
		'contact': text['contact'],
		'token': petcity.gz
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
	text =
	{
	'content': '\n名字：一点黑  \n性别：母  \n未免疫、未驱虫、未绝育  \n自家猫生的，有爱心小伙伴可以带回家自家猫生的，元旦节当天出生，活泼可爱，有想要养猫的小伙伴可以带它回家  \n领养要求：仅限同城无偿领养  \n坐标：广州市番禺区东乡村一节二巷3号',
	'imgs': 'https://petsuuu.oss-cn-beijing.aliyuncs.com/upload/2022-02-20/aaf25ef453754afb9358a2a6c58defbb.jpg,https://petsuuu.oss-cn-beijing.aliyuncs.com/upload/2022-02-20/7fb44ccd809343caadfb2b2fa9a98bea.jpg',
	'address_info': '广东省.广州市.番禺区',
	'contact': '微信：15914922341，请备注领养'
	}
	petUploadNetworking(text)










