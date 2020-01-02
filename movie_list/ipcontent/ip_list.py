TESTER_CYCLE = 20
GETTER_CYCLE = 20
GETTER_ENABLED = False
TESTER_ENABLED = False
API_ENABLED = True

API_HOST = '0.0.0.0'
API_PORT = 5000

from multiprocessing import Process
from ipcontent.Flask_test import app
from ipcontent.ip_list_network import IPNetWorking
from ipcontent.RedisClient import RedisClient
from ipcontent.Tester import Tester
import time
import requests

PROXY_POOL_URL = 'http://localhost:5000/random'


class Scheduler():
    def scheduler_getter(self,cycle = GETTER_CYCLE):
        getter = IPNetWorking()
        while True:
            getter.main()
            time.sleep(5)

    def scheduler_test(self,cycle = TESTER_CYCLE):
        test = Tester()
        while True:
            test.run()

    def scheduler_api(self):
        app.run(API_HOST,API_PORT)

    def run(self):
        print("代理池开始运行")
        if GETTER_ENABLED:
            getter_process = Process(target=self.scheduler_getter())
            getter_process.start()

        if TESTER_ENABLED:
            tester_process = Process(target=self.scheduler_test())
            tester_process.start()

        if API_ENABLED:
            api_process = Process(target=self.scheduler_api())
            api_process.start()

    def get_proxy(self):
        try:
            response = requests.get(PROXY_POOL_URL)
            if response.status_code == 200:
                print(response.text)
                return response.text
            else:
                return None
        except ConnectionError:
            return None

if __name__ == "__main__":
    scheduler = Scheduler()
    # scheduler.run()
    txt = scheduler.get_proxy()
    print(txt)