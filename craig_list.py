# 用于打开chrome读取网页，分析源代码
from selenium import webdriver
#导入网页解析库，借助网页的结构和属性来解析网页，方便我们从中提取数据
from bs4 import BeautifulSoup
#导入HTTP请求库，此处主要用reque模块来模拟发送请求，相当于点击了链接；Python3中不包含urllib2这个库，统一为urllib库
import urllib
#导入正则表达式的库，用于处理字符串
import re
import pandas as pd
import numpy as np
# 因为url中的头文件为https，需要import ssl 支持加密链接抓取
import ssl
from urllib.request import urlopen
pd.set_option('max_colwidth', 5000)
pd.options.display.max_rows = 999
#导入IPython库，用来显示数据；他包含在强大的Jupyter库中
from IPython.display import display, HTML
# 把下载的Chromedriver文件移动到/usr/local/bin目录里面，以后使用Chrome()就不用添加环境变量。
driver = webdriver.Chrome()

#Python注意缩进，他也是程序语言的一部分
def craig_list(price, location_list=list):
    '''
    craig_list 是一个创建精简版Craigslist帖子信息的函数
    输入：
         price_max: 想要的房屋的最高价格的整数
         place: 字符串列表，其中字符串表示选择的区域
    输出：
        带有描述和链接的数据
    '''
    craig_title = []
    link_list = []
    #此处for循环一直到pd.DataFrame函数
    for place in location_list:
        print('------MOVING TO PLACE' + str(place) + '-------')
        link_list.append(' ')
        craig_title.append(str(place))
        url = 'https://sfbay.craigslist.org/search/roo?lang=zh&query=' + \
        str(place) + '&max_price=' + str(price) + '&availabilityMode=0'
        # 抓取第一个页面的标题和链接
        driver.get(url)
        # chrome查看源码，可以发现所需结果都在<li class = "result-row">...</li>所在区域
        all_posts = driver.find_elements_by_class_name('result-row')
        for post in all_posts:
            craig_title.append(post.text)
        # 移动到第二个页面，抓取这个页面的标题和链接，处理加密链接
        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        html_page = urlopen(url, context=gcontext)
        #解析urllib库点击的链接
        soup = BeautifulSoup(html_page, 'lxml')
        for pid in soup.find_all('a', attrs={'class': 'result-title hdrlnk'}):
            link_list.append(pid['href'])
    craig_df = pd.DataFrame(np.column_stack([craig_title, link_list]),
                            columns=['Info', 'Link'])
    return craig_df


places = ['glen+park', "balboa+park"]
price_max = 900
craig_df = craig_list(price_max, places)
display(craig_df)
