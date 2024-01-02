# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/12/23
Last Modified: 2023/12/23
Description: 
"""
from crawler.resource.china_agriculture import ChinaAgricultureMinistry
from crawler.resource.liaoning import LiaoNingAgriculture
from crawler.spider import Spider
from crawler.models import News


class SpiderEngine:
    """爬虫引擎"""
    def __init__(self):
        self.status = True

        # 待爬取资源列表
        self.src_list = [
            # ChinaAgricultureMinistry,
            LiaoNingAgriculture
        ]

    def start(self):
        """启动爬虫引擎"""
        for src in self.src_list:
            # 获取不同资源的爬取计划
            schedual_list = src().make_schedual(hisotry=True)

            for schedual in schedual_list:
                spi = Spider(schedual)
                result = spi.parse_html()

                # 写入数据库
                news = News()
                news.create(**result)

    def stop(self):
        """停止爬虫引擎"""
        pass
