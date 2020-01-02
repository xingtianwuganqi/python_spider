VALID_STATUS_CODES = [200]
TEST_URL = "http://www.beiwo888.com"
BATCH_TEST_SIZE = 20

import asyncio
import ssl
from ipcontent.RedisClient import RedisClient
import aiohttp
import time


class Tester():

    def __init__(self):
        self.redis = RedisClient()

    async def test_single_proxy(self,proxy):


        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy,bytes):
                    proxy = proxy.decode("utf-8")
                real_proxy = "http://" + proxy
                print("real_proxy：",real_proxy)
                async with session.get(TEST_URL,proxy = real_proxy,timeout = 15) as response:
                    if response.status in VALID_STATUS_CODES:
                        self.redis.max(proxy)
                        print("代理可用")
                    else:
                        self.redis.decrease(proxy)
                        print("请求响应码不合法：",proxy)
            except:
                self.redis.decrease(proxy)
                print("代理请求失败：",proxy)

    def run(self):
        '''
        测试主函数
        :return:None
        '''
        print("测试开始")
        try:
            proxies = self.redis.all()
            print(proxies)
            loop = asyncio.get_event_loop()
            # 批量测试
            for i in range(0,len(proxies),BATCH_TEST_SIZE):
                test_proxy = proxies[i:i+BATCH_TEST_SIZE]
                tasks = [self.test_single_proxy(i) for i in test_proxy]
                loop.run_until_complete(asyncio.wait(tasks))
                time.sleep(5)
        except Exception as e:
            print("测试器发生故障：",e.args)




if __name__ == "__main__":
    test = Tester()
    test.run()