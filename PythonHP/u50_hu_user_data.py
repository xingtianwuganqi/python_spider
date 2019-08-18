import requests
from lxml import etree

class HPUserInfo():

    def __init__(self):
        self.headers = {
            'cookie': '_cnzz_CV30020080=buzi_cookie%7Ce2eb9183.8477.5dc1.5178.3c5144b78953%7C-1; _dacevid3=e2eb9183.8477.5dc1.5178.3c5144b78953; __gads=ID=649e340af5e92bd2:T=1492919805:S=ALNI_MYBMVtFZPo1STOmtXSZ9n95WTVhRQ; _HUPUSSOID=c6ddd697-8934-4d2d-926f-4ea3c01e6954; PHPSESSID=jsfmg6b3kr9v79n7hq1lb562u7; _cnzz_CV30020080=buzi_cookie%7Ce2eb9183.8477.5dc1.5178.3c5144b78953%7C-1; AUM=dgCXGiCQoriRSTtS7_kLmDI3jN5nt-yqlWtWpTno5j7lw; _CLT=00376064be821b71351c003dda774e37; u=26245921|6KW/5a6J5bel56iL5aSn5a2m546v5YyW5a2m6Zmi|4216|f799fea6e38ca7c4c6121d9d7b5dd49b|e38ca7c4c6121d9d|aHVwdV82MmU0ZDMyMzViYjM3OThk; us=b6d23ea03287659004f98cc5891277f17031ccd797ead77af39920d01ca404ea24c1d288f6b851e3535032e42b8a3f2de72c0a109b89d4de64cc223ab3d41d83; ua=70320264; _fmdata=4eg04TbIIm0H7KrQ0EIYVA1dda%2BfGtH8eqqirUL7YPWK6qDbACkKYZhr7FklqLIkwZKFTsw9wayBUMOarHdw1TBB1qKFvUvLE7vcNJ6lKwA%3D; __dacevst=2b84afb1.b5f5be6c|1547047794544',
            'referer': 'https://my.hupu.com/125698410611229',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'upgrade-insecure-requests': "1"
        }

        self.get_url = 'https://my.hupu.com/125698410611229'
        self.session = requests.Session()


    def get_userInfo(self):

        response = self.session.get(self.get_url,headers = self.headers)
        if response.status_code == 200:
            self.get_sex(response.text)


    def get_sex(self,html):

        selector = etree.HTML(html)
        name = selector.xpath('//title/text()')[0]
        sex = selector.xpath('//div[@class="personalinfo"]/span[@itemprop="gender"]/text()')[0]
        image = selector.xpath('//div[@class="personal_left"]/img[@id="j_head"]/@src')[0]
        print(name,sex,image)



if __name__ == "__main__":
    info = HPUserInfo()
    info.get_userInfo()