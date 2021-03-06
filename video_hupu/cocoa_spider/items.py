# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VideoItem(scrapy.Item):

    title = scrapy.Field()
    desc = scrapy.Field()
    athor = scrapy.Field()
    time = scrapy.Field()
    img_url = scrapy.Field()
    article_id = scrapy.Field()
    article_text = scrapy.Field()


