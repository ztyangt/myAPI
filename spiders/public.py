# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-21 10:50:02
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-21 21:26:06

import time

class Public():
	def __init__(self):
		self.headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/84.0.4147.105',
	  'Content-Type': 'application/json; charset=UTF-8'}
		self.developer = {
					"author": "南玖",
					"home": "https://www.ztongyang.cn/",
					"email": "yang2210670@163.com",
					"time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
					"powered_by": "南玖API-免费开放的API接口服务",
					"docs": "https://docs.ucool.icu/api/"
				}
