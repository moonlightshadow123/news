# -*- coding=UTF-8 -*-
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import os
from utils import nowStr
bgcolor = "#d3e0f3"
logo_url = "baidu.svg"
url = "http://top.baidu.com/buzz?b=1"
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Host": "top.baidu.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": '1'
    }

class BaiduData:
    def __init__(self):
        self.file_name = "../json/baidu.json"

    def parse(self, text):
        soup = BeautifulSoup(text, "lxml")
        table = soup.find('table')
        trs = table.find_all('tr')
        data = []
        for tr in trs[1:]:
            index = tr.find(class_="first")
            if not index:
                continue
            index = int(index.text)
            keyword = tr.find(class_="keyword").find('a').text
            href = tr.find(class_="keyword").find('a')['href']
            keyword = keyword.replace('\n', '').replace('\t', '').strip()
            search_index = tr.find(class_="last").text
            search_index = int(search_index)
            data.append({
                'num': index,
                'title': keyword,
                'score': search_index,
                'url':href
            })
        res_dict = {}
        res_dict["list"] = data
        res_dict["date"] = nowStr()
        res_dict["logo"] = logo_url
        res_dict["color"] = bgcolor
        return res_dict

    def request(self):
        global url
        res = requests.get(url, headers=headers)
        res_list = self.parse(res.content.decode('gbk'))
        with open(self.file_name, "w") as f:
            json.dump(res_list, f, indent=4)


if __name__ == '__main__':
    baidu = BaiduData()
    baidu.request()


'''

    def 

class Parser:
    doc = ''

    def __init__(self, doc):
        self.doc = doc

    def parse(self):
        soup = BeautifulSoup(self.doc, "lxml")
        table = soup.find('table')
        trs = table.find_all('tr')
        data = []
        for tr in trs[1:]:
            index = tr.find(class_="first")
            if not index:
                continue
            index = int(index.text)
            keyword = tr.find(class_="keyword").find('a').text
            href = tr.find(class_="keyword").find('a')['href']
            keyword = keyword.replace('\n', '').replace('\t', '').strip()
            search_index = tr.find(class_="last").text
            search_index = int(search_index)
            data.append({
                'index': index,
                'keyword': keyword,
                'search_index': search_index,
                'href':href
            })
        return data


class Clawer:
    TIMEOUT = 30
    _HEARDERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Host": "top.baidu.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": '1'
    }

    def request(self, url):
        res = requests.get(url, headers=self._HEARDERS, timeout=self.TIMEOUT)
        doc = res.content.decode('gbk')
        return doc


class Runner:
    base_url = "http://top.baidu.com/buzz?b={}"
    base_dir = "./data"
    CLASSES = {
        "realtime":1,
        "today": 341,
        "sevent_day": 42,
        "life": 342,
        "entertainment": 344,
        "sports": 11,
    }

    def __init__(self):
        now = datetime.now()
        self._year = str(now.year)
        self._filename = now.strftime("%m-%d.json")

    def _check_directory(self, name):
        classes_dir = os.path.join(self.base_dir, name)
        if not os.path.exists(classes_dir):
            os.mkdir(classes_dir)

        year_dir = os.path.join(classes_dir, self._year)
        if not os.path.exists(year_dir):
            os.mkdir(year_dir)
        return year_dir

    def _save(self, name):
        _id = self.CLASSES.get(name)
        url = self.base_url.format(_id)
        clawer = Clawer()
        doc = clawer.request(url)

        parser = Parser(doc)
        data = parser.parse()

        directory = self._check_directory(name)
        path = os.path.join(directory, self._filename)
        json.dump(data, open(path, 'w'), ensure_ascii=False)

    def run_all(self):
        for name in self.CLASSES.keys():
            self._save(name)


if __name__ == '__main__':
    runner = Runner()
    runner.run_all()
'''