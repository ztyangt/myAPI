# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-22 21:51:06
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-23 18:29:51

import requests,json,time
from pprint import pprint
from exceptions import ResponseException
from spiders import Public

class YiyanSpider(Public):
	def __init__(self, c):
		super(YiyanSpider, self).__init__()
		self.api = "https://v1.hitokoto.cn/?&c={}"
		self.c = c

	def parse_data(self):
		try:
			c_dict = {
				"a": "动画",
				"b": "漫画",
				"c": "游戏",
				"d": "文字",
				"e": "原创",
				"f": "网络",
				"g": "其他",
				"h": "影视",
				"i": "诗词",
				"j": "网易云",
				"k": "哲学",
				"l": "抖机灵"
			}
			res = requests.get(self.api.format(self.c),headers = self.headers)
			data = json.loads(res.text)
			result = {
				"code": 200,
				"msg": "success",
				"data": {
					"content": data['hitokoto'],
					"type": c_dict[data['type']],
					"from": data['from'],
					"author": data['creator'],
					"created_at": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data['created_at']))),
					"length": data['length']
				},
				"developer": self.developer
			}
			return result
		except:
			return ResponseException(status_code= 500,msg="请求失败，请检查链接重试!")