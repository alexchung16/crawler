#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------
# @ File       : selenium_demo.py
# @ Description:  
# @ Author     : Alex Chung
# @ Contact    : yonganzhong@outlook.com
# @ License    : Copyright (c) 2017-2018
# @ Time       : 2020/6/28 下午7:35
# @ Software   : PyCharm
#-------------------------------------------------------
import time

from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.options import Options

chrome_driver = './libs/chromedriver'

if __name__ == "__main__":
    browser = webdriver.Chrome(executable_path=chrome_driver)
    browser.get("http://www.xinhuanet.com/politics/")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    while True:
        try:
            load_more = browser.find_elements_by_xpath('//*[@class="moreBtn"]')
            # load_more = browser.find_element_by_xpath('//*[@class="moreB"]')
            # load_more = browser.find_elements_by_xpath('//*[@class="moreB"]')
            print(len(load_more)==0)
            load_more.click()
            time.sleep(0.1)
        # load to end page
        except ElementNotInteractableException:
            html = browser.page_source
            break


