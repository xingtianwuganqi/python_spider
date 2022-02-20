import requests
import json
import time

def petUploadNetworking(text):
	data = {
		'content': text['content'],
		'imgs': text['imgs'],
		'address_info': text['address_info'],
		'contact': text['contact'],
		'token': '2acc94559fdb6ef6a6d630d345f2580b'
	}
	headers = {'Content-Type': 'application/json'}
	url = 'https://test.rxswift.cn/api/v1/releasetopic/'
	print('data',json.dumps(data))
	response = requests.post(url,headers=headers,data=json.dumps(data))
	if response.status_code == 200:
		print('success')
	else:
		print(response.status_code)
		print('error')


if __name__ == "__main__":
	text = {'content': '\n>名字：流二代小橘猫  \n性别：母  \n未免疫、未驱虫、未绝育  \n流二代小橘猫找主人要求如下\n1.不吃毒猫粮，喂健康猫粮\n2.封窗，不散养，不笼养\n3.打妙三多猫三联，适龄绝育\n4.经济稳定，猫生病要去看病\n5.希望有责任心，把猫当成家里的一份子，尊重生命，不随意遗弃宠物或虐猫践踏生命！  \n领养要求：仅限同城无偿领养  \n坐标：广东省广州市白云区望岗西胜街1号    \n', 'imgs': 'https://petsuuu.oss-cn-beijing.aliyuncs.com/upload/2022-02-17/8c155558b22b48528d9811e2a4a14224.jpg', 'address_info': '广东省广州市白云区望岗西胜街1号', 'contact': '微信：17520094467，请备注领养'}
	petUploadNetworking(text)










