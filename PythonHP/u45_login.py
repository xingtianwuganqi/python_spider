from lxml import etree
import requests

class Login():
    def __init__(self):
        self.headers = {
            'Referer' : 'https://github.com/',
            'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_login = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.sesseion = requests.Session()

    def get_token(self):
        response = self.sesseion.get(self.login_url,headers = self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//form[@action="/session"]/input[@name="authenticity_token"]/@value')[0]
        return token

    def dynamics(self,html):
        '''登录成功之后获取首页列表'''
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[contains(@class,"news")]//div[contains(@class,"alert")]')
        for item in dynamics:
            dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
            print(dynamic)

    def profile(self,html):
        '''登录成功之后获取个人页面的信息'''
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
        print(name,email)

    def login(self,email,password):
        post_data = {
            'commit': "Sign in",
            'utf8': '✓',
            'authenticity_token': self.get_token(),
            'login':email,
            'password': password
        }

        response = self.sesseion.post(self.post_login,data=post_data,headers = self.headers)
        # if response.status_code == 200:
            # self.dynamics(response.text)

        respon = self.sesseion.get(self.logined_url,headers=self.headers)
        if respon.status_code == 200:
            self.profile(respon.text)


if __name__ == "__main__":
    login = Login()
    login.login(email='xingtianwuganqi123@163.com',password='github151216011602')
