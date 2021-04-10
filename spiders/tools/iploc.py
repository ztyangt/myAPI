import requests,json,re
from pprint import pprint
from exceptions import ResponseException
from spiders import Public

class IpLoction(Public):
	def __init__(self,ip):
		super().__init__()
		self.ip = str(ip)
		self.data_api = "https://api.map.baidu.com/location/ip?ak=hXpgwTZBxn1Bdaf0yxHI0VeKqd6xMuHz&ip={}&coor=bd09ll"
	

	def get_data(self):
		res = requests.get(self.data_api.format(self.ip),headers = self.headers)
		js_data = json.loads(res.text)
		return js_data

	def parse_data(self):
		try:
			data = self.get_data()
			result = {
				"code": 200,
				"msg": "请求成功",
				"data": data,
				"developer": self.developer
			}
			return result
		except:
			return ResponseException(status_code= 500,msg="解析失败，请检查链接重试!")

if __name__ == '__main__':
	ip = ""
	s = IpLoction(ip)
	pprint(s.parse_data())
