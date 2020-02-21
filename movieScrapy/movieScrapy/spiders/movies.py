# -*- coding: utf-8 -*-
import scrapy
# import lxml.etree as etree
import re
from movieScrapy.items import MoviescrapyItem
from scrapy import Request
import re


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['www.beiwo888.com']
    start_urls = ['http://www.beiwo888.com/list/8/']
    base_url = 'http://www.beiwo888.com/list/8/'
    detail_url = 'http://www.beiwo888.com'

    def start_requests(self):
        # 一共107页
        for i in range(1, 2):
            if i == 1:
                url = self.base_url
                self.logger.debug("第一页" + url)
                yield Request(url=url, callback=self.parse)
            else:
                url = self.base_url + "index-{}.html".format(i)
                self.logger.debug(url)
                yield Request(url=url, callback=self.parse)

    def parse(self, response):
        movie_list = response.xpath(
            '//div[@class="movielist"]/ul[@class="img-list clearfix"]/li')  # /a[@class="play-img"]/img/@alt
        for movie in movie_list:
            items = MoviescrapyItem()
            movie_name = movie.xpath('./h5/a/text()').extract_first()
            movie_url = movie.xpath('./h5/a/@href').extract_first()
            actor = movie.xpath('./p').xpath('./a/text()').extract()
            movie_actor = "/".join(map(lambda x: str(x), actor))
            movie_star = movie.xpath('./p[@class="star"]/em/text()').extract_first()
            movie_img = movie.xpath('./a[@class="play-img"]/img/@src').extract_first()
            items['movie_type'] = "动作片"
            items['movie_name'] = movie_name
            items['movie_url'] = movie_url
            items['movie_img'] = movie_img
            items['movie_actor'] = movie_actor
            items['movie_star'] = movie_star
            url = self.detail_url + items["movie_url"]
            yield Request(url=url,meta={'item': items},callback=self.movie_detail)

    def movie_detail(self,response):
        item = response.meta['item']
        year = response.xpath('//div[@class="info"]/ul/li/text()').extract_first()
        downlist = response.xpath('//div[@class="downlist"]/ul/script').extract_first()
        results = re.search('var.*?= "(.*)";.*?', downlist, re.S)
        movie_list_str = results.group(1)
        print(movie_list_str)
        description = response.xpath('//div[@class="endtext"]/text()').extract_first()
        item["movie_year"] = year
        item["movie_download"] = movie_list_str
        item["movie_description"] = description
        return item
