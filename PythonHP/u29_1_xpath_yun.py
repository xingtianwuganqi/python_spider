import requests

r = requests.get('https://720yun.com/')
if r.status_code == 200:
	print(r.text)
else: 
	print('error')