# !_*_ coding:utf8 _*_
# @function 百度图片爬虫
# @Author alexchung
# @Date 2019/7/29 17:21 PM

import os
import re
import requests
import hashlib
import time

import concurrent.futures

from urllib import error
from bs4 import BeautifulSoup

class Crawler(object):
    def __init__ (self, fig_type='', fig_num=0, save_path=None):
        self.type = fig_type
        self.page = fig_num / 30
        # self.route = file_route
        self.save_path = os.path.join(save_path, str(fig_type))

        self.url_list = []
        self.number = len(self.url_list)

        if os.path.exists(self.save_path) is False:
            os.makedirs(self.save_path)

    def run(self):
        """
        运行方法，更新属性
        :return:
        """
        self.get_url()
        # self.getSearchURL()
        # self.getFileURL()
        self.download_picture_threading()

    def get_url(self):

        params = []
        for i in range(30, 30 * int(self.page) + 30, 30):
            params.append({
                'tn': 'resultjson_com',
                'ipn': 'rj',
                'ct': 201326592,
                'is': '',
                'fp': 'result',
                'queryWord': self.type,
                'cl': 2,
                'lm': -1,
                'ie': 'utf-8',
                'oe': 'utf-8',
                'adpicid': '',
                'st': -1,
                'z': '',
                'ic': 0,
                'word': self.type,
                's': '',
                'se': '',
                'tab': '',
                'width': '',
                'height': '',
                'face': 0,
                'istype': 2,
                'qc': '',
                'nc': 1,
                'fr': '',
                'pn': i,
                'rn': 30,
                'gsm': '5a',
                '1564468338576': ''
            })
        url = 'https://image.baidu.com/search/index'
        for p in params:
            page_list = requests.get(url, params=p).json().get('data')
            for ls in page_list:
                if ls.get('thumbURL') == None:
                    continue
                else:
                    self.url_list.append(ls.get('thumbURL'))
                    self.number += 1

    # @ property
    def get_search_url(self):
        """
        获取搜索url
        :return:
        """
        self.url = r'http://image.baidu.com/search/index?tn=baiduimage&ps=1&lm=-1&cl=2&nc=1&ie=utf-8&word=' + self.type

    def get_file_url(self):
        """
        获取图片文件url
        :return:
        """
        # time
        t = 0
        # url size
        fig_size = 0
        while t < 1000:
            Url = self.url + str(t)
            try:
                Result = requests.get(Url, timeout=7)
            except BaseException:
                t += 60
                continue
            else:
                result = Result.text
                # html = urlopen(self.url)
                # htmls = html.read().decode()
                pic_url = re.findall(r'"objURL":"(.*?)",', result, re.S)
                self.number = len(pic_url)
                if len(pic_url) == 0:
                    break
                else:
                    self.url_list = pic_url
                    t += 60

    def download_picture(self):
        """
        执行图片下载
        :return:
        """

        # num_index = 0
        print('图片保存路径为:{0}'.format(self.save_path))
        print('当前页面检索到{0}张照片'.format(str(self.number)))
        for pic_source in self.url_list:
            # print('正在下载第{0}/{1}张照片，照片源：{2}'.format(str(num_index+1), str(self.number), str(pic_source)))
            try:
                self.save_image(pic_source)
            except BaseException:
                print('未知原因导致当前图片无法下载')
                continue

    def download_picture_threading(self):
        """
        执行图片下载
        :return:
        """

        # num_index = 0
        print('图片保存路径为:{0}'.format(self.save_path))
        print('当前页面检索到{0}张照片'.format(str(self.number)))

        with concurrent.futures.ThreadPoolExecutor() as execute:
            execute.map(self.save_image, self.url_list)


    def save_image(self, pic_url):
        """
        save unique image
        :param pic_url:
        :param save_path:
        :return:
        """
        print('正在下载照片源：{0}'.format(str(pic_url)))
        if pic_url is None:
            raise KeyError("picture url is None")
        else:
            pic = requests.get(pic_url, timeout=7)

        md5 = hashlib.md5()
        md5.update(pic_url.encode('utf-8'))
        string = os.path.join(self.save_path, str(md5.hexdigest()) + '.jpg')

        fp = open(string, 'wb')
        fp.write(pic.content)
        fp.close()


if __name__  == "__main__":
    save_path = os.getcwd()
    # 获取类实例
    start_time = time.perf_counter()
    crawler_fig = Crawler('湖泊', 300, save_path=save_path)
    crawler_fig.run()
    finish_time = time.perf_counter()
    print(f"Spend {finish_time-start_time} second")




