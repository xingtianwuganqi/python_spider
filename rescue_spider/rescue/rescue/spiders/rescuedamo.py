import scrapy


class RescuedamoSpider(scrapy.Spider):
    name = 'rescuedamo'
    allowed_domains = ['www.douban.com']
    start_urls = ['http://www.douban.com/']
    base_url = 'https://www.douban.com/group/beijingpet/'

    def parse(self, response):
        lists = response.xpath('//table[@class="olt"]/tbody')
        # for item in lists:


