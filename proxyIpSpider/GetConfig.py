"""
读取配置文件
"""
import os
from configparser import ConfigParser
from ToolClass import LazyProperty


class GetConfig(object):
    def __init__(self):
        # 本文件路径
        self.pwd = os.path.split(os.path.realpath(__file__))[0]
        self.config_path = os.path.join(self.pwd, "Config.ini")
        self.config_file = ConfigParser()
        self.config_file.read(self.config_path)

    @LazyProperty
    def proxy_getter_functions(self):
        return self.config_file.options('ProxyGetter')
if __name__ == '__main__':
    gg = GetConfig()
    print(gg.proxy_getter_functions)