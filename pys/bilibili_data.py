# -*- coding=UTF-8 -*-

import os
import json
import time
import requests
from lxml import etree
from utils import nowStr

from utils import nowStr
bgcolor = "#d3e0f3"
logo_url = "bibili.png"
url = "https://www.bilibili.com/ranking"

class BiliData:
    def __init__(self):
        self.file_name = "../json/bili.json"

    def parse(self, text):
        html_xpath = etree.HTML(text)
        data = html_xpath.xpath('//*[@class="rank-item"]')
        # print(data)

        res_list = []
        num = 0
        for idx,item in enumerate(data):
            cur_dict = {}
            title = item.xpath('./div[@class="content"]/div[@class="info"]/a/text()')
            hot_score = item.xpath('./div[@class="content"]/div[@class="info"]/div[@class="pts"]/div/text()')
            url = item.xpath('./div[@class="content"]/div[@class="info"]/a')[0].get("href")
            cur_dict["title"] = title[0]
            cur_dict["score"] = hot_score[0]
            cur_dict["num"] = idx + 1
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
    bili = BiliData()
    bili.request()