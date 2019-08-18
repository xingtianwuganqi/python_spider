import requests
from lxml import etree
import json

class Hplogin():
    def __init__(self):
        self.headers = {
            'Host' : 'auth.cocos.com',
            'Origin': 'https://auth.cocos.com',
            'Referer': 'https://auth.cocos.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'X-CSRF-TOKEN': 'A8H90GH13U',
        }
        self.signin_url = 'https://auth.cocos.com/jsApi/doSignIn'
        self.session = requests.Session()

    def login(self):
        post_data = {
            'username': '刑天舞干戚',
            'password': 'ios1512',
            'autoLogin': False,
            'checkCode': ''
        }
        response = self.session.post(self.signin_url,headers=self.headers,data=post_data)
        if response.status_code == 200:
            print(response.content)
            dic = json.loads(response.content)
            print(dic)

    # def redirect(self):



if __name__ == "__main__":
    login = Hplogin()
    login.login()