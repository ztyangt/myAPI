# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-19 11:42:16
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-24 10:29:40

import uvicorn
from fastapi import FastAPI,Request
from exceptions import ResponseException
from api import douyin,kuaishou,weishi 
from api import wallpaper,bizhi,bing
from api import soul,joke,shici,yiyan,today
from api import wycloud

# 接口列表
app = FastAPI()
# 视频解析类
app.include_router(douyin, prefix = '/douyin', tags = ['抖音解析接口'])
app.include_router(kuaishou, prefix = '/kuaishou', tags = ['快手解析接口'])
app.include_router(weishi, prefix = '/weishi', tags = ['微视解析接口'])
#图片资源类
app.include_router(wallpaper, prefix = '/wallpaper', tags = ['随机壁纸接口'])
app.include_router(bizhi, prefix = '/bizhi', tags = ['360随机壁纸'])
app.include_router(bing, prefix = '/bing', tags = ['必应每日壁纸'])
#文字信息类
app.include_router(soul, prefix = '/soul', tags = ['心灵毒汤'])
app.include_router(joke, prefix = '/joke', tags = ['笑话大全'])
app.include_router(shici, prefix = '/shici', tags = ['随机诗词'])
app.include_router(yiyan, prefix = '/yiyan', tags = ['Hitokoto一言'])
app.include_router(today, prefix = '/today', tags = ['历史上的今天'])
# 音乐解析类
app.include_router(wycloud, prefix = '/wycloud', tags = ['网易云音乐解析'])

# 异常响应
@app.exception_handler(ResponseException)
async def unicorn_exception_handler(request: Request, exc: ResponseException):
    return JSONResponse(
        status_code= exc.status_code,
        content={"msg": exc.msg},
    )
if __name__ == '__main__':
	uvicorn.run('run:app', host='0.0.0.0', port = 5000, reload = True)

# 启动命令： uvicorn run:app --reload