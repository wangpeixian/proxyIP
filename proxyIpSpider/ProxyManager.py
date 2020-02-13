"""
对代理操作
"""
import random

from GetConfig import GetConfig
from Dbclient import DbClient
from GetFreeProxy import GetFreeProxy
from ToolFunction import *

class ProxyManager(object):
    def __init__(self):
        self.db = DbClient("raw_proxy_queue")
        self.config = GetConfig()
        self.raw_proxy_queue = "raw_proxy_queue"
        self.useful_proxy_queue = "useful_proxy_queue"


    def refresh(self):
        """
        获取代理，存储到 proxy.raw_proxy 数据表中
        :return:
        """
        for proxyGetter in self.config.proxy_getter_functions:
            proxy_set = set()
            try:
                proxy_iter = [_ for _ in getattr(GetFreeProxy, proxyGetter.strip())()]
            except Exception as e:
                continue

            for proxy in proxy_iter:
                proxy = proxy.strip()
                if proxy and verifyProxyFormat(proxy):
                    proxy_set.add(proxy)
                else:
                    pass

            for proxy in proxy_set:
                self.db.change_table(self.raw_proxy_queue)
                self.db.put(proxy)

    def get(self):
        self.db.change_table(self.useful_proxy_queue)
        item_dict = self.db.get_all()
        if item_dict:
            return random.choice(list(item_dict.keys()))
        return None

    def delete(self, proxy):
        """
        删除表
        :param proxy:
        :return:
        """
        self.db.change_table(self.useful_proxy_queue)
        self.db.delete(proxy)

    def get_all(self):
        """
        获取全部
        :return:
        """
        self.db.change_table(self.useful_proxy_queue)
        item_dict = self.db.get_all()
        return list(item_dict.keys()) if item_dict else list()


