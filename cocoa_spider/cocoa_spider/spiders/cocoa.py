# -*- coding: utf-8 -*-
import scrapy
from cocoa_spider.items import CocoaItem
import requests, json
class CocoaSpider(scrapy.Spider):
    name = 'cocoa'
    allowed_domains = ['cocoachain']
    start_urls = ['http://www.cocoachina.com/api/v1/articles?page=1&typeid=0']

    def parse(self, response):
        text = json.loads(response.text)
        datas = text["data"]
        for data in datas:
            item = CocoaItem()
            item['title'] = data["title"]
            item['athor'] = data["writer"]
            item['desc'] = data["description"]
            item['time'] = data["pubdate_new"]
            item['img_url'] = data["litpic"]
            yield item
