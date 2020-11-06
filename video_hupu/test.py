# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
import json
class Test():
    def __init__(self):
        # "http://www.cocoachina.com/api/v1/articles?page=1&typeid=0"
        self.url = 'https://games.mobileapi.hupu.com/3/7.5.23/forum/index?time_zone=Asia%2FShanghai&client=C4D03294-AE54-4B22-93EE-440D90472A9E&sign=5dffc10730a7cc5203cf38a5c521d826&night=0&crt=1604644411&clientId=91556154&is_first=0&bddid=4450454964275527&ab_items=4&name=video'

    def request_networking(self):
        # headers = {
        #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

        content = requests.get(self.url)
        if content.status_code == 200:
            print(content.text)
            self.xpath(content.text)

    def xpath(self,content):
        text = json.loads(content)
        print(content)
        # datas = text["data"]
        # for data in datas:
        #     print(data["title"])


if __name__ == "__main__":
    test = Test()
    test.request_networking()