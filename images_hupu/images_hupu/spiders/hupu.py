# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
from images_hupu.items import ImagesHupuItem

class HupuSpider(scrapy.Spider):
    name = 'hupu'
    allowed_domains = ['bbs.hupu.com']
    start_urls = ['https://bbs.hupu.com/selfie']
    base_url = 'https://bbs.hupu.com'
    # def start_requests(self):
    #     # 构建url
    #     content = self.request()
    #     links = self.xpath_action(content)
    #     for url in links:
    #         link = "https://bbs.hupu.com" + url
    #         yield Request(url,self.parse)

    def start_requests(self):
        base_url = 'https://bbs.hupu.com/selfie-'
        for page in range(1, 3):
            url = base_url + str(page)
            yield Request(url, self.parse)

    def parse(self, response):
        lists = response.xpath('//ul[@class="for-list"]/li')
        for i in lists:
            item = ImagesHupuItem()
            link = i.xpath('./div[@class="titlelink box"]/a/@href').extract()
            # if len(link) > 1:
            #     item["detail_url"] = link[-1]
            # else:
            #     item["detail_url"] = link[0]
            if link[-1] == "/25814835.html":
                continue
            else:
                item["detail_url"] = link[-1]
            url = self.base_url + item["detail_url"]
            yield Request(url,meta={'item': item},callback=self.detail_parse)

    def detail_parse(self,response):
        # 接收上级已爬取的数据
        item = response.meta['item']
        imgurl = response.xpath('//div[@class="quote-content"]/p/img/@src').extract()
        if "https://b1.hoopchina.com.cn/web/sns/bbs/images/placeholder.png" in imgurl:
            imgurl.remove("https://b1.hoopchina.com.cn/web/sns/bbs/images/placeholder.png")
        if len(imgurl) > 0:
            long_url = ""
            for i in imgurl:
                img_url = i.split('?x',1)[0]
                long_url = long_url + "," + img_url
            item["image_url"] = long_url
            yield item
        else:
            item["image_url"] = "null"
            yield item
