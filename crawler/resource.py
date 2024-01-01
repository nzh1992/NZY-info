# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/12/23
Last Modified: 2023/12/23
Description: 网站资源
"""
from bs4 import BeautifulSoup

from utils.dt import DateTime
from utils.http import HttpRequest


class ChinaAgricultureMinistry:
    """中华人民共和国农业农村部"""
    def __init__(self):
        self.index_url = "http://www.moa.gov.cn/xw/"
        self.name = "中华人民共和国农业农村部"

        # 农业农村部动态
        self.zwdt_url = "http://www.moa.gov.cn/xw/zwdt/"
        # 全国信息联播
        self.qg_url = "http://www.moa.gov.cn/xw/qg/"
        # 部门动态
        self.bmdt_url = "http://www.moa.gov.cn/xw/bmdt/"
        # 机关党建
        self.lzjs_url = "http://www.moa.gov.cn/xw/lzjs/"
        # 国际交流
        self.gjjl_url = "http://www.moa.gov.cn/xw/gjjl/"

        self.sections = [self.zwdt_url, self.qg_url, self.bmdt_url, self.lzjs_url, self.gjjl_url]

    def _get_href(self, base_url, li_tag):
        """
        从列表标签中提取出新闻详情的连接

        :param base_url: str. 网站的url前缀
        :param li_tag: bs4.Tag. li标签
        :return:
        """
        href = li_tag.find('a')['href'][2:]
        return base_url + href

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

        for base_url in self.sections:
            # 获取
            index_html = HttpRequest(base_url).get_html()
            soup = BeautifulSoup(index_html, 'html.parser')

            # 文字区域
            text_div = soup.find("div", {"class": "pub-media1-txt-list fullwidth"})
            # 获取所有ul中的li标签对象
            li_tags = text_div.ul.find_all("li")

            for li_tag in li_tags:
                li_date = li_tag.span.get_text()

                # 根据history字段判定，是爬取前一天还是数据，还是所有历史数据
                if hisotry:
                    href = self._get_href(base_url, li_tag)
                    href_meta = self._make_href_meta(href)
                    urls.append(href_meta)
                else:
                    yesterday_date = DateTime.get_yesterday_date_str()
                    if yesterday_date in li_date:
                        href = self._get_href(base_url, li_tag)
                        href_meta = self._make_href_meta(href)
                        urls.append(href_meta)

        return urls
