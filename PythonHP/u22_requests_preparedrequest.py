from requests import Request,Session

url = 'http://httpbin.org/post'
data = {
	'name':'germey'
}
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
s = Session()
req = Request('POST',url,data = data,headers = headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
