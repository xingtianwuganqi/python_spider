#match() 方法

import re

content= 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))


#match()方法，向它传入要匹配的字符串以及正则表达式，就可以监测这个正则表达式是否匹配字符串

result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
print(result)
print(result.group())
print(result.span())

#匹配方法

contents = 'Hello 1234567 World_This is a Regex Demo'
results = re.match('^Hello\s(\d+)\sWorld(\w+)',contents)
print(results)
print(results.group())
print(results.group(1)) #1 2  用来输出正则表达式括号中的内容
print(results.group(2))
print(results.span())

# .* 的用法   .表示可以匹配任意字符（除换行符） * 表示匹配前面的字符无限次

resultss = re.match('^Hello.*Demo$',content)
print(resultss)
print(resultss.group())
print(resultss.span())

#  贪婪与非贪婪  (贪婪匹配是尽可能匹配多的字符 .* ，非贪婪匹配是尽可能匹配少的字符 .*?)
resu = re.match('^Hello.*(\d+).*Demo$',contents)
print(resu)
print(resu.group(1))
print(resu.span())

resul = re.match('^Hello.*?(\d+).*Demo$',contents)
print(resul)
print(resul.group(1))
print(resul.span())


#在末尾，用.*? 可能会匹配不到内容

cont = 'http://www.weibo.com/content/Eroor'
result1 = re.match('^http:.*?content(.*?)',cont)
result2 = re.match('^http:.*?content(.*)',cont)
print('result1',result1.group(1))
print('result2',result2.group(1))

# 修饰符  re.S 使.匹配包括换行符在内的所有字符
con = '''Hello 1234567 World_This
is a Regex Demo
'''
result3 = re.match('^He.*?(\d+).*?Demo$',con,re.S)
print(result3.group(1))

# 转义匹配 .用来匹配任意字符， 字符串中有.的时候
content1 = '(百度)www.baidu.com'
result4 = re.match('\(百度\)www\.baidu\.com',content1)
print(result4)

# search()
content2 = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
result5 = re.search('Hello.*?(\d+).*?Demo',content2)
print(result5)

content3 = '''<ul>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.qianqian.com/ugcdiy/pic/e6ebf45c0475e1278a1aaba36256ce1e.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    3679
                                            </span></div>
                    <div class="btn-bg" style="display: none;">
                        <a href="/songlist/556611433" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="556611433"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/556611433" title="金曲嘻哈天团，顽童MJ116的青春之声">金曲嘻哈天团，顽童MJ116的青春之声</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E6%AD%8C%E5%8D%95%E5%AE%9E%E9%AA%8C%E5%AE%A4" title="歌单实验室">歌单实验室</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.qianqian.com/ugcdiy/pic/d754476f91eb04f7c9f57adcc0aac2ed.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    6390
                                            </span></div>
                    <div class="btn-bg" style="display: none;">
                        <a href="/songlist/557403117" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="557403117"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/557403117" title="【华语怀旧集】似是故人来">【华语怀旧集】似是故人来</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E7%86%8A%E6%9C%ACboy" title="熊本boy">熊本boy</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.qianqian.com/ugcdiy/pic/3dc8f96e3c208986da39cedba3187b84.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    2451
                                            </span></div>
                    <div class="btn-bg" style="display: none;">
                        <a href="/songlist/557404145" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="557404145"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/557404145" title="有一种好听叫做榜上有名">有一种好听叫做榜上有名</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E6%AC%A7%E7%BE%8E%E8%80%81%E8%85%8A%E8%82%89" title="欧美老腊肉">欧美老腊肉</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.qianqian.com/ugcdiy/pic/8c5afcca33257b29d3003fe9b0adf0d6.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    5943
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/556424490" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="556424490"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/556424490" title="聆听被音乐击中的孤单心事">聆听被音乐击中的孤单心事</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E6%88%91%E6%98%AF%E4%BD%A0%E7%9A%84%E5%B0%8F%E5%AE%9D%E5%AE%9D" title="我是你的小宝宝">我是你的小宝宝</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.qianqian.com/ugcdiy/pic/91e67b42063e99a1bc157558da0d8569.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    498
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/557412788" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="557412788"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/557412788" title="好心情催化剂☻今天也要快乐鸭">好心情催化剂☻今天也要快乐鸭</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E9%BA%A6%E8%8A%BD%E7%B3%96%E7%B3%96" title="麦芽糖糖">麦芽糖糖</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.qianqian.com/ugcdiy/pic/acf30f05fb330adf86b4a594e6c8b675.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    4009
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/556591927" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="556591927"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/556591927" title="为潮流中国风打Call！">为潮流中国风打Call！</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E5%BD%93%E6%88%91%E6%83%B3%E4%BD%A0%E7%9A%84%E9%82%A3%E4%B8%80%E7%A7%92" title="当我想你的那一秒">当我想你的那一秒</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.cdn.qianqian.com/ugcdiy/pic/c8f8eba860842899a513c7baefd8759e.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    8万
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/516760155" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="516760155"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/516760155" title="百度音乐U榜第十二期热门歌曲">百度音乐U榜第十二期热门歌曲</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E5%8D%83%E5%8D%83%E9%9F%B3%E4%B9%90" title="千千音乐">千千音乐</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.qianqian.com/ugcdiy/pic/6a1a723a0fb68dd8b7a83772845fdfdc.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    49万
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/512266089" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="512266089"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/512266089" title="感性女人味|莫文蔚的优雅恋歌">感性女人味|莫文蔚的优雅恋歌</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E6%AD%8C%E5%8D%95%E5%AE%9E%E9%AA%8C%E5%AE%A4" title="歌单实验室">歌单实验室</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.cdn.qianqian.com/ugcdiy/pic/1c73c2d2276d3976251d3bfcbd00687e.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    145万
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/365310869" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="365310869"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/365310869" title="大叔的歌，唱尽人生">大叔的歌，唱尽人生</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E6%AD%8C%E5%8D%95%E5%AE%9E%E9%AA%8C%E5%AE%A4" title="歌单实验室">歌单实验室</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.cdn.qianqian.com/ugcdiy/pic/1f23499bb076ab1e364ca7df1c4c22d2.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    37万
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/512073020" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="512073020"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/512073020" title="暖心歌后郁可唯，听阳光洒进耳朵">暖心歌后郁可唯，听阳光洒进耳朵</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E6%AD%8C%E5%8D%95%E5%AE%9E%E9%AA%8C%E5%AE%A4" title="歌单实验室">歌单实验室</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.cdn.qianqian.com/ugcdiy/pic/c9123c01809b262108c277c7c474debd.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    44万
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/515032999" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="515032999"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/515032999" title="惊艳LIVE现场，超越原版的味道">惊艳LIVE现场，超越原版的味道</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E6%AD%8C%E5%8D%95%E5%AE%9E%E9%AA%8C%E5%AE%A4" title="歌单实验室">歌单实验室</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.qianqian.com/ugcdiy/pic/c0c962a834ab58f0a4f79bd648a5b2a4.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    8万
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/517529717" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="517529717"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/517529717" title="我走路带风，可以这么形容">我走路带风，可以这么形容</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E7%9C%8B%E4%B8%8D%E6%83%AF%E6%88%91%E5%B0%B1%E6%9D%A5%E6%89%93%E6%88%91%E5%95%8A" title="看不惯我就来打我啊">看不惯我就来打我啊</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.cdn.qianqian.com/ugcdiy/pic/cc99a96aa608ccf7174770e632ef22dc.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    21万
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/515739371" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="515739371"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/515739371" title="质感女声李丽芬精选集">质感女声李丽芬精选集</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E6%AD%8C%E5%8D%95%E5%AE%9E%E9%AA%8C%E5%AE%A4" title="歌单实验室">歌单实验室</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.qianqian.com/ugcdiy/pic/7801ce2bd6896e2cf487f5f5f5224572.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    18万
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/517725546" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="517725546"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/517725546" title="“甜心天使”卓文萱的浪漫音符">“甜心天使”卓文萱的浪漫音符</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E6%AD%8C%E5%8D%95%E5%AE%9E%E9%AA%8C%E5%AE%A4" title="歌单实验室">歌单实验室</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.cdn.qianqian.com/ugcdiy/pic/2dfd3b3980b496c7e5c12d9a21b87a6e.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    28万
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/365643477" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="365643477"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/365643477" title="让这些歌来教你写情书">让这些歌来教你写情书</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E6%AD%8C%E5%8D%95%E5%AE%9E%E9%AA%8C%E5%AE%A4" title="歌单实验室">歌单实验室</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.cdn.qianqian.com/ugcdiy/pic/2cf16b8d0316e257aebcd3b143e38f99.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    12万
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/498199382" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="498199382"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/498199382" title="让森林之声帮你睡个好觉">让森林之声帮你睡个好觉</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E6%9D%A5%E7%BD%9082%E5%B9%B4%E7%9A%84%E5%8F%AF%E4%B9%90%E5%90%A7" title="来罐82年的可乐吧">来罐82年的可乐吧</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://hiphotos.qianqian.com/ting/pic/item/f11f3a292df5e0fee9f2994c5f6034a85fdf7290.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    78万
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/4844" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="4844"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/4844" title="古风之男女对唱">古风之男女对唱</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E5%A4%AA%E5%90%88%E9%9F%B3%E4%B9%90%E4%BA%BA" title="太合音乐人">太合音乐人</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.cdn.qianqian.com/ugcdiy/pic/5e50946247df154ad60bf5debbbb4153.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    14万
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/365316670" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="365316670"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/365316670" title="老牌歌手的新时代">老牌歌手的新时代</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E6%AD%8C%E5%8D%95%E5%AE%9E%E9%AA%8C%E5%AE%A4" title="歌单实验室">歌单实验室</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://hiphotos.qianqian.com/ting/pic/item/d788d43f8794a4c2f9f9947109f41bd5ac6e3995.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    312万
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/6053" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="6053"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/6053" title="儿歌精选">儿歌精选</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E5%8D%83%E5%8D%83%E9%9F%B3%E4%B9%90" title="千千音乐">千千音乐</a></p>
            </li>
                        <li>
                <div class="img-wrap">
                                            <img src="http://musicugc.qianqian.com/ugcdiy/pic/415d407a739e8b653922cd537e5ef7f9.jpg@s_1,w_300,h_300">
                                        <div class="num"><i></i><span>
                                                    9万
                                            </span></div>
                    <div class="btn-bg">
                        <a href="/songlist/518116968" class="link"></a>
                        <a href="javascript:;" class="play songlist-play-hook" data-listid="518116968"></a>
                    </div>
                </div>
                <p class="text-title"><a href="/songlist/518116968" title="弹动你的神经，触动你的情怀。">弹动你的神经，触动你的情怀。</a></p>
                <p class="text-user">by<a target="_blank" href="/user?nickname=%E7%9C%8B%E4%B8%8D%E6%83%AF%E6%88%91%E5%B0%B1%E6%9D%A5%E6%89%93%E6%88%91%E5%95%8A" title="看不惯我就来打我啊">看不惯我就来打我啊</a></p>
            </li>
                    </ul>
'''
result6 = re.search('class="(.*?)".*?href="(.*?)".*?title="(.*?)"',content3,re.S)
print(result6.group(1),result6.group(2),result6.group(3))

result7 = re.findall('class="(.*?)".*?href="(.*?)".*?title="(.*?)"',content3,re.S)
print(result7)
print(type(result7))
for i in result7:
	print(i)
	print(i[0],i[1],i[2])


# sub() 修改文本信息,文本替换

content4 = '78hhugt8h873h9uu38ju8ou'
content4 = re.sub('\d+','',content4)
print(content4)

#去掉文本中的div 标签
content5 = re.sub('<div.*?>|</div>','',content3)
print(content5)

# 去掉a 标签
content6 = re.sub('<a.*?>|</a>','',content5)
print(content6)

result8 = re.findall('<p.*?>(.*?)</p>',content6,re.S)
print(result8)

# complie() 将正则字符串编译成正则表达式对象，
content7 = '2016-12-15 12:00'
content8 = '2016-12-17 12:55'
content9 = '2016-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
result9 = re.sub(pattern,'',content7)
result10 = re.sub(pattern,'',content8)
result11 = re.sub(pattern,'',content9)
print(result9,result10,result11)
