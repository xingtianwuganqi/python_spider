e
text = '''
<div class="hp-topbarNav-bd">
                                <ul class="hp-quickNav">
                                    <li class="mobileWeb"><a href="javascript:void(0)" onclick="hp_quick_touch()"><i class="ico-mobile"></i>手机虎扑</a></li>
                                    <li class="line">|</li>
                                    <li class="mobileclientDown"><a class="red" href="https://mobile.hupu.com/?_r=globalNav" target="_blank">虎扑客户端</a></li>
                                    <li class="line">|</li>
                                    <li class="hp-dropDownMenu topFollowBlog">
                                        <a href="javascript:void(0)" class="hp-set">关注虎扑<s class="setArrow"></s></a>
                                        <div class="hp-drapDown followLayer">
                                            <a class="weibo" target="_blank" rel="nofollow" href="//weibo.com/liangle4u"><i class="hp-ico-weibo"></i>新浪微博</a>
											<a class="weixin" target="_blank" href="https://voice.hupu.com/other/1581560.html"><i class="hp-ico-weixin"></i>官方微信</a>
                                            <a class="instagram" target="_blank" rel="nofollow" href="https://voice.hupu.com/other/1634334.html"><i class="hp-ico-instagram"></i>Instagram</a>
                                        </div>
                                    </li>
                                </ul>
                                <div class="hp-topLogin-info"></div>
                            </div>
'''

html = etree.HTML(text)

# html = etree.parse('./text.html',etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
results = html.xpath('//*')#所有节点
print(results)
result2 = html.xpath('//li')#所有li节点
print(result2)
result3 = html.xpath('//li/a')# li节点下的a节点
print(result3)
result4 = html.xpath('//ul//a')# ul节点下的a节点
print(result4)

#父节点
result5 = html.xpath('//a[@href="//weibo.com/liangle4u"]/../@class') # a 节点中href="//weibo.com/liangle4u" 父节点的class属性
print(result5)
result6 = html.xpath('//a[@href="//weibo.com/liangle4u"]/parent::*/@class')#两个一样
print(result6)
# 属性匹配
result7 = html.xpath('//li[@class="line"]')
print(result7)
#获取文本
result8 = html.xpath('//li[@class="mobileWeb"]/a/text()')
print(result8)
result9 = html.xpath('//li[@class="mobileWeb"]//text()')
print(result9)
# 属性获取
result10 = html.xpath('//li/a/@class')
print(result10)
# 属性多值匹配
# 有时候，某些节点的某个属性可能有多个值
text1 = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html1 = etree.HTML(text1)
result11 = html1.xpath('//li[@class="li"]/a/text()') # 无法获得值
print(result11)

# 属性多值匹配
result12 = html1.xpath('//li[contains(@class,"li")]/a/text()')
print(result12)

# 多属性匹配
text2 = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html2 = etree.HTML(text2)
result13 = html2.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(result13)

# 按序选择
result14 = html.xpath('//div/a/@class')
print(result14)

result15 = html.xpath('//li[1]/@class')
print(result15)
result16 = html.xpath('//li[last()]/@class')
print(result16)
result17 = html.xpath('//li[position()<3]/@class')
print(result17)
result18 = html.xpath('//li[last()-2]/@class')
print(result18)

# 节点轴
result19 = html.xpath('//li[1]/ancestor::*') # 所有祖先节点
print(result19)
result20 = html.xpath('//li[1]/ancestor::div') # 祖先节点div
print(result20)
result21 = html.xpath('//li[1]/a[1]/attribute::*') # 获取所有属性
print(result21)
result22 = html.xpath('//li[1]/child::a[@href="javascript:void(0)"]') #子节点中 的 a 的 href 属性
print(result22)
result23 = html.xpath('//li[1]/descendant::a')# 获取子节点 a
print(result23)
result24 = html.xpath('//li[1]/following-sibling::*') # 当前节点之后的全部同级节点
print(result24)
result25 = html.xpath('//li[1]/following::*[2]') # 获取当前节点之后的所有节点中的第二个节点
print(result25)
