#### 环境

​	python2		Python-Goose

​	python3		newspaper，readability，html2text（html转txt）

#### 扩展包 Python-Goose 文章提取器

​       这是Python中的完全重写。该软件的目的是获取任何新闻文章或文章类型的网页，不仅提取文章的主体，而且提取所有元数据和最可能的图像候选。

​	有部分提取方法可根据场景重写

```
git clone https://github.com/grangier/python-goose.git
cd python-goose
pip install -r requirements.txt
python setup.py install
```

#### goose弊端

​	内置方法下载不到页面，通过raw_html提取

```
import goose
raw_html = ""
a = g.extract(raw_html=raw_html)
a.infos
```

#### 扩展包 newspaper

​	安装    pip3 install --ignore-installed --upgrade newspaper3k 或 pip install newspaper3k

#### readability

​	安装 	pip install readability-lxml

​	基于[BeautifulSoup](http://www.pythonclub.org/modules/beautifulsoup/start)  速度会稍微慢一些。

​	Raedability网站(www.readability.com)最引以为傲的就是其强大的解析引擎, 号称世界上最强大的文本解析神器. Safari中的"阅读器"功能就是用它来实现的! 他们还提供了API可以调用解析器的功能。

​	具体情况待测

#### boilerpipe

​	参考 https://github.com/misja/python-boilerpipe

​	只能解析出正文

#### 总结

​	newspaper 和 goose 对于提取都有一定的偏差， 可根据场景重写底层方法

​	都消耗大量cpu，

​	目前较好的是 readability， 但是基于[BeautifulSoup](http://www.pythonclub.org/modules/beautifulsoup/start)  速度会稍微慢一些。

#### 参考

1、https://piaosanlang.gitbooks.io/spiders/content/10day/section10.1.html

2、https://github.com/grangier/python-goose

3、https://github.com/codelucas/newspaper

4、https://blog.csdn.net/mouday/article/details/87942995 使用newspaper解析新闻页面信息

5、 https://github.com/misja/python-boilerpipe