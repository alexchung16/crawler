#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------
# @ File       : run.py
# @ Description:  
# @ Author     : Alex Chung
# @ Contact    : yonganzhong@outlook.com
# @ License    : Copyright (c) 2017-2018
# @ Time       : 2020/6/19 上午11:26
# @ Software   : PyCharm
#-------------------------------------------------------

import os
import sys
from scrapy.commands.crawl import Command
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # Command().run(args=["scrapy crawl itcast"], opts="-o teacher.csv")

    # execute(argv=["scrapy", "crawl", "douban_book"])
    execute(argv=["scrapy", "crawl", "douban_book"])