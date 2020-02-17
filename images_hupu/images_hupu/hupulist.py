import requests
import lxml.etree as etree

class hupu():
    def __init__(self):
        self.base_url = 'https://bbs.hupu.com/selfie'

    def request(self):
        response =requests.get(self.base_url)
        if response.status_code == 200:
            return response.content
        else:
            return None

    def xpath_action(self,content):
        select = etree.HTML(content)
        list = select.xpath('//ul[@class="for-list"]/li')
        if len(list) > 0:
            list.remove(list[0])
        for i in list:
            link = i.xpath('./div[@class="titlelink box"]/a/@href')
            if len(link) > 1:
                print(link[-1])
            else:
                print(link[0])


if __name__ == "__main__":
    h = hupu()
    content = h.request()
    h.xpath_action(content)