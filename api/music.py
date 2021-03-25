# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-24 10:24:44
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-24 10:28:07

from fastapi import APIRouter
from spiders import WycloudSpider
from pydantic import BaseModel

class WyPost(BaseModel):
	music_id: str

wycloud = APIRouter()

@wycloud.get("/")
async def get_api(music_id: str):
	data = WycloudSpider(music_id).parse_data()
	return data

@wycloud.post("/")
async def post_api(param: WyPost):
	music_id = param.dict()['music_id']
	data = WycloudSpider(music_id).parse_data()
	return data