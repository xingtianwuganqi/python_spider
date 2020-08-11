import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawlhupu.items import hupuDetailItem

class HupucrawlSpider(CrawlSpider):
    name = 'hupucrawl'
    allowed_domains = ['bbs.hupu.com']
    start_urls = ['https://bbs.hupu.com/selfie']

    rules = (
        Rule(LinkExtractor(allow=r'/\d+.html$'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = hupuDetailItem()
        img_url = []
        ps = response.xpath('//div[@class="quote-content"]/p')
        title= response.xpath('//title/text()').extract_first()
        if ps and len(ps) > 0:
            for p in ps:
                imgs = p.xpath('./img/@src').extract()
                if imgs and len(imgs) > 0:
                    for img in imgs:
                        if len(img) > 0 and "placeholder" not in img:
                            img_url.append(img)
                        else:
                            continue
                else:
                    continue
        else:
            imgs = response.xpath('//div[@class="quote-content"]/div/img/@src').extract()
            if imgs and len(imgs) > 0:
                for img in imgs:
                    if len(img) > 0 and "placeholder" not in img:
                        img_url.append(img)
                    else:
                        continue

        img_str = ';'.join(img_url)
        if len(img_str) > 0:
            item['imgs'] = img_str
            item['title'] = title
            print('have img',title)
            yield item
        else:
            print("no img ",title)
            yield None

