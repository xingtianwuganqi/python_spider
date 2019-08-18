import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)
for key,value in r.cookies.items():
	print(key + " = " + value)


#登录知乎并获取text

headers = {
	'Cookie': 'd_c0="AGCC2O75YAuPTj1qCHhZ_-M3RzoW1xQroNg=|1488266530"; _zap=bca2c60a-cf1a-44e5-aa37-2c2b9732616c; __utmv=51854390.100--|2=registration_date=20170319=1^3=entry_date=20170228=1; q_c1=87b6c63509e342f08298a1860f1fb350|1508853078000|1488266530000; __DAYU_PP=ENbeqI7uff7YZ3aFrrm7ffffffff8776d59e1048; z_c0="2|1:0|10:1527088184|4:z_c0|92:Mi4xZ01SeEJBQUFBQUFBWUlMWTd2bGdDeVlBQUFCZ0FsVk5PTkx5V3dBUlFkTXY4OVpSZk1oYnltRmlqUjRDSnhUNlhR|a95fbf48f8e5c2c2ca7c4e8075ec9187a5602f4b52cc6cb73fef5e67c17fc7d7"; _xsrf=EjfYfExGSwAXtOOtwanlM02qXaYvDYvW; q_c1=87b6c63509e342f08298a1860f1fb350|1541426291000|1488266530000; __utmc=51854390; __utma=51854390.1526938544.1488266531.1541426295.1541429615.6; __utmz=51854390.1541429615.6.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/xiang-cheng-wei-da-niu-de-ma-nong/activities; tst=r; tgw_l7_route=23ddf1acd85bb5988efef95d7382daa0',
	'Host': 'www.zhihu.com',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
r = requests.get('https://www.zhihu.com',headers = headers)
# print(r.text)

# 另一种写法，通过cookies参数，构造RequestsCookieJar 对象，
cookies = 'd_c0="AGCC2O75YAuPTj1qCHhZ_-M3RzoW1xQroNg=|1488266530"; _zap=bca2c60a-cf1a-44e5-aa37-2c2b9732616c; __utmv=51854390.100--|2=registration_date=20170319=1^3=entry_date=20170228=1; q_c1=87b6c63509e342f08298a1860f1fb350|1508853078000|1488266530000; __DAYU_PP=ENbeqI7uff7YZ3aFrrm7ffffffff8776d59e1048; z_c0="2|1:0|10:1527088184|4:z_c0|92:Mi4xZ01SeEJBQUFBQUFBWUlMWTd2bGdDeVlBQUFCZ0FsVk5PTkx5V3dBUlFkTXY4OVpSZk1oYnltRmlqUjRDSnhUNlhR|a95fbf48f8e5c2c2ca7c4e8075ec9187a5602f4b52cc6cb73fef5e67c17fc7d7"; _xsrf=EjfYfExGSwAXtOOtwanlM02qXaYvDYvW; q_c1=87b6c63509e342f08298a1860f1fb350|1541426291000|1488266530000; __utmc=51854390; __utma=51854390.1526938544.1488266531.1541426295.1541429615.6; __utmz=51854390.1541429615.6.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/xiang-cheng-wei-da-niu-de-ma-nong/activities; tst=r; tgw_l7_route=23ddf1acd85bb5988efef95d7382daa0'
jar = requests.cookies.RequestsCookieJar()
headerss = {
	'Host': 'www.zhihu.com',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
for cookie in cookies.split(';'):
	key,value = cookie.split('=',1)
	jar.set(key,value)

rs = requests.get('https://www.zhihu.com',cookies = jar,headers = headerss)
print(r.text)
