import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawlhupu.items import hupuDetailItem

class HupucrawlSpider(CrawlSpider):
    name = 'hupucrawl'
    allowed_domains = ['bbs.hupu.com']
    start_urls = ['http://bbs.hupu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'\d+.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = hupuDetailItem()
        item["title"] = response.xpath('//title/text()').extract_first()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        yield item
