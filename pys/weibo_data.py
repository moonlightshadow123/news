# -*- coding=UTF-8 -*-

import os
import json
import time
import requests
from lxml import etree

from utils import nowStr
bgcolor = "#ffad33"
logo_url = "../img/sina.svg"
url = "https://s.weibo.com/top/summary?cate=realtimehot"
host = "https://s.weibo.com"
headers={
    'Host': 's.weibo.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://weibo.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}

class WeiboData:
    def __init__(self):
        self.file_name = "../json/weibo.json"

    def parse(self, text):
        html_xpath = etree.HTML(text)
        data = html_xpath.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')
        # print(data)

        res_list = []
        num = 0
        for tr in (data):
            cur_dict = {}
            title = tr.xpath('./td[2]/a/text()')
            hot_score = tr.xpath('./td[2]/span/text()')
            url = host + tr.xpath('./td[2]/a')[0].get("href")
            tag = tr.xpath('./td[3]/i/text()')
            # print(url)
            # if len(tag) != 0: print(tag[0])

            # 过滤第 0 条
            if num == 0:
                pass
            else:
                cur_dict["title"] = title[0]
                cur_dict["score"] = hot_score[0]
                cur_dict["num"] = num
                cur_dict["url"] = url
                if len(tag): cur_dict["tag"] = tag[0]
                res_list.append(cur_dict)
            num += 1
        res_dict = {}
        res_dict["list"] = res_list
        res_dict["date"] = nowStr()
        res_dict["logo"] = logo_url
        res_dict["color"] = bgcolor
        return res_dict

    def request(self):
        global url
        r = requests.get(url,headers=headers)
        print(r.status_code)

        res_list = self.parse(r.text)        
        with open(self.file_name, "w") as f:
            json.dump(res_list, f, indent=4)
        return res_list

if __name__ == "__main__":
    weibo = WeiboData()
    weibo.request()