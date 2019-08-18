import requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://localhost:5000',auth = HTTPBasicAuth('username','password'))
#还可以这样写
s = requests.get('http://hocalhost:5000',auth = ('username','password'))
print(r.status.code)