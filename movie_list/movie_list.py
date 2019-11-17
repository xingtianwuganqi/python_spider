import requests
import lxml.etree as etree
import re

class movie_list():

    def __init__(self):
        self.url = 'http://www.beiwo888.com/list/1/'
        self.baseUrl = 'http://www.beiwo888.com'
        self.testUrl = 'http://www.beiwo888.com/list/8'

    def networking(self,url):
        response = requests.get(url)
        response.encoding="utf-8"
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

    def getPageNum(self,text):
        selector = etree.HTML(text)
        page_texts = selector.xpath('//div[@id="pages"]/text()')
        if len(page_texts) > 0:
            page_text = page_texts[0]
            result = re.search('^共.*:1/(.*)页',page_text,re.S)
            return result.group(1)
        else:
            return None


    def movieList(self,text):
        # 根据电源类型获取电源列表
        # print(text)
        pages = self.getPageNum(text)
        print(pages,type(pages))
        if int(pages) > 0:
            selector = etree.HTML(text)
            movie_list = selector.xpath('//div[@class="movielist"]/ul[@class="img-list clearfix"]/li')#/a[@class="play-img"]/img/@alt
            print(movie_list)
            for movie in movie_list:
                print(movie)
                movie_name = movie.xpath('./h5/a/text()')[0]
                movie_url  = movie.xpath('./h5/a/@href')[0]
                actor = movie.xpath('./p')[0].xpath('./a/text()')
                movie_actor = "，".join(map(lambda x: str(x),actor))
                movie_star = movie.xpath('./p[@class="star"]/em/text()')
                print(movie_name,movie_url,movie_actor,movie_star)[0]
                yield {
                    "movie_name": movie_name,
                    "movie_url" : movie_url,
                    "movie_actor" : movie_actor,
                    "movie_star" : movie_star
                }




if __name__ == '__main__':
    movies = movie_list()
    # text = movies.networking(movies.url)
    #     # # 类型列表
    #     # dic = movies.hotType(text)
    #     # print(dic)
    text = movies.networking(movies.testUrl)
    movies.movieList(text)



