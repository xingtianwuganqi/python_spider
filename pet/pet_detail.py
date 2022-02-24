# -*- coding: utf-8 -*-
import requests
import json
import time


def pet_detail_networking(topic_id):
	headers = {'Content-Type': 'application/json'}
	data = {
		'topic_id': topic_id
	}
	url = 'https://rescue.rxswift.cn/api/topic/detail/'
	response = requests.post(url,headers=headers,data=json.dumps(data))
	if response.status_code == 200:
		print(response.text)
		print('success')
	else:
		print(response.status_code)
		print('error')


if __name__ == "__main__":
	topic_id = 1012
	pet_detail_networking(topic_id)
