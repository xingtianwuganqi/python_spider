import requests
from lxml import etree
import json

class Zhlogin():

    def __init__(self):

        self.headers = {
            'app-key':'eByjUyLDG2KtkdhuTsw2pY46Q3ceBPdT',
            'origin':'https://720yun.com',
            'referer': 'https://720yun.com/',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'cookie': '720yun_v8_session=NK1L5wep6MJQV83rZldbD4kpg4vPm9R7iV9WNe3oznWmBX9PAg2RvozjyE0YOx7G; Hm_lvt_08a05dadf3e5b6d1c99fc4d862897e31=1546960660; Hm_lpvt_08a05dadf3e5b6d1c99fc4d862897e31=1546961006'
        }
        self.session_headers = {
            'Referer' : 'https://720yun.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

        self.session_url = 'https://720yun.udesk.cn/agents/free'
        self.get_url = 'https://720yun.com/'
        self.login_url = 'https://apiv4.720yun.com/login'
        self.session = requests.Session()

    def get_session(self):
        get_data = {
            'im_web_plugin_id': '34116',
            'session_key': '',
            'callback': 'udesk_jsonp1'
        }

        response = self.session.get(self.session_url,headers=self.session_headers,data=get_data)
        if response.status_code == 200:
            print(response.content)


    def login(self,loginId,password):

        post_data = {
            'loginId': loginId,
            'password': password,
        }

        # respon = self.session.get(self.get_url,headers=self.headers)
        # if respon.status_code == 200:
        #     print(respon.text)

        response = self.session.post(self.login_url,data=post_data,headers=self.headers)
        if response.status_code == 200:
            print(response,response.content)
            dic = json.loads(response.content)
            print(dic)
            self.save_userInfo(response.content)
        else:
            print('login_error',response)

    def save_userInfo(self,dic):
        with open('userInfo.json','wb+') as file_objc:
            file_objc.write(dic)

if __name__ == "__main__":
    login = Zhlogin()
    login.get_session()
    login.login(loginId='15652715776',password='123456')

