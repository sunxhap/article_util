# -*- coding: utf-8 -*-
"""
 @Time: 2019/6/26 14:33
"""

import time
import os
import sys

from boilerpipe.extract import Extractor

# url = "http://www.sohu.com/a/299667318_501931"
# extractor = Extractor(extractor='ArticleExtractor', url=url)


import codecs
with codecs.open('test.html', 'r', encoding='utf-8') as f:
    content = f.read()
extractor = Extractor(extractor='ArticleSentencesExtractor', html=content)

# extractor = Extractor(url=url)

extracted_text = extractor.getText()

extracted_html = extractor.getHTML()

print(extracted_html)