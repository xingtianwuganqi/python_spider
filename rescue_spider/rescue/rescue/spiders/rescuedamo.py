import scrapy


class RescuedamoSpider(scrapy.Spider):
    name = 'rescuedamo'
    allowed_domains = ['www.douban.com']
    start_urls = ['http://www.douban.com/']

    def parse(self, response):
        pass
