# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/12/29
Last Modified: 2023/12/29
Description: 
"""
from utils.db import mongo
from utils.dt import DateTime


class News:
    def __init__(self):
        pass

    def create(self, **kwargs):
        """
        创建新闻

        :param kwargs: dict.
        :return:
        """
        # 新闻标题
        title = kwargs.get("title", "")
        # 发布日期
        publish_time = kwargs.get("publish_time", "")
        publish_time_formated = DateTime.format_dt(publish_time)
        # 作者
        author = kwargs.get("author", "")
        # 新闻内容
        content = kwargs.get("content", "")

        # 来自网站
        web_source = kwargs.get("web_source", "")
        # 来自网站的哪个部分
        section_source = kwargs.get("section_source", "")
        # 省份(全国就保存'全国'，省份就保存省名)
        province = kwargs.get("province", "")
        # 写入时间
        create_time = DateTime.get_current_dt_str()

        news_data = {
            "title": title,
            "publish_time": publish_time_formated,
            "author": author,
            "content": content,
            "web_source": web_source,
            "section_source": section_source,
            "province": province,
            "create_time": create_time,
        }

        mongo.news.insert_one(news_data)
