# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class ImagesHupuPipeline(object):
#     def process_item(self, item, spider):
#         return item

import pymongo
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class MongoDBHupuPipeline(object):
    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DB")
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self,item,spider):
        name = "hupu"
        if item["image_url"] == "null":
            return DropItem()
        else:
            self.db[name].insert(dict(item))
            return item

    def close_spider(self,spider):
        self.client.close()


class ImagePipline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 生成request对象，加入调度队列
        img_list = item['image_url'].split(',')
        if len(img_list) > 0:
            for url in img_list:
                yield Request(url)
        else:
            yield DropItem('Dowload Failed')


    # 返回照片的文件名
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    # 判断是否下载完成，下载失败返回忽略
    def item_completed(self, results, item, info):
        image_paths = [x["path"] for ok,x in results if ok]
        if not image_paths:
            return DropItem('Image Download Failed')
        return item