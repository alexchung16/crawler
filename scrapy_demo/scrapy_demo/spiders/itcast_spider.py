#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------
# @ File       : itcast_spider.py
# @ Description:  
# @ Author     : Alex Chung
# @ Contact    : yonganzhong@outlook.com
# @ License    : Copyright (c) 2017-2018
# @ Time       : 2020/6/18 下午3:25
# @ Software   : PyCharm
#-------------------------------------------------------

import scrapy
from scrapy_demo.items import ScrapyDemoItem
class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    # parse web html
    # def parse(self, response):
    #     filename = "teacher.html"
    #     with open(filename, 'wb') as wf:
    #         wf.write(response.body)

    def parse(self, response):

        items = []
        for each in response.xpath("//div[@class='li_txt']"):
            item = ScrapyDemoItem()

            item['name'] = each.xpath("h3/text()").extract()[0]
            item['level'] = each.xpath("h4/text()").extract()[0]
            item['info'] = each.xpath("p/text()").extract()[0]

            # items.append(item)
            yield item

