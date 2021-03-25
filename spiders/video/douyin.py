# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-19 13:05:46
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-23 18:25:00

import requests,json,re
from pprint import pprint
from exceptions import ResponseException
from spiders import Public

class DouyinSpider(Public):
	def __init__(self,share_info):
		super().__init__()
		self.share_info = share_info
		self.url_head = "https://v.douyin.com/"
		self.data_api = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids="
	
	def get_mid(self):
		share_url = 'https://v.douyin.com/' + re.findall('https://v.douyin.com/(.*?)/', self.share_info)[0] + "/"
		url = requests.get(share_url,headers = self.headers).url
		mid = re.findall('video/(.*?)/', url)[0]
		return mid

	def get_data(self):
		res = requests.get(self.data_api + self.get_mid(),headers = self.headers)
		js_data = json.loads(res.text)
		play_url = js_data['item_list'][0]['video']['play_addr']['url_list'][0].replace("playwm","play")
		video_url = requests.get(play_url,headers = self.headers).url
		js_data['item_list'][0]['video']['play_addr']['url_list'][0] = video_url
		return js_data

	def parse_data(self):
		try:
			data = self.get_data()
			if data['status_code'] == 0:
				code = 200 
			else:
				code = 0
			data = data['item_list'][0]
			result = {
				"code": code,
				"msg": "解析成功",
				"data": {
					"video": {
						"comment_count": data['statistics']['comment_count'],
						"digg_count": data['statistics']['digg_count'],
						"share_count": data['statistics']['share_count'],			
						"share_title": data['share_info']['share_title'],
						"cover": data['video']['cover']['url_list'][0],
						"music": data['music']['play_url']['url_list'][0],
						"play_addr": data['video']['play_addr']['url_list'][0]		
					},
					"author": {
						"uid": data['author']['uid'],
						"short_id": data['author']['short_id'],
						"nickname": data['author']['nickname'],
						"avatar": data['author']['avatar_larger']['url_list'][0]
					}
				},
				"developer": self.developer
			}
			return result
		except:
			return ResponseException(status_code= 500,msg="解析失败，请检查链接重试!")

if __name__ == '__main__':
	share_info = "抖音解析 %景甜太喜欢 司藤的这套衣服和造型，真的很像公主  %司藤谈恋爱会开花  %网剧司藤  %景甜新剧人设好飒  https://v.douyin.com/eLyndWT/ 复制此链接，答开Dou音搜索，値接观看视频！"
	s = DouyinSpider(share_info)
	pprint(s.parse_data())
