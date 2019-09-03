# -*- coding: utf-8 -*-
"""
 @Time: 2019/6/21 14:16
"""

import time
import os
import sys


from newspaper import Article
url = 'http://world.huanqiu.com/exclusive/2016-07/9209839.html'
news = Article(url, language='zh')
news.download()
news.parse()
print(news.text)
print(news.title)
# print(news.html)

# ---直接解析页面---------------------
news = Article("", language='zh')
html = """
<html><body><div><article class="article" id="mp-editor">
      <p data-role="original-title">原标题：公务员考试行测技巧：折纸盒，难道只能画橡皮吗</p>
            <p>不管公务员考试还是事业单位考试，图形推理折纸盒基本是必考题型。而一谈到这个题型的解题方法，考生们第一个想法几乎都是画橡皮，某宝甚至还有各种立方体的橡皮出售，被考生们称为折纸盒神器。那么，画橡皮法真的好用吗?要得出这个问题的答案，中公教育专家建议各位考生亲身体验一次，随意找一道折纸盒题，用准备好的橡皮画一画，看看自己的解题时间和正确率如何。如果能在一分钟内解出来那就基本合格，如果不能，尤其是画错图案或者选错答案的，那么建议要么勤画苦练，要么学习一下下列方法，或许能助你半分钟内拿下折纸盒题。</p>
<p>一、相对面排除法</p>
<p>以正六面体为例，每个正六面体都有三组相对面，当一个纸盒的展开图确定了之后，三组相对面也就确定了，也就是说这三组相对面不可能变成相邻面了。所以，如果选项中的纸盒将本是相对的两个面折成相邻的，那这个选项即可直接排除。比如例1中，A项的左侧面与顶面是相对面，不可能相邻，可排除;B项，左侧面和右侧面是相对面，也不可能相邻，排除。这么做每个选项的判断时间基本可以控制在7秒之内，两个选项不超过15秒。那么剩下两个选项怎么办呢?请看下文。</p>
<p>二、公共边、公共点法</p>
</article>
    </div></body></html>
"""
# news.set_article_html(html)
news.download(input_html=html)
news.parse()
print(news.text)
print(news.title)
# ---直接解析页面---------------------

# from newspaper import Article
# url = '你想要爬取的网站url'
# news = Article(url, language='zh')
#
# news.download()  #先下载
# news.parse()    #再解析
#
# print(news.text) #新闻正文
# print(news.title) #新闻标题
# print(news.html)   #未修改的原始HTML
# print(news.authors)  #新闻作者
# print(news.top_image) #本文的“最佳图像”的URL
# print(news.movies)  #本文电影url
# print(news.keywords) #新闻关键词
# print(news.summary)   #从文章主体txt中生成的摘要
# print(news.images) #本文中的所有图像url
