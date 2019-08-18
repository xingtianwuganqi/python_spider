from redis import StrictRedis,ConnectionPool

# 连接redis
# redis = StrictRe


# 使用ConnectionPool 连接
pool = ConnectionPool(host = 'localhost',port = 6379,db = 0,password = None)
redis = StrictRedis(connection_pool=pool)
redis.set('name','bob')
print(redis.get('name'))
