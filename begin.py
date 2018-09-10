#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2018/9/7 下午4:43
@Author  : fanyuexiang
@Site    : 
@File    : begin.py
@Software: PyCharm
@version: 1.0
@describe: 运行爬虫程序
'''
from scrapy import cmdline

cmdline.execute('scrapy crawl demoSpider'.split())