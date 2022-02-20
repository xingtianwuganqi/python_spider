import requests
import json
import time

def petUploadNetworking(text):
	data = {
		'content': text['content'],
		'imgs': text['imgs'],
		'address_info': text['address_info'],
		'contact': text['contact'],
		'token': 'f3db5cb47b4d3d72dd664ccb00b0bf4d'
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
	text = {'content': '名字：虎皮美短  \n性别：公  \n已免疫、已驱虫、未绝育  \n可爱温顺粘人  \n领养要求：找个喜欢猫，靠谱的家人，无偿领养，  \n坐标：北京市北京市顺义区', 'imgs': 'https://dechong.oss-cn-qingdao.aliyuncs.com/publish_pic/oxmi94qnrPvflNz1BY4mS5_FC_Ys_1645360324198_6dd69ca43ee3.jpg,https://dechong.oss-cn-qingdao.aliyuncs.com/publish_pic/oxmi94qnrPvflNz1BY4mS5_FC_Ys_1645360324526_2d2a204d298d.jpg', 'address_info': '北京.北京市.顺义区', 'contact': '微信：15711019201，请备注领养'}
	petUploadNetworking(text)










