# coding:utf-8
from bs4 import BeautifulSoup
import requests


def yingyonghui_crawler(name):
    url = 'http://www.appchina.com/sou/?keyword='+name
    web_data = requests.get(url)
    
    #.text：直接是网页源代码
    #print(web_data.text)：将整个网页源代码打印出来
    soup = BeautifulSoup(web_data.text, 'lxml')
    title = soup.select(
        'ul > li > div.app-info > h1 > a')[0].get_text()
    times = soup.select(
        'ul > li > div.app-info > span.download-count')[0].get_text()[6:12]
    print('在应用汇上,'+title+'下载量为：'+times)


def zhushou_crawler(name):
    url = 'http://zhushou.360.cn/search/index/?kw='+name
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'lxml')
    title = soup.select(
        'body > div.warp > div.main > div > ul > li > dl > dd > h3 > a')[0].get_text()
    times = soup.select(
        'body > div.warp > div.main > div > ul > li > div > div.sdlft > p.downNum')[0].get_text()[:-2]
    print('在360助手上，'+title+'下载量为：'+times)


name = input('请输入想搜索的应用名：')
yingyonghui_crawler(name)
zhushou_crawler(name)
