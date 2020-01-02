import requests
import lxml.etree as etree
import re
from ipcontent.RedisClient import RedisClient

class IPNetWorking():
    def __init__(self):
        self.url = "http://www.66ip.cn/1.html"
        self.baseUrl = 'http://www.66ip.cn/'
        self.redis = RedisClient()

    def networking(self,url):
        response = requests.get(url)
        response.apparent_encoding
        response.encoding = "utf-8"
        if response.status_code == 200:
            return response.content
        else:
            return None

    def get_ip_list(self,text):
        selected = etree.HTML(text)
        ips = selected.xpath('//div[@class="container"]/div[@class="containerbox boxindex"]/div[@align="center"]/table//tr')
        ips.remove(ips[0])
        for ippath in ips:
            ip = ippath.xpath('./td/text()')[0]
            port = ippath.xpath('./td/text()')[1]
            address = ippath.xpath('./td/text()')[2]
            ip_type = ippath.xpath('./td/text()')[3]
            test_time = ippath.xpath('./td/text()')[4]
            yield {
                'ip': ip,
                'port': port,
                'address': address,
                'ip_type': ip_type,
                'test_time': test_time
            }


    def get_page(self):
        text = self.networking(self.baseUrl)
        selected = etree.HTML(text)
        pages = selected.xpath('//div[@class="container"]/div[@class="containerbox boxindex"]/div[@class="mypage"]/div/div[@id="PageList"]/a')
        page = pages[-2]
        count = page.xpath('./text()')[0]
        return count

    def save_list(self,ips):
        for ip in ips:
            proxy = ip["ip"] + ":" + ip["port"]
            print(proxy)
            if not self.redis.exists(proxy):
                self.redis.add(proxy)
            else:
                print("代理已存在")

    def main(self):
        page = self.get_page()
        print(page)
        if int(page) > 10:
            for i in range(1,11):
                text = self.networking(self.baseUrl + str(i) + ".html")
                ips = self.get_ip_list(text)
                self.save_list(ips)

if __name__ == "__main__":
    net = IPNetWorking()
    net.main()
