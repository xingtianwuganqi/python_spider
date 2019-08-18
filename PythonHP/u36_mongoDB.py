import pymongo
from bson.objectid import ObjectId
# mongodb 连接
client = pymongo.MongoClient(host = 'localhost',port = 27017)
# client = pymongo.MongoClient('mongodb://localhost:27017/')
# 指定数据库
db = client.test
# db = client["test"]

# 指定集合 类似于关系数据库中的表
collections = db.studentss
# collection = db["students"]

# # 插入数据
# student = {
#     'id' : '20120001',
#     'name' : 'bob',
#     'age' : 20,
#     'gendel': 'male'
# }
#
# result = collections.insert_one(student)
# print(result)
# print(result.inserted_id)
#
# student1 = {
#     'id':'20120002',
#     'name': 'tom',
#     'age': 30,
#     'gendel': 'male'
# }
#
# student2 = {
#     'id':'20120003',
#     'name': 'Anni',
#     'age': 22,
#     'gendel': 'girl'
# }
#
# result1 = collections.insert_many([student1,student2])
# print(result1)
# print(result1.inserted_ids)

# 查询
# result = collections.find_one({'name': 'tom'}) # 查询第一条数据
# print(type(result))
# print(result)

# 通过objectid 查询
result = collections.find_one({'_id': ObjectId('5c03e9a5a1069e4218b79fbc')})
print(result)

result1 = collections.find({'name':'tom'})
print(result1)
for i in result1:
    print(i)

result2 = collections.find({'age':{'$gt':21}})
for i in result2:
    print(i)

# 正则匹配查询
# 查询name 以b 开头的
result3 = collections.find({'name':{'$regex':'^b.*'}})
for i in result3:
    print(i['id'])

# 计数

result4 = collections.find({'name':'bob'}).count()
print(result4)

# 排序
result5 = collections.find().sort('name',pymongo.DESCENDING) # pymongo.ASCENDING升序  pymongo.DESCENDING 降序
print([result['name'] for result in result5])

# 偏移
result6 = collections.find().sort('name',pymongo.DESCENDING).skip(2) # 获取下标为2及 以后的数据
print([result['name'] for result in result6])

# limit() 指定剩余几个数据
result7 = collections.find().sort('name',pymongo.DESCENDING).skip(2).limit(3)
print([i['name'] for i in result7])

# 数据库很大时不宜使用偏移

# 更新
condition = {'name':'bob'}
student = collections.find_one(condition)
student["age"] = 24
result8 = collections.update_one(condition,{'$set':student}) # 第一个参数传原条件，第二条数据传修改后的数据，但是要用{'$set': student}
print(result8)

conditions = {'age': {'$gt:22'}}
result9 = collections.update_one(condition,{'$inc': {'age': 1}}) # 满足conditions 条件的第一条数据，age 增加1
print(result9)
print(result9.matched_count,result9.modified_count) # 匹配数与影响数
# 使用update_many 会对所有数据进行更改

# 删除
result10 = collections.delete_one({'name':'tom'})
print(result10)

# delete_many 会删掉所有满足的条件

# 其他方法
# find_one_and_delete()  find_one_and_replace()

