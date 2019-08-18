import requests
import time
import re
import base64
import hmac
import hashlib
import json
import matplotlib.pyplot as plt
from http import cookiejar
from PIL import Image

#  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
class zhihuLogin():

    def __init__(self):
        self.login_url = 'https://www.zhihu.com/signup'
        self.login_api = 'https://www.zhihu.com/api/v3/oauth/sign_in'
        self.login_data = {
            'client_id': 'c3cef7c66a1843f8b3a9e6a1e3160e20',
            'grant_type': 'password',
            'source': 'com.zhihu.web',
            'username': '',
            'password': '',
            # 传入'cn'是倒立汉字验证码
            'lang': 'en',
            'ref_source': 'homepage',
        }

        self.session = requests.session()
        self.session.headers = {
            'Host': 'www.zhihu.com',
            'Referer': 'https://www.zhihu.com/signin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

        self.session.cookies = cookiejar.LWPCookieJar(filename='./cookies.txt')

    def login(self,username = None,password = None,load_cookies = True):

        if load_cookies and self.load_cookie():
            if self.check_login():
                return True
        headers = self.session.headers.copy()
        headers.update({
            'X-Xsrftoken': self.get_token()
        })

    def load_cookie(self):
        '''
        读取cookie
        :return:
        '''
        try:
            self.session.cookies.load(ignore_discard=True)
            return True
        except FileNotFoundError:
            return False

    def check_login(self):
        resp = self.session.get(self.login_url,allow_redirects = False)
        if resp.status_code == 302:
            self.session.cookies.save()
            print('登录成功')
            return True
        return False

    def get_token(self,lang,headers):
        if lang == 'cn':
            api = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=cn'
        else:
            api = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=en'

        resp = self.session.get(api,headers,headers)
        show_captcha = re.search(r'true',resp.text)

        if show_captcha:
            put_resp = self.session.put(api, headers=headers)
            json_data = json.loads(put_resp.text)
            img_base64 = json_data['img_base64'].replace(r'\n', '')
            with open('./captcha.jpg', 'wb') as f:
                f.write(base64.b64decode(img_base64))
            img = Image.open('./captcha.jpg')
            if lang == 'cn':
                plt.imshow(img)
                print('点击所有倒立的汉字，按回车提交')
                points = plt.ginput(7)
                capt = json.dumps({'img_size': [200, 44],
                                   'input_points': [[i[0] / 2, i[1] / 2] for i in points]})
            else:
                img.show()
                capt = input('请输入图片里的验证码：')
            # 这里必须先把参数 POST 验证码接口
            self.session.post(api, data={'input_text': capt}, headers=headers)
            return capt
        return ''