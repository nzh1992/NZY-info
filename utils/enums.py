# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/12/23
Last Modified: 2023/12/23
Description: 所有枚举类
"""
from enum import Enum


class HTTPMethod(Enum):
    """HTTP方法枚举"""
    GET = 'GET'
    POST = 'POST'


class HTTPStatusCode(Enum):
    """HTTP状态码枚举"""
    SUCCESS = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    SERVER_ERROR = 500



