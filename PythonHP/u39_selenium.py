from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains # 动作链相关库
import time

# browser = webdriver.Chrome()  # 声明浏览器对象
# try:
#     browser.get('http://www.baidu.com') # 访问页面
#     input = browser.find_element_by_id('kw') # 查找节点
#     input.send_keys('Python') #
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser,10)
#     wait.until(EC.presence_of_element_located((By.ID,'content_left')))
#     # print(browser.current_url)
#     # print(browser.get_cookies())
#     # print(browser.page_source)
# finally:
#     browser.close()

# 查找节点
# bro = webdriver.Chrome()
# try:
#     bro.get('https://www.taobao.com')
#     input = bro.find_element_by_id('q')
#
#
#     # 单个节点查询
#     inputT = bro.find_element_by_xpath('//*[@id="q"]')
#     inputO = bro.find_element_by_css_selector('#q')
#
#     inputY = bro.find_element(By.ID,'q') # 这几个方法是一样的
#
#     # print(input,inputT,inputO,inputY)
#
#     # 查找多个节点 find_elements
#     more_li = bro.find_elements_by_xpath('//*[@class="service-bd"]/li')
#     more_lis = bro.find_elements_by_css_selector('.service-bd li')
#     print(more_li ,"==========",more_lis)
#
#     # 节点交互
#     inputs = bro.find_element_by_id('q')
#     inputs.send_keys('保暖内衣')
#     time.sleep(1)
#     inputs.clear()
#     inputs.send_keys('内衣')
#     button = bro.find_element_by_class_name('btn-search')
#     button.click()
# except:
#     print('查询失败')

# time.sleep(5)
# bro.close()

# 动作链
# bor = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# try:
#     bor.get(url)
#     bor.switch_to.frame('iframeResult')
#     source = bor.find_element_by_css_selector('#draggable')
#     target = bor.find_element_by_css_selector('#droppable')
#     actions = ActionChains(bor)
#     actions.drag_and_drop(source,target)
#     actions.perform()
# except:
#     print('拖拽失败')
# bor.close()


# 执行javaScript
# brow = webdriver.Chrome()
# brow.get('https://www.zhihu.com/explore')
# brow.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# brow.execute_script('alert("To Bottom")')

# 获取节点属性
brow = webdriver.Chrome()
brow.implicitly_wait(10) #隐式等待
brow.get('https://www.zhihu.com/explore')
logo = brow.find_element_by_id('zh-top-link-logo') # 获取属性
print(logo)
print(logo.get_attribute('class'))

inputs = brow.find_element_by_class_name('zu-top-add-question') # 获取文本值
print(inputs.text)



# 获取id,位置，标签名和大小

print(inputs.id)
print(inputs.location)
print(inputs.tag_name)
print(inputs.size)

# # 页面中有子Frame时，如果想获取子frame 中的节点，需先调用switch_to.frame() 切换到对应的frame ，再进行操作
# brow.close()
# browe = webdriver.Chrome()
# browe.get('https://www.taobao.com/')
# wait = WebDriverWait(browe,10)
# input = wait.until(EC.presence_of_element_located((By.ID,'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
# print(input,button)
# browe.close()
# # 前进和后退
# browe = webdriver.Chrome()
# browe.get('https://www.baidu.com/')
# browe.get('https://www.taobao.com/')
# browe.get('https://www.python.org')
# browe.back()
# time.sleep(1)
# browe.forward()
# browe.close()

# Cookies
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name':'name','domain':'domain','value':'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

# 选项卡管理
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    browser.execute_script('window.open()')
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://www.taobao.com')
    time.sleep(1)
    browser.execute_script('window.open()') # 打开选项卡
    browser.switch_to.window(browser.window_handles[2]) #切换到选项卡，下标切换
    browser.get('https://www.python.org')
    browser.find_element_by_id('hello')
except:
    print("打开失败")
finally:
    browser.close()








