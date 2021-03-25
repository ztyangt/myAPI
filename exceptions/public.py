# -*- coding: utf-8 -*-
# @Author: 很安静
# @Date:   2021-03-19 16:27:47
# @Email:   yang2210670@163.com
# @Blog:   https://blog.ztongyang.cn
# @Last Modified time: 2021-03-19 16:34:44


class ResponseException(Exception):
    def __init__(self, status_code: int, msg: str):
        self.status_code = status_code
        self.msg = msg
