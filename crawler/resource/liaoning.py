# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2024/1/1
Last Modified: 2024/1/1
Description: 辽宁省农业农村厅
"""
from bs4 import BeautifulSoup

from utils.dt import DateTime
from utils.http import HttpRequest
from utils.text import TextProcess


class LiaoNingAgriculture:
    """辽宁省农业农村厅"""
    def __init__(self):
        self.base_url = "https://nync.ln.gov.cn"
        self.name = "辽宁省农业农村厅"

        # 通知公告
        self.tzgg_url = "https://nync.ln.gov.cn/nync/index/tzgg/"
        # 农业要闻-农业新闻-农业要闻
        self.nyyw_nyyw = "https://nync.ln.gov.cn/nync/index/nyyw/nyxw/nyyw/index.shtml"
        # 农业要闻-农业新闻-工作动态
        self.nyyw_gzdt = "https://nync.ln.gov.cn/nync/index/nyyw/nyxw/gzdt/index.shtml"
        # 农业要闻-农业新闻-文化活动
        self.nyyw_whhd = "https://nync.ln.gov.cn/nync/index/nyyw/nyxw/whhd/index.shtml"
        # 新闻动态-全省农业信息联播
        self.xwdt_qsnyxx = "https://nync.ln.gov.cn/nync/index/nyyw/zsqsnyxxlb/index.shtml"

        self.sections = [
            self.tzgg_url,
            self.nyyw_nyyw,
            self.nyyw_gzdt,
            self.nyyw_whhd,
            self.xwdt_qsnyxx
        ]

    def _get_href(self, li_tag):
        """
        从列表标签中提取出新闻详情的连接

        :param base_url: str. 网站的url前缀
        :param li_tag: bs4.Tag. li标签
        :return:
        """
        href = li_tag.find('a')['href']
        return self.base_url + href

    def _get_date(self, li_tag, encoding="utf8"):
        """获取li标签中的日期"""
        li_html = li_tag.encode_contents().decode(encoding)
        tp = TextProcess(li_html)
        return tp.get_date()

    def _make_href_meta(self, href):
        """记录新闻详情url的同时，记录其他网站元信息"""
        href_meta = {
            "web_source": self.name,
            "href": href
        }
        return href_meta

    def make_schedual(self, hisotry=False):
        """
        制定爬虫计划。获取待爬取新闻详情url以及网站的元信息。

        :param hisotry: bool. 默认False，仅爬取当日新闻。如果为True爬取所有历史新闻
        :return: list.
        """
        # 全部待爬取url
        urls = []

        for section_url in self.sections:
            # 获取
            index_html = HttpRequest(section_url).get_html()
            soup = BeautifulSoup(index_html, 'html.parser')

            # 文字区域
            text_div = soup.find("div", {"class": "workmenu"})
            # 获取所有ul中的li标签对象
            li_tags = text_div.ul.find_all("li")

            for li_tag in li_tags:
                date = self._get_date(li_tag)

                # 根据history字段判定，是爬取前一天还是数据，还是所有历史数据
                if hisotry:
                    href = self._get_href(li_tag)
                    href_meta = self._make_href_meta(href)
                    urls.append(href_meta)
                else:
                    yesterday_date = DateTime.get_yesterday_date_str()
                    if yesterday_date in date:
                        href = self._get_href(li_tag)
                        href_meta = self._make_href_meta(href)
                        urls.append(href_meta)

        return urls

