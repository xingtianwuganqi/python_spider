import requests
import lxml.etree as etree
import re
import pymysql
from xpinyin import Pinyin

class movie_list():

    def __init__(self):
        self.url = 'http://www.beiwo888.com/list/1/'
        self.baseUrl = 'http://www.beiwo888.com'
        self.testUrl = 'http://www.beiwo888.com/list/8'
        self.db = pymysql.connect(host='localhost',user='root',password='qwe123',port=3306,db='spiders',charset='utf8')
        self.cursor = self.db.cursor()
        self.p = Pinyin()

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
        dic = {}
        for hot in hotTypes:
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

    def movieListType(self, text):
        selector = etree.HTML(text)
        type_texts = selector.xpath('//div[@class="filter"]/div[@class="title"]/b/text()')
        if len(type_texts) > 0:
            type_text = type_texts[0]
            type = re.search('(.*)分类筛选',type_text,re.S)
            return type.group(1)
        else:
            return None


    def movieList(self,text):
        # 根据电源类型获取电源列表
        # print(text)
        pages = self.getPageNum(text)
        type = self.movieListType(text)
        if int(pages) > 0:
            selector = etree.HTML(text)
            movie_list = selector.xpath('//div[@class="movielist"]/ul[@class="img-list clearfix"]/li')#/a[@class="play-img"]/img/@alt
            for movie in movie_list:
                movie_name = movie.xpath('./h5/a/text()')[0]
                movie_url  = movie.xpath('./h5/a/@href')[0]
                actor = movie.xpath('./p')[0].xpath('./a/text()')
                movie_actor = "/".join(map(lambda x: str(x),actor))
                movie_star = movie.xpath('./p[@class="star"]/em/text()')[0]
                yield {
                    "movie_type": type,
                    "movie_name": movie_name,
                    "movie_url" : movie_url,
                    "movie_actor" : movie_actor,
                    "movie_star" : movie_star
                }





    def create_mysql_list(self,table_name):
        sql ="""CREATE TABLE IF NOT EXISTS %s (
        movie_type VARCHAR(255) NOT NULL,
        movie_name VARCHAR(255) NOT NULL,
        movie_url VARCHAR(255) NOT NULL,
        movie_actor VARCHAR(255) NOT NULL,
        movie_star VARCHAR(255) NOT NULL,
        PRIMARY KEY (movie_name))"""%table_name
        self.cursor.execute(sql)

    def drop_table(self,table_name):
        sql = """
            drop table %s        
        """%table_name
        self.cursor.execute(sql)

    def getpingyin(self,text):
        pinyin = self.p.get_pinyin(text,splitter='')
        return pinyin

    def insert_data(self,dic):
        # for key,value in dic.items():
        key = dic["movie_type"]
        list_name = self.getpingyin(key)
        sql = 'insert into {} (movie_type,movie_name,movie_url,movie_actor,movie_star) VALUES (%s,%s,%s,%s,%s)'.format(list_name)
        print(sql)
        try:
            self.cursor.execute(sql,(str('%s')%dic["movie_type"],str('%s')%dic["movie_name"],str('%s')%dic["movie_url"],str('%s')%dic["movie_actor"],str('%s')%dic["movie_star"]))
            self.db.commit()
            print("success")
        except  Exception as e:
            print(str(e))
            self.db.rollback()
            print("error")




if __name__ == '__main__':
    movies = movie_list()
    types_text = movies.networking(movies.url)
    # # 类型列表
    type_dic = movies.hotType(types_text)
    print(type_dic)
    # 根据种类建表
    # for key,value in type_dic.items():
    #     table_name = movies.getpingyin(key)
    #     print(table_name)
    #     movies.create_mysql_list(table_name)
        # movies.drop_table(table_name)

    text = movies.networking(movies.testUrl)
    dic = movies.movieList(text)
    for i in dic:
        print(i)
        movies.insert_data(i)


