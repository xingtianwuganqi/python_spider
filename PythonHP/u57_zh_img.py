import requests
from lxml import etree
from bs4 import BeautifulSoup

class zhihuImage():

    def __init__(self,url,token):

        self.requsetUrl = url + token
        self.headers = {
            'referer' : url+token,
            'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

    def get_html(self):

        response = requests.get(self.requsetUrl,headers = self.headers)
        if response.status_code == 200:
            return response.text

        return None

    def get_image(self,html):

        print(html)
        text = etree.HTML(html)
        list = text.xpath('//div[@class="Card"]/div[@class="List"]/div')[1]
        print(list)
        items = list.xpath('//div[@class="List-item"]')
        print(items)
        images = []
        for item in items:
            it = item.xpath('//figure/img/@data-original')
            images.append(it)
        print(images)
        return images


        # soup = BeautifulSoup(html,'lxml')
        # list_items = soup.select('div .List-item')
        # for list_item in list_items:
        #     print(list_item)

        # lists = soup.select('figure .origin_image.zh-lightbox-thumb.lazy')
        # print(lists)
        # images = []
        # for i in lists:
        #     print(i["data-original"])






if __name__ == '__main__':
    htmls = zhihuImage(
        url='https://www.zhihu.com/question/',
        token= '47246635'
    )
    html = htmls.get_html()
    items = htmls.get_image(html)