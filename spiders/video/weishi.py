# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-20 21:41:18
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-23 18:25:44

import requests,json,re,time
from pprint import pprint
from exceptions import ResponseException
from spiders import Public

class WeishiSpider(Public):
	def __init__(self, share_info):
		super().__init__()
		self.share_info = share_info
		self.api = "https://h5.weishi.qq.com/webapp/json/weishi/WSH5GetPlayPage?feedid="

	def get_vid(self):
		vid = self.share_info.split("id=")[1][0:17]
		return vid

	def get_data(self):
		vid = self.get_vid()
		get_api = self.api + vid 
		res = requests.get(get_api, headers = self.headers)
		data = json.loads(res.text)
		js_data = data['data']['feeds'][0]
		return js_data

	def parse_data(self):
		try:
			data = self.get_data()
			result = {
				"code": 200,
				"msg": "解析成功",		
				"data": {
					"video": {
						"share_title": data['feed_desc_withat'],
						"cover": data['video_cover']['static_cover']['url'],
						"play_addr": data['video_url']
					},
				"developer": self.developer
				}	
			}
			return result
		except:
			return ResponseException(status_code= 500,msg="解析失败，请检查链接重试!")		

if __name__ == '__main__':
	s= WeishiSpider("美景 @经纪人小微 >>https://isee.weishi.qq.com/ws/app-pages/share/index.html?wxplay=1&id=70zFdYARy1G5ncfMq&spid=1654542125055672320&qua=v1_and_weishi_8.13.0_585_312026001_d&chid=100081014&pkg=&attach=cp_reserves3_1000370011")
	print(s.get_vid())
	pprint(s.parse_data())


