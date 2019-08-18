from pyquery import PyQuery as pq 
import requests

html = '''
<div id="container">
<div class="hp-topbarNav-bd">
	<title>The Dormouse's story</title>
	<a href="javascript:void(0)" class="hp-set">关注虎扑</a>
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
</div>
'''
# 字符串初始化
doc = pq(html)
print(doc("li"))

# url 初始化
# doc1 = pq(url='https://cuiqingcai.com')
# print(doc1('title'))

# doc2 = pq(requests.get('https://cuiqingcai.com').text) # 与doc1 相同
# print(doc2('title'))

# 文件初始化
# doc3 = pq(filename='demo.html')
# print(doc3('li'))

# css 选择器
print(doc('#container .hp-quickNav li')) # 取到id 是container class 是hp-quickNav 里的 节点是 li 的内容
print(type(doc('#container .hp-quickNav li')))

# 查找节点
items = doc('.hp-quickNav')
print(type(items))
print(items)

lis = items.find('li')  #查找所有的子孙节点
print(type(lis))
print(lis)

liss = items.children() # 查找子节点
print(type(liss))
print(liss)

active = items.children('.mobileWeb') # 查找具体的某个节点
print(active)


# 父节点
items1 = doc('.hp-quickNav')
container = items1.parent() # 查找该节点的直接父节点
print(container)

# 所有父节点

items2 = doc('.mobileWeb')
parents = items2.parents()  #返回所有的父节点
print('所有父节点',parents)

# 返回具体的某个父节点
print('具体的父节点',items2.parents('.hp-topbarNav-bd'))
print('具体的父节点',items2.parents('div'))

# 兄弟节点

li = doc('#container .hp-quickNav .mobileclientDown')
print('兄弟节点',li.siblings())

li3 =doc('#container .hp-quickNav .mobileWeb') 
print('具体的某个节点',li3.siblings('.hp-dropDownMenu.topFollowBlog')) # 具体的某个兄弟节点

# 遍历
lis3 = doc('li').items() # items() 会得到一个生成器
print(type(lis3))
print(lis3)
for li in lis3:
	print(li)

# 获取信息
atts = doc('.hp-dropDownMenu.topFollowBlog a') # 获取a标签
print(atts.attr('href'))
print(atts.attr.href)

# 获取所有a 标签
a = doc('li')
print(a)
print(a.attr('class')) # attr 只会得到第一个属性
print(a.attr.href)

#  要获取所有 a 标签的属性 ，需要遍历
for i in doc('li').items():
	print(i.attr.class_)

# 获取文本
aa = doc('a')
print('aa 标签的文字',aa.text()) # 返回一个字符串， 是把所有的a 节点的字符串拼成一个字符串

# 获取节点内的html 文本
ht = doc('li').html()
print(ht) # 返回第一个 li 标签里的html 文本

# 节点操作

# remove()
aas = doc('ul')
print('ul 标签的文字',aas.text())
aas.find('a').remove()
print('删除微博',aas.text())

li4 = doc('.hp-topbarNav-bd .hp-quickNav')
print('删除',li4.removeClass('hp-quickNav'))
print('添加',li4.addClass('hp-quickNav')) # 可以动态改变class 的属性

# 添加text  attr html
print(li4.attr('name','link'))
print(li4.text('change item'))
print(li4.html('<span>change item</span>'))  # 不传参数 获取值 ，传参 赋值

#伪类选择器
li = doc('li:first-child') # 第一个li节点
print(li)
li = doc('li:last-child')# 最后一个li节点
print(li)
li = doc('li:nth-child(2)') # 第二个li 节点
print(li) 
li = doc('li:gt(2)') #第三个 li 节点之后的li 节点
print(li)
li = doc('li:nth-child(2n)') #偶数位置的li 节点
print(li)
li = doc('li:contains(second)') # 含有second 节点的li 节点
print(li)


