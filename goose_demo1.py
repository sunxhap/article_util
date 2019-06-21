# -*- coding: utf-8 -*-
"""
 @Time: 2019/6/21 12:07
"""

import time
import os
import sys

from goose import Goose
from goose.text import StopWordsChinese
# url = 'http://world.huanqiu.com/exclusive/2016-07/9209839.html'

# url = 'http://world.huanqiu.com/exclusive/2016-07/9209839.html'

url = "http://www.sohu.com/a/299667318_501931"

g = Goose({'stopwords_class': StopWordsChinese})
article = g.extract(url=url)
# article.

print article.links

# print article.publish_date
print article.title
print("--"*20)
print article.cleaned_text
# 【环球时报综合报道】针对美国共和党全国代表大会审议通过的新党纲在台湾、涉藏、经贸、南海等问题上出现干涉中国内政、指责中国政策的内容，中国外交部发言人陆慷20日回应说，推动中美关系稳定发展符合两国根本利益，有利于亚太地区乃至世界的和平与发展，是双方应该坚持的正确方向。美国无论哪个党派，都应该客观、理性
# print article.meta_description
# 美国共和党新党纲“21次提及中国”。
# print article.meta_keywordsn
# 中国,美共和党,党纲,内政