# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/12/23
Last Modified: 2023/12/23
Description: 读取根目录中settings.ini配置文件，并对外提供接口
"""
import os


class ConfigurationManager:
    """配置管理器"""
    def __init__(self):
        config_fp = os.path.join(os.getcwd(), "settings.ini")
        self.config_fp = config_fp
