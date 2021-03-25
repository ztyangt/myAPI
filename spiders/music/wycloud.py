# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-24 09:25:49
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-24 10:39:14

import requests,json
from pprint import pprint
from exceptions import ResponseException
from spiders import Public

class WycloudSpider(Public):
	def __init__(self, music_id):
		super(WycloudSpider, self).__init__()
		self.music_id = music_id
		self.api = "https://api.imjad.cn/cloudmusic/?type={}&id={}&br={}"

	def parse_data(self):
		try:
			res1 = requests.get(self.api.format("detail",self.music_id,""),headers = self.headers)
			data1 = json.loads(res1.text)
			br = data1["songs"][0]["h"]["br"]
			res2 = requests.get(self.api.format("song",self.music_id,br),headers = self.headers)
			data2 = json.loads(res2.text)
			music = data2['data'][0]["url"]
			res3 = requests.get(self.api.format("lyric",self.music_id,""),headers = self.headers)
			data3 = json.loads(res3.text)
			lyric = data3['lrc']["lyric"]
			result = {
				"code":200,
				"msg": "success",
				"data": {
					"name": data1["songs"][0]["name"],
					"br": br,
					"author": data1["songs"][0]["ar"][0]["name"],
					"picurl": data1["songs"][0]["al"]["picUrl"],
					"music": music,
					"lyric": lyric,
				},
				"developer": self.developer
			}
			return result
		except:
			return ResponseException(status_code= 500,msg="解析失败，请检查链接重试!")		


		
	