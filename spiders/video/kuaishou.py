# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-20 09:18:16
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-23 18:25:36

import requests,json,re,time
from pprint import pprint
from exceptions import ResponseException
from spiders import Public

class KuaishouSpider(Public):
	def __init__(self, share_info):
		super().__init__()
		self.share_info = share_info
		self.url_head = "https://v.kuaishou.com/"

	def get_data(self):
		video_id = self.share_info.split("https://v.kuaishou.com/")[1][0:6]
		share_url = self.url_head + video_id
		res = requests.get(share_url,headers = self.headers)
		js_data = json.loads(re.findall('window.pageData= (.*?)</script>', res.text)[0])
		data = {}
		data['video'] = js_data['video']
		data['user'] = js_data['user']		
		return data 

	def parse_data(self):
		try:
			data = self.get_data()
			result = {
				"code": 200,
				"msg": "解析成功",
				"data": {
					"video": {
						"share_title": data['video']['caption'],
						"cover": data['video']['poster'],
						"play_addr": data['video']['srcNoMark']		
					},
					"author": {
						"id": data['user']['id'],
						"nickname": data['user']['name'],
						"avatar": data['user']['avatar']
					}
				},
				"developer": self.developer
			}
			return result
		except:
			return ResponseException(status_code= 500,msg="解析失败，请检查链接重试!")


if __name__ == '__main__':
	s = KuaishouSpider("大漠孤烟直，长河落日圆 https://v.kuaishou.com/aeh1wD 复制此消息，打开【快手】直接观看！")
	pprint(s.parse_data())

