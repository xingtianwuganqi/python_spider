from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
import time
from lxml import etree
import pymongo

from pyquery import PyQuery as pq

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
KEYWORD = 'iPad'
currentPage = 1




def get_detail(page):
    print('正在抓取的页码数：',page)
    try:
        browser.get('https://s.taobao.com/search?q='+ quote(KEYWORD))
        print('https://s.taobao.com/search?q='+ quote(KEYWORD))
        # submit = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@class="login-switch"]')))
        # submit.click()
        #
        # time.sleep(1)
        # input_name = wait.until(EC.presence_of_element_located((By.ID,'TPL_username_1')))
        # input_pswd = wait.until(EC.presence_of_element_located((By.ID,'TPL_password_1')))
        # input_name.send_keys('13689242201')
        # input_pswd.send_keys('tbtb787878')
        time.sleep(10)

        if page > 1:
#       失败的例子，选择器基础知识还不熟练
        # input = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="mainsrp-pager"]/div[@class="form"]/input[@class="input J_Input"]')))
        # submit = wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@class="mainsrp-pager"]/div[@class="form"]/span[@class="btn J_Submit]')))

            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
            time.sleep(4)
            print('点击成功')

        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active > span'),str(page))) # 等待指定的文本出现在某个节点里面时即返回成功
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item'))) # 直到这个几点出现，才执行get_products() 方法

        return get_products()

    except TimeoutException:
        print('超市')
        get_detail(page)

def get_products():
    html = browser.page_source
    # html = etree.HTML(html)
    # result = etree.tostring(html)
    # products = html.xpath('//div[@class="grid g-clearfix"]/div[@class="items"]')
    # for product in products:
    #     content2 = etree.tostring(product, method='html')
    #     print(content2)
    doc = pq(html)
    items = doc('#mainsrp-itemlist .grid.g-clearfix .items .item').items()
    productss = []
    for item in items:
        # print(item)
        product = {
            'img' : item.find('.pic .pic-link .J_ItemPic.img').attr("data-src"),
            'price': item.find('.price').text().rstrip("\n"),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop .shopname').text(),
            'location':item.find('.location').text()
        }
        print(product)
        productss.append(product)
        # save_mongoDB(product)

    print('为什么是空的',productss)
    return productss


def save_mongoDB(data):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.taobao
    collections = db.products
    try:
        collections.insert_many(data)
        # collections.insert_one(data)
        print('存储成功')
    except:
        print('存储到MongoDB 失败')


def main():
    for i in range(1,5):
        products = get_detail(i)
        save_mongoDB(products)

if __name__ == "__main__":
    main()