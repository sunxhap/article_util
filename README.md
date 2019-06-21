#### 环境

​	python2.7



#### 扩展包 Python-Goose 文章提取器

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





#### 参考

1、https://piaosanlang.gitbooks.io/spiders/content/10day/section10.1.html

2、https://github.com/grangier/python-goose