
import csv
import pdfkit
import time
import numpy as np
import image
import requests
import bs4
from selenium import webdriver
import re
import os
import gc



"""将网页url生成pdf文件"""
config = pdfkit.configuration(
    wkhtmltopdf=r"H:\\BaiduYunDownload\\1.00\\wkhtmltox64\\wkhtmltox\\bin\\wkhtmltopdf.exe")
"""设置输出pdf的格式"""
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
   # 'outline',
   # 'outline-depth',
}
"""将数组中字典变为url数组"""
"""
url_title=[]
for i in url_title_lst:
    url_title.append(i['url'])
print(url_title)
"""
"""传入url数组，打印输出文件名为out的pdf"""

#with open('out.csv','r') as f:
#   reader =list(csv.reader(f)):
#    for url,title in reader[1:]:
#url = np.loadtxt('out.csv',delimiter=",",skiprows=1)
#print(url)
#toc = {

#    'xsl-style-sheet': 'out.csv'
#}
"""读取csv文件中的内容为数组包含数组的格式，csv文件名为out.csv"""
""",encoding='UTF-8'"""

csvrows =[]
csvFileobj = open('out3.csv','r')
readerobj = csv.reader(csvFileobj)
for row in readerobj:
    if readerobj.line_num == 1:
        continue
    csvrows.append(row)
csvFileobj.close()
print(csvrows)
#cover = 'out.csv'

"""提取数组中某一列"""

url = [x[1] for x in csvrows]
print(url)

"""输出pdf文件名为out.pdf"""

"""处理html，使图片显示"""

chrome_driver = r"C:\Users\jiansi\PycharmProjects\jiansidata\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

"""定义一个selenium爬取单个动态页面生成加载完毕的html文件的函数"""

"""从某个url链接获得链接里的html源代码"""
def get_html(link):

    driver.get(link)
    driver.maximize_window()

#i = 100

    for i in range(2, 110):  # 也可以设置一个较大的数，一下到底
            js = "var q=document.documentElement.scrollTop={}".format(i * 100)  # javascript语句
            driver.execute_script(js)

    html1 = driver.execute_script("return document.documentElement.outerHTML")
    time.sleep(2)
    driver.close()
    #print(html1)
    return html1


"""将源代码里的某些字符替换，实现懒加载图片的成功下载"""


def replace_text(ht):
    html2 = ht.replace('tp=webp&amp;', '')
    #print(html2)
    return html2

"""新建txt文件，并将html源代码写入txt文件"""


def new_txt(html3):

    f = open("test4.txt", "a+", encoding='utf-8')

    f.write(html3)
    f.close()


"""将txt文件后缀改为html文件"""


def change_suffix():
    files = os.listdir('.')
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] == '.txt':
            newname = portion[0] + '.html'
            os.rename(filename, newname)

#html1 = get_html(link)
#html2 = replace_text(html1)
#for link in url:
    #get_html(link)
    #html1 = get_html(link)
html1 = get_html(url[0])
replace_text(html1)
html1 = replace_text(html1)
new_txt(html1)

#gc.collect()
"""
#for link in url:
for index in range(len(url)):

    get_html(url[index])
    html1 = get_html(url[index])
    replace_text(html1)
    html1 = replace_text(html1)
    new_txt(html1)
    #gc.collect()
"""

change_suffix()


#get_html(url[1])
#replace_text(get_html(url[1]))
#html = html2




"""
def save_html(file_name, file_content):
    with open(file_name.replace('/', '_')+".html", "wb")as f:
        file_content = file_content.decode("UTF-8")
        f.write(file_content)
"""

#html = get_html(url[1])
#save_html("test4", html)

pdfkit.from_file("test4.html", 'out2.pdf',
                 configuration=config,
                 options=options,
                 )


"""
    pdfkit.from_file('test3.html','out2.pdf',
                    configuration = config,
                    options = options,
                    )
"""

#html.replace('&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1','')

#text= ''.join(pre.findall(html))
#soup = bs4.BeautifulSoup(res.text)
#print(html)
#print(soup)



"""
pdfkit.from_url(url,
                'out.pdf',
                configuration=config,
                options=options,
               # toc=toc,
                #cover=cover,
                )
"""
"""
pdfkit.from_string(html,
                'out.pdf',
                configuration=config,
                options=options,
               # toc=toc,
                #cover=cover,
                )
"""
"""
pdfkit.from_file('test3.html','out2.pdf',
                configuration = config,
                options = options,
                )
"""