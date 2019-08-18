import pymysql

# 连接数据库 刚开始数据库密码为空
db = pymysql.connect(host='localhost',user='root',password='qwe123',port=3306) # 连接数据库
cursor = db.cursor() # 获取mySql 的操作游标
cursor.execute('SELECT VERSION()')
data = cursor.fetchone() # 获取第一条数据
print('Database version:',data)
cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8') # 创建数据库的操作
db.close()