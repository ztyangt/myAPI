# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-22 18:05:27
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-23 18:30:01


import requests,json,random
from pprint import pprint
from exceptions import ResponseException
from spiders import Public

class Shici(Public):
	def __init__(self,category):
		super(Shici, self).__init__()
		self.category = category

	def parse_data(self):
		try:
			file = open(f'source/shici/{self.category}.txt','r',encoding='utf-8')
			ls = file.readlines()
			count = len(ls)
			txt = ls[random.randint(0,count)].replace("\n","")
			file.close()
			result = {
				"code": 200,
				"msg":"success",
				"data": eval(txt),
				"developer": self.developer
			}
			return result
		except:
			return ResponseException(status_code= 500,msg="请求失败，请检查链接重试!")