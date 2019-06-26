# -*- coding: utf-8 -*-
"""
 @Time: 2019/6/26 13:59
"""

# encoding:utf-8
# import html2text
import requests
import time
import re
from readability.readability import Document


url = "http://world.huanqiu.com/exclusive/2016-07/9209839.html"
# res = requests.get('http://finance.sina.com.cn/roll/2019-02-12/doc-ihrfqzka5034116.shtml')
res = requests.get(url)

st = time.time()
d = Document(res.content)

# 获取新闻标题
readable_title = d.short_title()
print(readable_title)
# 获取内容并清洗
readable_article = d.summary()
# print(readable_article)

print(d.get_clean_html())

print("time: {}".format(time.time() - st))

# text_p = re.sub(r'</?div.*?>', '', readable_article)
# text_p = re.sub(r'((</p>)?<a href=.*?>|</a>(<p>)?)', '', text_p)
# text_p = re.sub(r'<select>.*?</select>', '', text_p)
# print(text_p)
