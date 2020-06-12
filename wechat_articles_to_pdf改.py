# coding: utf-8
from selenium import webdriver
import re
import time
from functools import reduce
from pprint import pprint
import pickle
import csv
import pdfkit
import image

"""
note: 需要使用selenium，chrome版本需要与chromedriver版本对应。具体见https://chromedriver.storage.googleapis.com/
"""

def login(username, password):
    #打开微信公众号登录页面
    driver.get('https://mp.weixin.qq.com/')
    driver.maximize_window()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/div[2]/a").click()
    # 自动填充帐号密码
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/div[1]/form/div[1]/div[1]/div/span/input").clear()
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/div[1]/form/div[1]/div[1]/div/span/input").send_keys(username)
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/div[1]/form/div[1]/div[2]/div/span/input").clear()
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/div[1]/form/div[1]/div[2]/div/span/input").send_keys(password)

    time.sleep(1)
    #自动点击登录按钮进行登录
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/div[1]/form/div[4]/a").click()
    # 手动拿手机扫二维码！
    time.sleep(15)

def open_link(nickname):
    # 进入新建图文素材
    driver.find_element_by_xpath('//*[@id="menuBar"]/li[5]/ul/li[3]/a/span/span').click()
    driver.find_element_by_xpath('//*[@id="js_main"]/div[3]/div[1]/div[2]/button').click()
    time.sleep(20)

    # 切换到新窗口
    for handle in driver.window_handles:
        if handle != driver.current_window_handle:
            #driver.switch_to_window(handle)
            driver.switch_to.window(handle)

    # 手动点击超链接

    time.sleep(3)
    # 点击查找文章
    driver.find_element_by_xpath('//*[@id="vue_app"]/div[5]/div[1]/div/div[2]/div[2]/form[1]/div[3]/div/div/p/button').click()
    # 输入公众号名称
    driver.find_element_by_xpath('//*[@id="vue_app"]/div[5]/div[1]/div/div[2]/div[2]/form[1]/div[3]/div/div/div/div/span/input').send_keys(nickname)
    # 点击搜索
    driver.find_element_by_xpath(
        '//*[@id="vue_app"]/div[5]/div[1]/div/div[2]/div[2]/form[1]/div[3]/div/div/div/div/span/span/button[2]').click()
    time.sleep(3)
    # 点击第一个公众号
    driver.find_element_by_xpath('//*[@id="vue_app"]/div[5]/div[1]/div/div[2]/div[2]/form[1]/div[3]/div/div/div/div[2]/ul/li[1]/div[1]/strong').click()
    time.sleep(3)
'''定义获取的url字典数据，生成带字典的数组'''
def get_url_title(html):
    lst = []
    for item in driver.find_elements_by_class_name('inner_link_article_item'):
        temp_dict = {
            'date': item.text.split('\n')[1],
            'url': item.find_element_by_tag_name('a').get_attribute('href'),
            'title': item.text.split('\n')[0],
        }
        lst.append(temp_dict)
    return lst

#用webdriver启动谷歌浏览器
chrome_driver=r"C:\Users\jiansi\PycharmProjects\jiansidata\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver)

'''需要手动输入个人微信公众号的账号，密码，要导出的公众号名称'''
nickname = '运营深度精选' # 公众号名称
username = '' # 账号
password = '' # 密码
login(username, password)
open_link(nickname)
page_num = int(driver.find_elements_by_class_name('weui-desktop-pagination__num__wrp')[-1].text.split('/')[-1])
# 点击下一页
url_title_lst = get_url_title(driver.page_source)
print(url_title_lst)
for _ in range(1, page_num):
        try:
            pagination = driver.find_elements_by_class_name('weui-desktop-pagination__nav')[-1]
            pagination.find_elements_by_tag_name('a')[-1].click()
            time.sleep(5)
            url_title_lst += get_url_title(driver.page_source)

        except:
        # 保存
            with open('data.pickle', 'wb') as f:
                pickle.dump(url_title_lst, f)
            print("第{}页失败".format(_))
            break

print(url_title_lst)

#with open('data2.pickle', 'wb') as f:
#    pickle.dump(data, f)
# 读取
#with open('data.pickle', 'rb') as f:
#    b = pickle.load(f)
'''
保存url字典到csv文件，这个似乎不行
outputFile = open('outputurl.csv','w',newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(url_title_lst)
outputFile.close()
'''
'''将url字典保存到csv文件'''
url_list = url_title_lst
with open('outputurl.csv','w',encoding="utf-8",newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['date','url', 'title'])
    writer.writeheader()
    writer.writerows(url_list)

'''将网页url生成pdf文件'''
config = pdfkit.configuration(
    wkhtmltopdf=r"H:\\BaiduYunDownload\\1.00\\wkhtmltox64\\wkhtmltox\\bin\\wkhtmltopdf.exe")
'''设置输出pdf的格式'''
options = {
    'page-size': 'A4',  # 默认是A4 Letter  etc
    'margin-top':'0.05in',   #顶部间隔
     'margin-right':'1in',   #右侧间隔
     'margin-bottom':'0.05in',   #底部间隔
     'margin-left':'1in',   #左侧间隔
    'encoding': "UTF-8",  #文本个数
    'dpi': '96',
    'image-dpi': '600',
    'image-quality': '94',
    'footer-font-size': '80',  #字体大小
    'no-outline': None,
    "zoom": '1',  # 网页放大/缩小倍数
}
'''将数组中字典变为url数组'''
url_title=[]
for i in url_title_lst:
    url_title.append(i['url'])
print(url_title)
'''传入url数组，打印输出文件名为out的pdf'''
pdfkit.from_url(url_title,
                'out.pdf',
                configuration=config,
                options=options)
