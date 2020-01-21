# -*- coding: utf-8 -*-
import scrapy
# import lxml.etree as etree
import re
from movieScrapy.items import MoviescrapyItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['www.beiwo888.com']
    start_urls = ['http://www.beiwo888.com/list/8/']

    def parse(self, response):
        items = MoviescrapyItem()
        # selector = etree.HTML(str(response.text))
        movie_list = response.xpath(
            '//div[@class="movielist"]/ul[@class="img-list clearfix"]/li')  # /a[@class="play-img"]/img/@alt
        for movie in movie_list:
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
            yield items

