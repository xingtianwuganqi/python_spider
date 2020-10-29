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
            item['method'] = earn[4]  # 加密方式
            item['password'] = earn[3] # 密码
            item['server'] = earn[1] # 服务
            item['port'] = earn[2] # 端口
            if len(earn) > 5:
                item['protocol'] = earn[5] # 协议
                item['obfs'] = earn[6] # 混淆
            yield item