# encoding: utf-8
import requests
import re, json
from bs4 import BeautifulSoup

from utils import nowStr
bgcolor = "#d3e0f3"
logo_url = "zhihu.svg"
zh_url = "https://www.zhihu.com/billboard"

def findKey(data, thekey):
	if type(data) != dict: return None
	for key,val in data.items():
		if key == thekey:
			return val
		else:
			res = findKey(val, thekey)
			if res != None: return res 
	return None

class ZhihuData:
	def __init__(self):
		self.file_name = "../json/zhihu.json"

	def parse(self, data):
		thelist = findKey(data, "hotList")
		res_list = []
		for idx, entry in enumerate(thelist):
			cur_dict = {}
			cur_dict["title"] = findKey(entry, "titleArea")["text"]
			cur_dict["url"] = findKey(entry, "link")["url"]
			cur_dict["num"] = idx+1
			cur_dict["score"] = findKey(entry, "metricsArea")["text"]
			if findKey(entry, "excerptArea")["text"]: cur_dict["extra"] = findKey(entry, "excerptArea")["text"]
			res_list.append(cur_dict)
		res_dict = {}
		res_dict["list"] = res_list
		res_dict["date"] = nowStr()
		res_dict["logo"] = logo_url
		res_dict["color"] = bgcolor
		return res_dict

	def request(self):
		headers={"User-Agent":"","Cookie":""}
		zh_response = requests.get(zh_url,headers=headers)

		webcontent = zh_response.text
		soup = BeautifulSoup(webcontent,"html.parser")
		# print(soup.find("script",id="js-initialData"))
		script_text = soup.find("script",id="js-initialData").encode_contents()
		data = json.loads(script_text)
		print(data)
		jsonData = self.parse(data)
		with open(self.file_name, "w") as f:
			json.dump(jsonData, f, indent=4)

if __name__ == "__main__":
	zhihu = ZhihuData()
	zhihu.request()