import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawlhupu.items import hupuDetailItem

class HupucrawlSpider(CrawlSpider):
    name = 'hupucrawl'
    allowed_domains = ['bbs.hupu.com']
    start_urls = ['https://bbs.hupu.com/selfie']

    rules = (
        Rule(LinkExtractor(allow=r'\d+.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = hupuDetailItem()
        img_url = []
        ps = response.xpath('//div[@class="quote-content"]/p')
        print(ps)
        for p in ps:
            xl = p.xpath('./img/@src').extract_first()
            if xl and len(xl) > 0 and "placeholder" not in xl:
                print("xl is ", xl)
                img_url.append(xl)
            else:
                break

        img_str = ','.join(img_url)
        if len(img_str) > 0:
            item['imgs'] = img_str
            yield item
        else:
            yield None

