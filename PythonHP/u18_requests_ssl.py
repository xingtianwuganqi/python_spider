import requests
# from requests.packages import urllib3
import logging

#忽略警告
# urllib3.disable_warnings()

#或者通过捕获警告到日志的方式忽略警告
logging.captureWarnings(True)

response = requests.get('https://www.12306.cn',verify = False)
print(response.status_code)