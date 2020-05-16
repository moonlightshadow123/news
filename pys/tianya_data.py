# -*- coding=UTF-8 -*-

import os
import json
import time
import requests
from lxml import etree

from utils import nowStr
bgcolor = "#66cc00"
logo_url = "../img/tianya.jpg"
url = "https://bbs.tianya.cn/m/hotArticle.jsp"
headers={
    'Host': 's.weibo.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://weibo.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}

class TianyaData:
    def __init__(self):
        self.file_name = "../json/tianya.json"

    def parse(self, text):
        html_xpath = etree.HTML(text)
        data = html_xpath.xpath('//*[@id="j-bbs-hotpost"]/*[@class="m-box"]/ul/li')
        # print(data)

        res_list = []
        num = 0
        for idx, li in enumerate(data):
            cur_dict = {}
            title = li.xpath('.//p[@class="title"]/text()')
            # hot_score = tr.xpath('./td[2]/span/text()')
            url = li.xpath('./a')[0].get("href")
            # 过滤第 0 条
            cur_dict["title"] = title[0]
            cur_dict["score"] = ""
            cur_dict["num"] = idx+1
            cur_dict["url"] = url
            res_list.append(cur_dict)
        res_dict = {}
        res_dict["list"] = res_list
        res_dict["date"] = nowStr()
        res_dict["logo"] = logo_url
        res_dict["color"] = bgcolor
        return res_dict

    def request(self):
        global url
        r = requests.get(url)
        print(r.status_code)

        res_list = self.parse(r.text)        
        with open(self.file_name, "w") as f:
            json.dump(res_list, f, indent=4)

if __name__ == "__main__":
    tianya = TianyaData()
    tianya.request()