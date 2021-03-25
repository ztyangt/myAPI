# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-21 20:49:55
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-23 18:29:04

import requests,json,random
from pprint import pprint
from exceptions import ResponseException
from spiders import Public
class BingSpider(Public):
	def __init__(self):
		super(BingSpider, self).__init__()
		self.api = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"

	def parse_data(self):
		try:
			res = requests.get(self.api,headers = self.headers)
			data = json.loads(res.text)
			url = "https://www.bing.com/" + data['images'][0]['url'].split("&")[0]
			result = {
				"code": 200,
				"data": {
					"startdate": data['images'][0]['startdate'],
					"enddate": data['images'][0]['enddate'],
					"url": url,
					"copyright":data['images'][0]['copyright']
				},
				"developer": self.developer
			}
			return result
		except:
			return ResponseException(status_code= 500,msg="请求失败，请检查链接重试!")
