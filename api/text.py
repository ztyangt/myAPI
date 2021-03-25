# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-23 18:41:43
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-23 18:47:59

import random
import time 
from fastapi import APIRouter
from spiders import Soul
from spiders import Joke
from spiders import Shici
from spiders import YiyanSpider
from spiders import TodaySpider
from pydantic import BaseModel
from typing import Optional

soul = APIRouter()
joke = APIRouter()
shici = APIRouter()
yiyan = APIRouter()
today = APIRouter()

categories = ["dongwu","jieri","renwu","shanshui","shenghuo","shiwu","shuqing","siji","tianqi","zhiwu"]
class PostData(BaseModel):
	category: Optional[str] = None

yiyan_list = ["a","b","c","d","e","f","g","h","i","j","k","l"]
class Yiyan(BaseModel):
	c: Optional[str] = None


class Todat(BaseModel):
	date: Optional[str] = None

@soul.get("/")
async def get_api():
	data = Soul().parse_data()
	return data

		

@joke.get("/")
async def get_api():
	data = Joke().parse_data()
	return data


@shici.get("/")
async def get_api(category: Optional[str] = None):
	if category == None:
		category = random.choice(categories)
	data = Shici(category).parse_data()
	return data
		
@shici.post("/")
async def post_api(param: PostData):
	category = param.dict()['category']
	if category == None:
		category = random.choice(categories)
	data = Shici(category).parse_data()
	return data

		
@yiyan.get("/")
async def get_api(c: Optional[str] = None):
	if c == None:
		c = random.choice(yiyan_list)
	data = YiyanSpider(c).parse_data()
	return data
		
@yiyan.post("/")
async def post_api(param: Yiyan):
	c = param.dict()['c']
	if c == None:
		c = random.choice(yiyan_list)
	data = YiyanSpider(c).parse_data()
	return data

		
@today.get("/")
async def get_api(date: Optional[str] = None):
	if date == None:
		date = time.strftime("%m-%d")
	data = TodaySpider(date).parse_data()
	return data
		
@today.post("/")
async def post_api(param: Todat):
	date = param.dict()['date']
	if date == None:
		date = time.strftime("%m-%d")
	data = TodaySpider(date).parse_data()
	return data