import requests, json
apiKey = "161c297a4e864b6ea39616beee6baf34"
country = "us"
categories = ["business","entertainment", "general", "health", "science", "sports", "technology"]

class NewsData:
	def __init__(self):
		self.file_name = "../json/news.json"
		self.url = "http://newsapi.org/v2/top-headlines"

	def buildUrl(self, keyword, category):
		url = self.url + "?apiKey=" + apiKey
		if country != "": url += ("&country=" + country )
		if keyword and keyword != "": url += ("&q=" + keyword)
		if category and category != "": url += ("&category=" + category)
		return url

	def request(self, keyword="", category=""):
		url = self.buildUrl(keyword, category)
		response = requests.get(url)
		# print(response.json())
		with open(self.file_name, "w") as f:
			json.dump(response.json(), f, indent=4)
		return response.json()
if __name__ == "__main__":
	news = NewsData()
	news.request()