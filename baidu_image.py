# !_*_ coding:utf8 _*_
# @function 百度图片爬虫
# @Author alexchung
# @Date 2019/7/29 17:21 PM

import os
import re
import requests

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
        self.getURL()
        # self.getSearchURL()
        # self.getFileURL()
        self.downloadPicture()

    def getURL(self):

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
    def getSearchURL(self):
        """
        获取搜索url
        :return:
        """
        self.url = r'http://image.baidu.com/search/index?tn=baiduimage&ps=1&lm=-1&cl=2&nc=1&ie=utf-8&word=' + self.type

    def getFileURL(self):
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


    def downloadPicture(self):
        """
        执行图片下载
        :return:
        """
        num_index = 0
        print('图片保存路径为:{0}'.format(self.save_path))
        print('当前页面检索到{0}张照片'.format(str(self.number)))
        for pic_source in self.url_list:
            print('正在下载第{0}/{1}张照片，照片源：{2}'.format(str(num_index+1), str(self.number), str(pic_source)))
            try:
                if pic_source is None:
                    continue
                else:
                    pic = requests.get(pic_source, timeout=7)


                string = os.path.join(self.save_path, str(num_index) + '.jpg')

                fp = open(string, 'wb')
                fp.write(pic.content)
                fp.close()
                num_index += 1

            except BaseException:
                print('未知原因导致当前图片无法下载')
                continue


if __name__  == "__main__":
    save_path = os.getcwd()
    # 获取类实例
    crawler_fig = Crawler('湖泊', 300, save_path=save_path)
    crawler_fig.run()



