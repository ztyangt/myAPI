# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-23 09:26:05
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-24 09:19:06

import requests,json,re
from html import unescape
from pprint import pprint
from lxml import etree
from exceptions import ResponseException
from spiders import Public

class TodaySpider(Public):
	def __init__(self, date):
		super(TodaySpider, self).__init__()
		self.date = date
		self.api = "https://baike.baidu.com/cms/home/eventsOnHistory/{:0>2d}.json"

	def get_data(self):
		mon = self.date.split("-")[0]
		day = self.date.split("-")[1]
		api = self.api.format(int(mon))
		res = requests.get(api,headers = self.headers)
		data = json.loads(res.text)["{:0>2d}".format(int(mon))]["{:0>2d}{:0>2d}".format(int(mon),int(day))]
		return data

	def rm_html(self,string):
		result = re.sub('<[^<]+?>', '', string).replace('\n', '').strip()
		return result

	def get_desc(self,link):
		res = requests.get(link,headers = self.headers)
		sel = etree.HTML(res.text)
		desc = sel.xpath('//*[@class="summary-content"]')[0]
		content = etree.tostring(desc, method='html')
		data = unescape(str(content, encoding="utf-8"))
		return self.rm_html(data)

	def parse_data(self):
		try:
			data = self.get_data()
			data_list = []
			for item in data:
				ts = {
					"time": str(item['year']) + "-" + self.date,
					"title": self.rm_html(item['title']),
					"desc": self.get_desc(item['link'])
				}
				data_list.append(ts)

			result = {
				"code": 200,
				"msg": "success",
				"data": data_list,
				"developer": self.developer
			}
			return result
		except:
			return ResponseException(status_code= 500,msg="请求失败，请检查链接重试!")