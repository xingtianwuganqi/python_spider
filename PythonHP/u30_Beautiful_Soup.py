from bs4 import BeautifulSoup
import re
# soup = BeautifulSoup('<p>Hello</p>','lxml')
# print(soup.p.string)

html = '''
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
'''
soup = BeautifulSoup(html,'lxml')
print(soup.prettify()) # 将解析的字符串以标准的缩进格式输出（自动更正格式）
print(soup.title.string) # 输出title节点的文本内容

# 节点选择器 tag
print(type(soup.title)) # soup.title 的类型
print(soup.li) # li 节点
print(soup.a)
print(soup.a.string)

# 提取信息
print(soup.title.name) # title  节点的名称 为title
print(soup.a.attrs) # 获取节点a 的属性
print(soup.a.attrs['href']) #  获取具体的某个属性的值
print(soup.li['class']) # 获取节点属性
print(soup.a.string)

# 嵌套选择
print(soup.div.a)
print(soup.div.a.string)

html1 = '''
<html><head><title>The Dormouse's story</title></head></html>
'''
soup1 = BeautifulSoup(html1,'lxml')
print(soup1.head.title)
print(soup1.head.title.string)
print(type(soup1.head.title))

# 关联选择
print(soup.div.contents)  # contents 方法得到直接子节点的列表
 # 使用children 属性获取
print(soup.div.children) # 返回的生成器类型
for i in enumerate(soup.div.children):
	print(i)

print(soup.div.descendants) # 获取所有的子孙节点
for i,children in enumerate(soup.div.descendants):
	print(i,children)

# 获取父节点
print(soup.li.parent) # 直接父节点
print(soup.li.parents) #  获取所有祖先节点
print(list(enumerate(soup.li.parents)))

# 获取兄弟节点
print('next sibling',soup.a.next_sibling) # 节点的下一个节点
print('prev sibling',soup.a.previous_sibling) # 节点的上一个节点
print('next siblings',list(enumerate(soup.a.next_siblings))) # 所有的下一个节点
print('prev siblings',list(enumerate(soup.a.previous_siblings))) # 所有的上节点

# 提取信息
print('title sibling: ',soup.title.next_sibling)
print('title sibling string: ',soup.title.next_sibling.string)

print(list(soup.li.parents)[0])
print(list(soup.li.parents)[0].attrs['class']) # 获取属性

#  方法选择器
# find.all(name,attrs,recursive,text, **kwargs)

# 1.根据节点名查询元素
print(soup.find_all(name='a')) 
for i in soup.find_all(name='li'):
	print(i.find_all(name='a'))

# 2.传入属性
print(soup.find_all(attrs={'class': 'mobileWeb'})) # 参数是字典类型

print(soup.find_all(class_='mobileWeb'))
print(soup.find_all(target="_blank"))

# 3.匹配节点文本 传入的可以是字符串，也可以是正则表达式
print(soup.find_all(text=re.compile('虎扑')))

# find() 方法 返回单个元素
print(soup.find('a'))
print(soup.find(attrs = {'class':'line'}))

# find_parents() find_parent()
# find_next_siblings() find_next_sibling()
# find_previous_siblings()  find_previous_sibling()
# find_all_next() find_next()
# find_all_previous() find_previous()
# 返回所有（） 节点 ，返回第一个（） 节点

# css 选择器
print(soup.select('ul li')) # 返回ul标签下的li 标签
print(soup.select('.hp-quickNav .mobileWeb')) #  两个属性的 key相同时
print(soup.select('.mobileclientDown ._blank')) # key 不同时 是空
print(soup.select('.mobileWeb .ico-mobile'))

# 嵌套结构
for i in soup.select('ul'):
	print(i.select('li'))

# 获取属性
for i in soup.select('li'):
	print(i['class'])
	print(i.attrs['class'])

# 获取文本
for li in soup.select('li'):
	print(li.get_text())
	print(li.string)



