# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from MyQR import myqr
import base64
import os
from freepac.settings import IMAGES_STORE
from PIL import Image
class FreepacPipeline:
    def process_item(self, item, spider):
        method = item['method']
        if method == 'RC4':
            method = 'rc4'
        qrcode_str = method + ':' + item['password'] + '@' + item['server'] + ':' + item['port']
        print(qrcode_str)
        bytes_url = qrcode_str.encode("utf-8")
        str_url = base64.b64encode(bytes_url)  # 被编码的参数必须是二进制数据
        code = 'ss://'+str(str_url, encoding = "utf-8")
        print(code)
        img = myqr.run(words=code)
        print(img)
        # im.save('./Image/{}.png'.format(item['server'] + ':' + item['port']))
        return item



