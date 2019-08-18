import pymysql

# 插入数据
# id = '20120001'
# user = 'bob'
# age = 20
# db = pymysql.connect(host='localhost',user='root',password='qwe123',port=3306,db='spiders')
# cursor = db.cursor()
# sql = 'INSERT INTO students(id,name,age) values(%s,%s,%s)'
# try:
#     cursor.execute(sql,(id,user,age))
#     print('插入成功')
#     db.commit()
# except:
#     print('插入失败')
#     db.rollback()
# db.close()

# 动态模式
# data = {
#     'id': '20120002',
#     'name': 'jim',
#     'age' : 21
# }
#
# tables = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s']*len(data))
# db = pymysql.connect(host='localhost',user='root',password='qwe123',port=3306,db='spiders')
# cursor = db.cursor()
# sql = 'INSERT INTO {tables}({keys}) values({values})'.format(tables = tables,keys = keys,values = values)
# try:
#     if cursor.execute(sql,tuple(data.values())):
#         print('Success')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()

#更新数据
# db = pymysql.connect(host='localhost',user='root',password='qwe123',port=3306,db='spiders')
# cursor = db.cursor()
# sql = 'UPDATE students SET age = %s WHERE name = %s'
# try:
#     cursor.execute(sql,(25,'bob'))
#     db.commit()
#     print('更新成功')
# except:
#     print('更新失败')
#     db.rollback()
# db.close()

# 设置去重
# data = {
#     'id' : '20120003',
#     'name' : 'jim',
#     'age': 23
# }
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s']*len(data))
#
# db = pymysql.connect(host='localhost',user='root',password='qwe123',port=3306,db='spiders')
# cursor = db.cursor()
# # ON DUPLICATE KEY UPDATE 意思是主键存在，执行更新操作，不存在执行插入操作
# sql = 'INSERT INTO {table}({keys}) VALUES ({valuse}) ON DUPLICATE KEY UPDATE'.format(table=table,keys=keys,valuse=values)
# update = ' '+','.join(['{key} = %s'.format(key=key) for key in data]) # 这个地方因为没有加空格导致插入失败
# sql += update
# print(sql)
# try:
#     if cursor.execute(sql,tuple(data.values())* 2):
#         print('更新成功')
#         db.commit()
# except:
#     print('更新失败')
#     db.rollback()
# db.close()

# 删除数据 需要指定要删除的目标表名和删除条件

# table = 'students'
# db = pymysql.connect(host = 'localhost',user = 'root',password = 'qwe123',port = 3306,db = 'spiders')
# cursor = db.cursor()
# condition = 'id = "20120002"' # 删除字符串时要给value 加引号
# sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
# print(sql)
# try:
#     cursor.execute(sql)
#     print('删除成功')
#     db.commit()
# except:
#     print('删除失败')
#     db.rollback()
# db.close()

# 查询数据

table = 'students'
db = pymysql.connect(host = 'localhost',user = 'root',password = 'qwe123',port = 3306, db = 'spiders')
cursor = db.cursor()
condition = 'id = "20120001"' # string 类型要带 “”
sql = 'SELECT *FROM students WHERE {condition}'.format(condition = condition)
# try:
#     cursor.execute(sql)
#     print('Count:',cursor.rowcount)
#     one = cursor.fetchone() # 查询第一条数据
#     print('one',one)
#     result = cursor.fetchall() # 如果先调用了fetone 方法，fetchall 方法会从下一条数据返回全部数据
#     print('Result',result)
#     for row in result:
#         print('row',row)
# except:
#     print('Error')

# 逐条查询
try:
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        print("Row:",row)
        row = cursor.fetchone()
except:
    print("Error")
