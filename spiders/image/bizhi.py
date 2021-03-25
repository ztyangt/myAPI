# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-21 18:00:43
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-23 18:29:08

import requests,json,random
from pprint import pprint
from exceptions import ResponseException
from spiders import Public

class BizhiSpider(Public):
	def __init__(self, cid,count):
		super(BizhiSpider, self).__init__()
		self.cid = str(cid)
		self.count = str(count)
		self.api = "http://wallpaper.apc.360.cn/index.php?c=WallPaperAndroid&a=getAppsByCategory&cid={}&start={}&count={}"

	def get_total(self):
		res = requests.get(self.api.format(self.cid,0,1),headers = self.headers)
		data = json.loads(res.text)
		total = data['total']
		return total

	def parse_data(self):
		try:
			total = self.get_total()
			start = random.randint(0,int(total))
			url = self.api.format(self.cid,start,self.count)
			res = requests.get(url,headers = self.headers)
			data = json.loads(res.text)
			result = {
				"code":200,
				"data": data['data'],
				"developer": self.developer
			}
			return result
		except:
			return ResponseException(status_code= 500,msg="解析失败，请检查链接重试!")


	