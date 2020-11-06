# -*- coding: utf-8 -*-
import scrapy
from cocoa_spider.items import VideoItem
import requests, json


from lxml import html
from html.parser import HTMLParser #

class CocoaSpider(scrapy.Spider):
    name = 'cocoa'
    allowed_domains = ['games.mobileapi.hupu.com']
    start_urls = ['https://games.mobileapi.hupu.com/3/7.5.23/forum/index?time_zone=Asia%2FShanghai&client=C4D03294-AE54-4B22-93EE-440D90472A9E&sign=5dffc10730a7cc5203cf38a5c521d826&night=0&crt=1604644411&clientId=91556154&is_first=0&bddid=4450454964275527&ab_items=4&name=video']


    def parse(self, response):
        print('text ==== :',response)
        text = json.loads(response.text)
        print(text)
        item = VideoItem()
        return item

