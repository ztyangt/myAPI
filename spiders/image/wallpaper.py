# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-21 10:14:27
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-23 18:29:01

import requests,json,re
from pprint import pprint
from lxml import etree
from exceptions import ResponseException
from spiders import Public

class PaperSpider(Public):
	def __init__(self):
		super().__init__()
		self.random_api = "https://wallhaven.cc/random"
		self.pic_api = "https://wallhaven.cc/w/"
	
	def get_picID(self):
		res = requests.get(self.random_api,headers = self.headers)
		html = etree.HTML(res.text)
		url = html.xpath('//*[@id="thumbs"]/section/ul/li[1]/figure/a/@href')[0]
		picID = url.split("/")[-1]
		return picID

	def parse_data(self):
		try:
			picID = self.get_picID()
			url = self.pic_api + picID
			res = requests.get(url,headers = self.headers)
			html = etree.HTML(res.text)
			picurl = html.xpath('//*[@id="wallpaper"]/@src')[0]
			size = html.xpath('//*[@id="showcase-sidebar"]/div/div[1]/div[2]/dl/dd[4]/text()')[0]
			views = html.xpath('//*[@id="showcase-sidebar"]/div/div[1]/div[2]/dl/dd[5]/text()')[0]
			name_list = html.xpath('//*[@class="showcase-uploader"]/a/img[1]/@alt')
			name = name_list[0] if len(name_list) != 0 else "Unknown"
			avatar_url = html.xpath('//*[@class="showcase-uploader"]/a/img[1]/@data-cfsrc')[0]
			avatar = avatar_url if "http" in avatar_url else "https:" + avatar_url 
			time = html.xpath('//*[@id="showcase-sidebar"]/div/div[1]/div[2]/dl/dd[1]/time/@title')[0]

			result = {
				"code": 200,
				"data": {
					"image": {
						"pic_id": picID,
						"size": size,
						"views": views,
						"time": time,
						"picurl": picurl,
					},
					"author": {
						"name": name,
						"avatar": avatar
					}
				},
				"developer":self.developer
			}
			return result
		except:
			return ResponseException(status_code= 500,msg="解析失败，请检查链接重试!")


if __name__ == '__main__':
	s = PaperSpider()
	pprint(s.parse_data())

