# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-23 18:37:14
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-23 18:39:04
import random
from fastapi import APIRouter
from spiders import PaperSpider
from spiders import BizhiSpider
from spiders import BingSpider
from pydantic import BaseModel
from typing import Optional

wallpaper = APIRouter()
bing = APIRouter()
bizhi = APIRouter()		

@wallpaper.get("/")
async def get_api():
	data = PaperSpider().parse_data()
	return data

@bing.get("/")
async def get_api():
	data = BingSpider().parse_data()
	return data

class PostData(BaseModel):
	cid: Optional[int] = None
	count: Optional[int] = 1
		
cid_list = [36,30,9,15,26,11,14,5,6,10,22,16,32,35,1]

@bizhi.get("/")
async def get_api(cid: Optional[int] = None,count:Optional[int] = 1):
	if cid == None:
		cid = random.choice(cid_list)
	data = BizhiSpider(cid,count).parse_data()
	return data
		

@bizhi.post("/")
async def post_api(param: PostData):
	cid = param.dict()['cid']
	if cid == None:
		cid = random.choice(cid_list)
	count = param.dict()['count']
	data = BizhiSpider(cid,count).parse_data()
	return data