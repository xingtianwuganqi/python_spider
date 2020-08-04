# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 下载图片
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from PIL import Image

class CocoaSpiderPipeline:
    def process_item(self, item, spider):
        return item

class ImageDownLoad(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 生成request对象，加入调度队列
        file_url = item['img_url']
        print('first',item['article_text'])
        if len(file_url) > 0:
            file_name = file_url.split('uploads')[-1]
            file_name = "http://cc.cocimg.com/api/uploads" + file_name
            yield Request(file_name)
        else:
            yield DropItem('file_url null')


    def file_path(self, request, response=None, info=None):
        # 返回照片的文件名
        img_url = request.url
        file_name = img_url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        # 判断是否下载完成，下载失败返回忽略
        image_paths = [x['path'] for ok,x in results if ok]
        if not image_paths:
            return DropItem("Image Download Failed")
        return item