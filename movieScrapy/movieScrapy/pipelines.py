# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class MoviescrapyPipeline(object):
#     def process_item(self, item, spider):
#         return item

from scrapy.exceptions import DropItem
import pymongo

class TextPipelines(object):
    def __init__(self):
        self.limit = 100

    def process_item(self,item,spider):
        if item["movie_name"]:
            return item
        else:
            return DropItem("missing text")


class mongoPipelines(object):

    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        print("+++++创建成功++++")

    def process_item(self,item,spider):
        # if item["movie_actor"]:
        #     return item
        # else:
        #     return DropItem("missing text")
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    def close_spider(self,spider):
        self.client.close()