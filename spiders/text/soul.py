# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-22 12:46:51
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-23 18:30:05

import random
from spiders import Public
from exceptions import ResponseException

class Soul(Public):
	def __init__(self):
		super(Soul, self).__init__()

	def parse_data(self):
		try:
			file = open('source/soul.txt','r',encoding='utf-8')
			ls = file.readlines()
			count = len(ls)
			txt = ls[random.randint(0,count)].replace("\n","")
			file.close()
			result = {
				"code": 200,
				"data": txt,
				"developer": self.developer
			}
			return result
		except:
			return ResponseException(status_code= 500,msg="请求失败，请检查链接重试!")

