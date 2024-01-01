# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/12/23
Last Modified: 2023/12/23
Description: 爬虫
"""
from datetime import datetime

from bs4 import BeautifulSoup

from utils.http import HttpRequest


class Spider:
    def __init__(self, schedual):
        """
        :param schedual: dict. 待爬取元信息
        """
        self.detail_url = schedual.get("href")
        self.web_source = schedual.get("web_source")

    def parse_html(self):
        """解析新闻详情页内容"""
        detail_html = HttpRequest(self.detail_url).get_html()

        detail = {
            "web_source": self.web_source,
            "province": "全国",
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        soup = BeautifulSoup(detail_html, 'html.parser')

        # 新闻标题部分
        title_divs = soup.find_all('h1', {"class": "bjjMTitle"})
        titles = [div.get_text() for div in title_divs]
        title = "".join(titles)
        detail["title"] = title

        author_tag = soup.find("div", {"class": "bjjMAuthorBox"})

        # 作者部分
        author_tags = author_tag.find_all("span", {"class": "dc_3"})
        # 发布日期
        publish_time = author_tags[0].get_text()
        detail["publish_time"] = publish_time
        # 作者
        author_name = author_tags[1].get_text()
        detail["author_name"] = author_name
        # 来源
        source = author_tags[2].get_text()
        detail["source"] = source

        # 内容部分
        content_tag = soup.find("div", {"class": "TRS_Editor"}).div
        if content_tag.get_text():
            detail['content'] = content_tag.get_text()
            return detail

        paragraph_divs = content_tag.find_all("div")
        if paragraph_divs:
            paragraph_list = [div.get_text() for div in paragraph_divs]
            content = "".join(paragraph_list)
            detail['content'] = content
        else:
            p_tags = content_tag.find_all("p")
            p_list = [p.get_text() for p in p_tags]
            content = "".join(p_list)
            detail['content'] = content

        return detail
