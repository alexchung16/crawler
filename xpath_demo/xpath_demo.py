#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------
# @ File       : xpath_demo.py
# @ Description:  
# @ Author     : Alex Chung
# @ Contact    : yonganzhong@outlook.com
# @ License    : Copyright (c) 2017-2018
# @ Time       : 2020/6/22 下午2:27
# @ Software   : PyCharm
#-------------------------------------------------------

from lxml import etree

html_path = './test.html'

if __name__ == "__main__":
    html = etree.parse(html_path, etree.HTMLParser())

    # all html content
    result = etree.tostring(html)
    print(result.decode('utf-8'))

    # get all node
    all_node = html.xpath('//*')
    print(all_node)

    # get all li
    li_node = html.xpath('//li')
    print(li_node)


    # get ll a node
    a_node = html.xpath('//li/a')
    print(a_node)



    # father_node = html.xpath('//a[@href="https://ask.hellobi.com/link4.html"]/../@class')
    father_node = html.xpath('//a[@href="https://ask.hellobi.com/link4.html"]/parent::*/@class')
    print(father_node)


    # match property
    match_result = html.xpath('//li[@class="item-0"]')
    print(match_result)

    # get text()
    text_reslult = html.xpath('//li[@class="item-1"]/a/text()')
    print(text_reslult)

    # get property
    herf = html.xpath('//li/a/@href')
    print(herf)


    # 知识点一：
    # /: 直接获取子节点
    # //: 获取子孙节点
    # .: 获取当前节点
    # ..: 获取父节点

    # 属性多值匹配
    # contains
    multi_match = html.xpath('//li[contains(@class, "li")]/a/text()')
    print(multi_match)

    # 多属性匹配
    # and | or | mod
    multi_property = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
    print(multi_property)


    # 按序选择
    # position
    first_result = html.xpath('//li[1]/a/text()')
    print(first_result)

    last_result = html.xpath('//li[last()]/a/text()')
    print(last_result)

    two_result = html.xpath('//li[position()<3]/a/text()')
    print(two_result)

    third_bottom = html.xpath('//li[last()-2]/a/text()')
    print(third_bottom)


    # node axis
    # ancestor
    ancestor_node = html.xpath('//li[1]/ancestor::*')
    print(ancestor_node)
    # ancestor-or-self
    ancestor_self_node = html.xpath('//li[1]/ancestor-or-self::*')
    print(ancestor_self_node)
    # attribute
    attribute_node = html.xpath('//li[last()]/attribute::*')
    print(attribute_node)
    # child
    child_node = html.xpath('//li[1]/child::a[@href="https://ask.hellobi.com/link1.html"]')
    print(child_node)
    # descendant
    descendant_node = html.xpath('//li[last()]/descendant::*')
    print(descendant_node)
    # following

    # following-sibling
    following_result = html.xpath('//li[1]/following::*')
    print(following_result)
    # parent
    parent_result = html.xpath('//li[1]/parent::*')
    print(parent_result)
    # preceding
    preceding_result = html.xpath('//li[1]/preceding::*')
    print(preceding_result)






