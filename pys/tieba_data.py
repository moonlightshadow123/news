# -*- coding=UTF-8 -*-

import os
import json
import time
import requests
from lxml import etree
from utils import nowStr
bgcolor = "#ff66b3"
logo_url = "../img/tieba.png"
url = "http://tieba.baidu.com/hottopic/browse/topicList"
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Host": "tieba.baidu.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": '1'
    }

def findKey(data, thekey):
    if type(data) != dict: return None
    for key,val in data.items():
        if key == thekey:
            return val
        else:
            res = findKey(val, thekey)
            if res != None: return res 
    return None

class TiebaData:
    def __init__(self):
        self.file_name = "../json/tieba.json"

    def parse(self, data):
        # print(text)
        topic_list = findKey(findKey(data, "bang_topic"), "topic_list")
        # print(topic_list)

        res_list = []
        num = 0
        for idx,item in enumerate(topic_list):
            cur_dict = {}
            cur_dict["title"] = item["topic_name"]
            cur_dict["score"] = item["discuss_num"]
            cur_dict["num"] = idx + 1
            cur_dict["url"] = item["topic_name"]
            cur_dict["text"] = item["topic_desc"]
            cur_dict["img"] = item["topic_pic"]
            res_list.append(cur_dict)
        res_dict = {}
        res_dict["list"] = res_list
        res_dict["date"] = nowStr()
        res_dict["logo"] = logo_url
        res_dict["color"] = bgcolor
        return res_dict

    def request(self):
        global url
        r = requests.get(url, headers=headers)
        print(r.status_code)

        data = json.loads(r.content)
        # print(data)
        res_list = self.parse(data)        
        with open(self.file_name, "w") as f:
            json.dump(res_list, f, indent=4)
        return res_list

if __name__ == "__main__":
    tieba = TiebaData()
    tieba.request()