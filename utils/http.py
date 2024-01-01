# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/12/29
Last Modified: 2023/12/29
Description: 
"""
import requests


class HttpRequest:
    def __init__(self, url):
        self.url = url

    def get_html(self):
        resp = requests.get(self.url)
        return resp.content.decode('utf8')
