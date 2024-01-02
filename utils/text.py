# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2024/1/2
Last Modified: 2024/1/2
Description: 
"""
import re


class TextProcess:
    """文本处理工具类"""
    def __init__(self, text):
        self.text = text

    def get_date(self):
        """获取日期，格式为'YYYY-mm-dd'"""
        date_format_rex = r"(\d{4}-\d{1,2}-\d{1,2})"
        match = re.search(date_format_rex, self.text)
        groups = match.groups()

        if not groups:
            return ""
        else:
            return groups[0]
