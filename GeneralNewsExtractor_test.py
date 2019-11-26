# -*- coding: utf-8 -*-
# @Time: 2019/11/26 14:50

import codecs
from gne import GeneralNewsExtractor

with codecs.open('test.html', 'r', encoding='utf-8') as f:
    content = f.read()

extractor = GeneralNewsExtractor()
result = extractor.extract(content, noise_node_list=['//div[@class="comment-list"]'])
print(result)