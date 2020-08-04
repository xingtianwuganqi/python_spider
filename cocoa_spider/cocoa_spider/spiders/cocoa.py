# -*- coding: utf-8 -*-
import scrapy
from cocoa_spider.items import CocoaItem
import requests, json


from lxml import html
from html.parser import HTMLParser #

class CocoaSpider(scrapy.Spider):
    name = 'cocoa'
    allowed_domains = ['cocoachain','www.cocoachina.com','api.cocoachina.com']
    start_urls = ['http://www.cocoachina.com/api/v1/articles']
    begin_page = 1
    base_url = 'http://www.cocoachina.com/api/v1/articles'
    article_url = 'http://www.cocoachina.com/articles/'

    def start_requests(self):
        base_url = "http://www.cocoachina.com/api/v1/articles"
        url = base_url + '?page={}&typeid=0'.format(self.begin_page)
        yield scrapy.Request(url,self.parse)

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
            item['article_id'] = data["id"]
            url = self.article_url + str(item['article_id'])
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.article_detail)

    def article_detail(self,response):
        item = response.meta['item']
        detail = response.xpath('//div[@class="articles"]').extract_first()
        item['article_text'] = detail
        yield item