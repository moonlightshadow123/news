from flask import Flask, jsonify, request, send_from_directory
from baidu_data import BaiduData
from bili_data 	import BiliData
from news_data	import NewsData
from tianya_data	import TianyaData
from tieba_data import TiebaData
from weibo_data	import WeiboData
from zhihu_data import ZhihuData  

class DataManager:
	def __init__(self):
		self.news = NewsData()
		self.baidu = BaiduData()
		self.bili = BiliData()
		self.weibo = WeiboData()
		self.tianya = TianyaData()
		self.tieba = TiebaData()
		self.zhihu = ZhihuData()

app = Flask(__name__, static_url_path='', static_folder="../web")
dm = DataManager()   

@app.route('/test')
def test():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return jsonify(t)

@app.route('/news')
def news():
    keyword = request.args.get('keyword', default='', type=str)
    category = request.args.get('category', default='', type=str)
    print(keyword)
    print(category)
    data = dm.news.request(keyword=keyword, category=category)
    return jsonify(data)

@app.route('/weibo')
def weibo():
    data = dm.weibo.request()
    return jsonify(data)

@app.route('/baidu')
def baidu():
    data = dm.baidu.request()
    return jsonify(data)

@app.route('/bili')
def bili():
    data = dm.bili.request()
    return jsonify(data)

@app.route('/tianya')
def tianya():
    data = dm.tianya.request()
    return jsonify(data)

@app.route('/tieba')
def tieba():
    data = dm.tieba.request()
    return jsonify(data)

@app.route('/zhihu')
def zhihu():
    data = dm.zhihu.request()
    return jsonify(data)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000)