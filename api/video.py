# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-23 18:30:49
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-23 18:36:22

from fastapi import APIRouter
from spiders import DouyinSpider
from spiders import KuaishouSpider
from spiders import WeishiSpider
from pydantic import BaseModel

douyin = APIRouter()
kuaishou = APIRouter()
weishi = APIRouter()

class PostData(BaseModel):
	share_info: str
		

@douyin.get("/")
async def get_api(share_info: str):
	data = DouyinSpider(share_info).parse_data()
	return data
		
@douyin.post("/")
async def post_api(param: PostData):
	share_info = param.dict()['share_info']
	data = DouyinSpider(share_info).parse_data()
	return data
	


@kuaishou.get("/")
async def get_api(share_info: str):
	data = KuaishouSpider(share_info).parse_data()
	return data
		
@kuaishou.post("/")
async def post_api(param: PostData):
	share_info = param.dict()['share_info']
	data = KuaishouSpider(share_info).parse_data()
	return data



@weishi.get("/")
async def get_api(share_info: str):
	data = WeishiSpider(share_info).parse_data()
	return data
		

@weishi.post("/")
async def post_api(param: PostData):
	share_info = param.dict()['share_info']
	data = WeishiSpider(share_info).parse_data()
	return data