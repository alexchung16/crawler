# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 书籍背景图片地址
    cover_url = scrapy.Field()
    # 书籍详细页地址
    url = scrapy.Field()
    # 书籍名称
    book_name = scrapy.Field()
    # 书籍作者
    book_author = scrapy.Field()
    # 书籍介绍
    book_detail = scrapy.Field()
    # 书籍页数
    book_page_num = scrapy.Field()
    # 书籍价格
    book_price = scrapy.Field()
    # 发布时间
    publish_time = scrapy.Field()


class ScrapyCodesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass