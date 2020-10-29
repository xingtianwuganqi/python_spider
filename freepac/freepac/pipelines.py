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

        '''
        ss格式： ss://method:password@server:port
        ssr 格式：ssr://server:port:protocol:method:obfs:password_base64/?params_base64
        params_base64: obfsparam=obfsparam_base64&protoparam=protoparam_base64&remarks=remarks_base64&group=group_base64

        '''

        print('password====',item['password'])

        method_str = item['method']
        password_str = item['password']
        if '\xa0' in password_str:
            arr = password_str.split('\xa0')
            password_str = arr[0] + ' ' + arr[1]
        server_str = item['server']
        port_str = item['port']

        obfs_str = ''
        if item.get('obfs',0) != 0:
            # obfs 不为空
            obfs_str = item['obfs']
        protocol_str = ''
        if item.get('protocol',0) != 0:
            protocol_str = item['protocol']

        encode_str = ''
        if len(protocol_str) > 0:
            # 先将密码转成base64
            base64_pswd = base64.b64encode(password_str.encode('utf-8'))
            protocol = item['protocol']
            base64_obfs = base64.b64encode(obfs_str.encode('utf-8'))
            base64_proto = base64.b64encode(protocol.encode('utf-8'))
            print('base64_obfs === ', base64_obfs, 'base64_protocol === ', base64_proto)
            params_str = 'obfsparam=' + str(base64_obfs,encoding='utf-8') + '&protoparam=' + str(base64_proto,encoding='utf-8')
            print('params_str ====== : ',params_str)
            unencode_str = server_str + ':' + port_str + ':' + protocol_str + ':' + method_str + ':' + obfs_str + ':' + str(base64_pswd,encoding='utf-8') + '/?' + params_str
            print('unencode_str ==== ',unencode_str)
            str_url = base64.b64encode(unencode_str.encode('utf-8'))
            encode_str = 'ssr://' + str(str_url,encoding='utf-8')
            print(encode_str)

        else:
            qrcode_str = method_str + ':' + password_str + '@' + server_str + ':' + port_str
            print('qrcode_str ==== ',qrcode_str)
            str_url = base64.b64encode(qrcode_str.encode('utf-8'))# 被编码的参数必须是二进制数据
            encode_str = 'ss://'+str(str_url, encoding = "utf-8")
            print(encode_str)

        path = '{}.png'.format(server_str + ':' + port_str)
        if not os.path.exists(IMAGES_STORE):
            os.makedirs(IMAGES_STORE)
        filename = '{}{}{}'.format(IMAGES_STORE, os.sep, path)
        print('os.sep ====',os.sep,filename)
        img = qrcode.make(encode_str)
        img.save(filename)
        return item



