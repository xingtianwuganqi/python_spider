import scrapy
from freepac.items import FreepacItem

class FreechainSpider(scrapy.Spider):
    name = 'freechain'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7']

    def parse(self, response):
        list = response.xpath('//div[@class="markdown-body"]/table[@role="table"]/tbody/tr')#
        for data in list:
            earn = data.xpath('./td/text()').extract()
            item = FreepacItem()
            item['method'] = earn[4]
            item['password'] = earn[3]
            item['server'] = earn[1]
            item['port'] = earn[2]
            yield item