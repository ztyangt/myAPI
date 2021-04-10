# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-04-09 22:24:41
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-04-09 23:03:18

from fastapi import APIRouter,Request
from spiders import IpLoction
from pydantic import BaseModel
from typing import Optional

class IpPost(BaseModel):
	ip: Optional[str] = None

iploc = APIRouter()


@iploc.get("/")
async def get_api(request: Request,ip: Optional[str] = None):
	if ip == None:
		ip = request.client.host
	data = IpLoction(ip).parse_data()
	return data

@iploc.post("/")
async def post_api(request: Request,param: IpPost):
	ip = param.dict()['ip']
	if ip == None:
		ip = request.client.host
	data = IpLoction(ip).parse_data()
	return data