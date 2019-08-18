import http.cookiejar,urllib.request

#cookie
# cookie = http.cookiejar.CookieJar()
# handle = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handle)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
# 	print(item.name+ " = " + item.value)

# 将cookie保存到文件中
filename = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar(filename)           #MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard = True,ignore_expires = True)
