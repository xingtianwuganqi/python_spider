# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FreepacItem(scrapy.Item):
    method = scrapy.Field() # 加密方式
    password = scrapy.Field() # 密码
    server = scrapy.Field() # 地址
    port = scrapy.Field() # 端口
    protocol = scrapy.Field() # 协议
    obfs = scrapy.Field() # 混淆