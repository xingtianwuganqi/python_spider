import pymongo

def find():
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.taobao
    collections = db.products
    try:
        result = collections.find_one({'shop': '新异奇数码专营店'})
        print(result)
        count = collections.find()
        for i in count:
            print(i)
        # print(collections.find().count())
    except:
        print('查询失败')

def main():
    find()

if __name__ == '__main__':
    main()