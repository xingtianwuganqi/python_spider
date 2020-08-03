# -*- coding: utf-8 -*-
import scrapy
from cocoa_spider.items import CocoaItem
import requests, json
class CocoaSpider(scrapy.Spider):
    name = 'cocoa'
    allowed_domains = ['cocoachain','www.cocoachina.com','api.cocoachina.com']
    start_urls = ['http://www.cocoachina.com/api/v1/articles']
    begin_page = 1

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

        #?page=1&typeid=0
        if self.begin_page <= 1:
            self.begin_page = self.begin_page + 1
            next = '?page={}&typeid=0'.format(self.begin_page)
            url = response.urljoin(next)
            yield scrapy.Request(url=url,callback=self.parse)
        else:
            return