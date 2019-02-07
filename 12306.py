# -*- coding: utf-8 -*-
# 需要截获异步加载的信息
import urllib
import json
import ssl

ssl.create_default_https_context = ssl._create_stdlib_context

def getlist():
    req = urllib.urlopen('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E9%99%87%E5%8D%97,INJ&ts=%E5%85%B0%E5%B7%9E,LZJ&date=2019-02-23&flag=N,N,Y')
    html = req.read()
    dict_html = json.loads(html)
    return dict_html['data']

for i in getlist():
    print("i")