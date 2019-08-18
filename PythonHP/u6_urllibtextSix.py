import http.cookiejar,urllib.request

# 读取保存的cookie
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt',ignore_discard = True,ignore_expires = True)
handles = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handles)
rsponse = opener.open('http://www.baidu.com')
print(rsponse.read().decode('utf8'))

