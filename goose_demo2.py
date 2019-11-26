# -*- coding: utf-8 -*-
"""
 @Time: 2019/6/21 13:54
"""

import time
import os
import sys

# import urllib2
import goose
from goose.text import StopWordsChinese

# url = "http://www.sohu.com/a/299667318_501931"
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
# response = opener.open(url)
# raw_html = response.read()

import codecs
with codecs.open('test.html', 'r', encoding='utf-8') as f:
    raw_html = f.read()

g = goose.Goose({'stopwords_class': StopWordsChinese})
a = g.extract(raw_html=raw_html)
print(a.infos)
print(a.title)
print("--"*20)
print(a.cleaned_text)