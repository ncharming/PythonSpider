from __future__ import unicode_literals
import itchat
import time
import requests


def get_news():
    #金山词霸开发api:json数据
    url = 'http://open.iciba.com/dsapi'
    r = requests.get(url)
    #获取每日一句
    contents = r.json()['content']
    #获取每日一句的翻译
    translation = r.json()['translation']

    return contents, translation


def send_news():
    try:
        #自动给你弹出二维码登录
        itchat.auto_login()
        #查找你的好友（name=u'好友备注'） u：表示unicode字符串
        my_friend = itchat.search_friends(name=u'LLY')
        ifriend = my_friend[0]['UserName']


        #获取要发送的信息
        message1 = str(get_news()[0])
        content = str(get_news()[1][5:])
        message2 = str(content)
        message3 = '来自你的朋友'

        itchat.send(message1, toUserName=ifriend)
        itchat.send(message2, toUserName=ifriend)
        itchat.send(message3, toUserName=ifriend)
    except:
        message4 = u'你的朋友'
        itchat.send(message4, toUserName=ifriend)


def main():
    send_news()


if __name__ == '__main__':
    main()
