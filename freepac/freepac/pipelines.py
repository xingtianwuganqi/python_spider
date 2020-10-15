# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import qrcode
import base64
import os
from freepac.settings import IMAGES_STORE
from PIL import Image
import os
class FreepacPipeline:
    def process_item(self, item, spider):
        if item['method'] == "aes-256-gcm":
            return item
        qrcode_str = item['method'] + ':' + item['password'] + '@' + item['server'] + ':' + item['port']
        if "\xa0" in qrcode_str:
            arr = qrcode_str.split("\xa0")
            print('arr ==== ',arr)
            qrcode_str = arr[0] + ' ' + arr[1]
        else:
            print(" No Arr")
        str_url = base64.b64encode(qrcode_str.encode('utf-8'))# 被编码的参数必须是二进制数据
        print(str_url)
        code = 'ss://'+str(str_url, encoding = "utf-8")
        print(code)
        path = '{}.png'.format(item['server'] + ':' + item['port'])
        if not os.path.exists(IMAGES_STORE):
            os.makedirs(IMAGES_STORE)
        filename = '{}{}{}'.format(IMAGES_STORE, os.sep, path)
        print('os.sep ====',os.sep,filename)
        img = qrcode.make(code)
        img.save(filename)
        return item



