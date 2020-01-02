REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = "proxies"
INITIAL_SCORE = 10
MAX_SCORE = 100
MIN_SCORE = 0

import redis
from random import choice

class RedisClient():
    def __init__(self,host = REDIS_HOST,port = REDIS_PORT,password = REDIS_PASSWORD):
        self.db = redis.StrictRedis(
            host=host,
            port=port,
            password=password
        )

    def add(self,proxy,score = INITIAL_SCORE):
        if not self.db.zscore(REDIS_KEY,proxy):
            return self.db.zadd(REDIS_KEY,{proxy:score})

    def random(self):
        result = self.db.zrangebyscore(REDIS_KEY,MAX_SCORE,MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrangebyscore(REDIS_KEY,0,100)
            if len(result):
                return choice(result)
            else:
                return None

    def decrease(self,proxy):
        score = self.db.zscore(REDIS_KEY,proxy)
        if score and score > MIN_SCORE:
            return self.db.zincrby(REDIS_KEY,-1,proxy)
        else:
            return self.db.zrem(REDIS_KEY,proxy)

    def exists(self,proxy):
        return not self.db.zscore(REDIS_KEY,proxy) == None

    def max(self,proxy):
        return self.db.zadd(REDIS_KEY,{proxy:MAX_SCORE})

    def count(self,proxy):
        return self.db.zcount(REDIS_KEY,proxy)

    def all(self):
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)

if __name__ == "__main__":
    client = RedisClient()