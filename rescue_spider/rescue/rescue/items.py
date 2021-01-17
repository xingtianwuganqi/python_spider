# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RescueItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()

