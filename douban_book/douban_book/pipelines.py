# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import time
import csv
import json
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class ScrapyDemoPipeline(object):

    def __init__(self):
        pass

    @classmethod
    def from_crawler(cls, crawler):
        """transmit parameter"""
        pass

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass


    def process_item(self, item, spider):
        pass


class DoubanToTextPipeline():

    def __init__(self, file_path):
        self.path = os.path.join(file_path, str(int(time.time())) + '.txt')

    @classmethod
    def from_crawler(cls, crawler):
        file_path = crawler.settings.get('PATH')
        return cls(file_path=file_path)

    def open_spider(self, spider):
        self.fhd = open(self.path, 'w')

    def close_spider(self, spider):
        self.fhd.close()

    def process_item(self, item, spider):
        data_info = dict(item)
        vals = ','.join(data_info.values())
        self.fhd.write(vals)
        self.fhd.write('\n')
        return item


class DoubanToCSVPipeline(object):
    def __init__(self, file_path):
        self.path = os.path.join(file_path, str(int(time.time())) + '.csv')

    @classmethod
    def from_crawler(cls, crawler):
        file_path = crawler.settings.get('PATH')
        return cls(file_path=file_path)

    def open_spider(self, spider):
        self.fhd = open(self.path, 'w')
        self.write = csv.writer(self.fhd)
        self.write.writerow(['book_author', 'book_detail','book_name', 'book_page_num', 'book_price', 'cover_url', 'publish_time', 'url'])

    def close_spider(self, spider):
        self.fhd.close()
        self.write.close()

    def process_item(self, item, spider):

        book_list = [item['book_author'], item['book_detail'], item['book_name'], item['book_page_num'], item['book_price'],
                     item['cover_url'], item['publish_time'], item['url']]
        self.write.writerow(book_list)
        return item


class DoubanJsonPipeline(object):

    def __init__(self, file_path):
        self.path = os.path.join(file_path, str(int(time.time())) + '.json')

    @classmethod
    def from_crawler(cls, crawler):
        file_path = crawler.settings.get('PATH')
        return cls(file_path=file_path)

    def open_spider(self, spider):
        self.handler = open(self.path, 'w')
        self.handler.write('[')

    def close_spider(self, spider):
        self.handler.write(']')
        self.handler.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)
        self.handler.write(line)
        self.handler.write(',\n')
        return item

class DoubanImagePipeline(ImagesPipeline):
    """
    reference https://doc.scrapy.org/en/latest/topics/media-pipeline.html
    """
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    def get_media_requests(self, item, info):
        yield Request(item['cover_url'])

    def close_spider(self, spider):
        print('spider is closed')