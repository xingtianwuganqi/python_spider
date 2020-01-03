import requests
import lxml.etree as etree
import re
from ipcontent.RedisClient import RedisClient

import json
from ipcontent.utils import get_page

POOL_UPPER_THRESHOLD = 10000

class ProxyMetaClass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs["__CrawlFunc__"] = []
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1

        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls,name,bases,attrs)

class Crawler(metaclass=ProxyMetaClass):

    def __init__(self):
        self.baseurl = ""

    def get_proxies(self,callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理：',proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self,page_count = 5):
        start_url = "http://www.66ip.cn/{}.html"
        urls = [start_url.format(page) for page in range(1,page_count+1)]
        for url in urls:
            html = get_page(url)
            selected = etree.HTML(html)
            ips = selected.xpath('//div[@class="container"]/div[@class="containerbox boxindex"]/div[@align="center"]/table//tr')
            ips.remove(ips[0])
            for ippath in ips:
                ip = ippath.xpath('./td/text()')[0]
                port = ippath.xpath('./td/text()')[1]
                address = ippath.xpath('./td/text()')[2]
                ip_type = ippath.xpath('./td/text()')[3]
                test_time = ippath.xpath('./td/text()')[4]
                yield ":".join([ip,port])

    def crawl_89ip(self, page_count=5):
        start_url = "http://www.89ip.cn/index_{}.html"
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        ip_data = []
        for url in urls:
            html = get_page(url)
            selected = etree.HTML(html)
            ips = selected.xpath('//div[@class="fly-panel"]/div[@class="layui-form"]/table//tr')
            for ippath in ips:
                ip = ippath.xpath('//td/text()')[0].strip()
                port = ippath.xpath('//td/text()')[1].strip()
                yield ":".join([ip, port])

class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawl = Crawler()

    def is_over_threshold(self):
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print("获取器开始执行")
        print(self.crawl.__CrawlFuncCount__)
        for callback_label in range(self.crawl.__CrawlFuncCount__):
            callback = self.crawl.__CrawlFunc__[callback_label]
            proxies = self.crawl.get_proxies(callback)
            for proxy in proxies:
                if not self.redis.exists(proxy):
                    print(proxy)
                    self.redis.add(proxy)
                else:
                    print("代理已存在")


class test():
    def __init__(self):
        self.url = ""

    def crawl_89ip(self, page_count=5):
        start_url = "http://www.89ip.cn/index_{}.html"
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        ip_data = []
        for url in urls:
            html = get_page(url)
            selected = etree.HTML(html)
            ips = selected.xpath('//div[@class="fly-panel"]/div[@class="layui-form"]/table//tr')
            for ippath in ips:
                ip = ippath.xpath('//td/text()')[0].strip()
                port = ippath.xpath('//td/text()')[1].strip()
                yield ":".join([ip, port])

if __name__ == "__main__":
    net = Getter()
    net.run()

