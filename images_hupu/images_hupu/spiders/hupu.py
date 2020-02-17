# -*- coding: utf-8 -*-
import scrapy
import requests
import lxml.etree as etree
from scrapy import Spider, Request


class HupuSpider(scrapy.Spider):
    name = 'hupu'
    allowed_domains = ['bbs.hupu.com']
    start_urls = ['https://bbs.hupu.com/selfie']

    def start_requests(self):
        # 构建url
        content = self.request()
        links = self.xpath_action(content)
        for url in links:
            link = "https://bbs.hupu.com" + url
            yield Request(url,self.parse)

    def parse(self, response):
        pass

    def request(self):
        response =requests.get("https://bbs.hupu.com/selfie")
        if response.status_code == 200:
            return response.content
        else:
            return None

    def xpath_action(self,content):
        urls = []
        select = etree.HTML(content)
        list = select.xpath('//ul[@class="for-list"]/li')
        if len(list) > 0:
            list.remove(list[0])
        for i in list:
            link = i.xpath('./div[@class="titlelink box"]/a/@href')
            if len(link) > 1:
                urls.append(link(-1))
            else:
                urls.append(link[0])
        return urls
