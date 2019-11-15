import requests
import lxml.etree as etree

class movie_list():

    def __init__(self):
        self.url = 'http://www.beiwo888.com/list/1/'

    def networking(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    def hotType(self,text):
        # 使用xpath 对文本进行解析
        selector = etree.HTML(text)
        hotTypes = selector.xpath('//body[@class="channel15"]/div[@id="header"]/div[@id="menu"]/p[@class="s"]/a')
        print(hotTypes)
        dic = {}
        for hot in hotTypes:
            print(hot.tag,hot.attrib["href"],hot.text)
            dic[hot.text] = hot.attrib["href"]
        return dic


if __name__ == '__main__':
    movies = movie_list()
    text = movies.networking()
    dic = movies.hotType(text)
    print(dic)
