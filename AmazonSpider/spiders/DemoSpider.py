#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2018/9/7 下午4:36
@Author  : fanyuexiang
@Site    : 
@File    : DemoSpider.py
@Software: PyCharm
@version: 1.0
@describe: scrapy 测试Demo
'''
import scrapy
from scrapy import Selector
from AmazonSpider.items import AmazonspiderItem


class DemoSpider(scrapy.Spider):
    name = 'demoSpider'
    allowed_domains = ['demoSpider.org']
    start_urls = {
                     'https://www.amazon.cn/gp/site-directory/ref=nav_shopall_btn'
    }

    def parse(self, response):
        # item = AmazonspiderItem(scrapy.Item)
        print(response.url)
        selector = Selector(response)
        lables = selector.xpath('//a[@class = "nav_a a-link-normal a-color-base"]//@href').extract()
        print(len(lables))
        for lable in lables:
            print(lable)