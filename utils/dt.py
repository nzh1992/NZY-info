# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/12/23
Last Modified: 2023/12/23
Description: 
"""
from datetime import datetime, timedelta


class DateTime:
    DATE_FORMAT = "%Y-%m-%d"
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    ALLOWED_FORMATS = [
        "%Y-%m-%d %H:%M"
    ]

    @classmethod
    def get_current_dt(cls):
        """
        获取当前时间(datetime对象)
        """
        return datetime.now()

    @classmethod
    def get_current_dt_str(cls):
        """
        获取当前时间(字符串格式)
        """
        return datetime.now().strftime(cls.DATETIME_FORMAT)

    @classmethod
    def get_current_date_str(cls):
        """
        获取当前日期(字符串格式)
        """
        return datetime.now().strftime(cls.DATE_FORMAT)

    @classmethod
    def get_yesterday_date_str(cls):
        yesterday = datetime.now() - timedelta(days=1)
        return yesterday.strftime(cls.DATE_FORMAT)

    @classmethod
    def format_dt(cls, dt_str):
        """格式化时间字符串为标准格式"""
        for fmt in cls.ALLOWED_FORMATS:
            try:
                dt = datetime.strptime(dt_str, fmt)
            except Exception:
                pass
            else:
                return dt.strftime(cls.DATETIME_FORMAT)

        return ""