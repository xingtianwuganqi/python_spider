import requests
from urllib.parse import urlencode
import json
import pymongo
import time
import os

def get_photo(url,offset):

    params = {
        "offset": offset * 20,
        "format": "json",
        "keyword": "街拍",
        "autoload": "true",
        "count": 20,
        "cur_tab": 1,
        "from": "search_tab",
        "pd": "synthesis"
    }

    headers = {
        'content-type' : 'application/x-www-form-urlencoded',
        'cookie' : 'tt_webid=6631143644018214403; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=f8aswxa9j1543933446130; tt_webid=6631143644018214403; csrftoken=52db98f9b74e7c8b6249f51d1a8f49c7',
        'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
        'x-requested-with':'XMLHttpRequest'
    }

    try:
        response = requests.get(url = url, headers = headers,params = params)
        if response.status_code == 200:
            return response.text
        return None
    except:
        print('网络请求失败')
        return None
def get_imgurl(text):
    datas = json.loads(text)['data']

    for data in datas:
        if 'open_url' in data.keys():
            img_arr = []
            for img in data["image_list"]:
                img_arr.append(img['url'].replace('list','origin'))
            yield {
                'title':data["title"],
                'img':img_arr
            }
def clear_mongodb():
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.jrtt  # 创建库
    collections = db.jrttdata  # 创建集合，类似表
    # 插入时先清空数据库
    collections.delete_many({})  # 删除所有

def create_mongodb(imgs):
    client = pymongo.MongoClient(host = 'localhost',port = 27017)
    db = client.jrtt # 创建库
    collections = db.jrttdata # 创建集合，类似表
    collections.insert_many(imgs)

def find_allimg():
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.jrtt  # 创建库
    collections = db.jrttdata  # 创建集合，类似表
    data = collections.find()
    for da in data:
        print(da)
        down_loadImg(da['img'])


def down_loadImg(imgs):
    for imgurl in imgs:
        print(imgurl)
        try:
            img = requests.get('https:'+imgurl)
            if img.status_code == 200:
                root = 'jrtt//'
                path = imgurl.split("/")[-1]
                if not os.path.exists(root+path+'.jpg'): # 判断路径下是不是已经存在该图片
                    with  open(root+path+'.jpg','wb') as f:
                        f.write(img.content)
                else:
                    print('Already DownLoaded',root+path+'.jpg')
            else:
                print('下载失败',img.status_code)
        except:
            print('出错继续')
            pass
def main():
    url = 'https://www.toutiao.com/search_content/?'
    clear_mongodb()
    for i in range(0,5):
        data = get_photo(url,i)
        imgs = get_imgurl(data)
        create_mongodb(imgs)

    time.sleep(2)

    find_allimg()

if __name__ == '__main__':
    main()