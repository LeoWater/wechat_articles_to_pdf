
import csv
import pdfkit
import time
import numpy as np
import image



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




pdfkit.from_url(url,
                'out.pdf',
                configuration=config,
                options=options,
               # toc=toc,
                #cover=cover,
                )

"""
pdfkit.from_string(html,
                'out.pdf',
                configuration=config,
                options=options,
               # toc=toc,
                #cover=cover,
                )
"""