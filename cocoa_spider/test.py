# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
import json
class Test():
    def __init__(self):
        self.url = "http://www.cocoachina.com/api/v1/articles?page=1&typeid=0"

    def request_networking(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

        content = requests.get(self.url,headers=headers)
        if content.status_code == 200:
            self.xpath(content.text)

    def xpath(self,content):
        text = json.loads(content)
        datas = text["data"]
        for data in datas:
            print(data["title"])


if __name__ == "__main__":
    test = Test()
    test.request_networking()