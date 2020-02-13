"""
检验代理可用
"""

from queue import Queue

import time

from ProxyCheck import ProxyCheck
from ProxyManager import ProxyManager


class ProxyValidSchedule(ProxyManager, object):
    def __init__(self):
        ProxyManager.__init__(self)
        self.queue = Queue()
        self.proxy_item = dict()

    def __validProxy(self, threads=10):
        """
        验证 useful_proxy 代理
        :param threads:
        :return:
        """
        thread_list = list()
        for index in range(threads):
            thread_list.append(ProxyCheck(self.queue, self.proxy_item))

        for thread in thread_list:
            thread.start()

        for thread in thread_list:
            thread.join()


    def putQueue(self):
        self.db.change_table(self.useful_proxy_queue)
        self.proxy_item = self.db.get_all()
        for item in self.proxy_item:
            self.queue.put(item)

    def main(self):
        self.putQueue()
        while True:
            if not self.queue.empty():
                self.__validProxy()
            else:
                time.sleep(60 * 5)
                self.putQueue()

def run():
    p = ProxyValidSchedule()
    p.main()

if __name__ == '__main__':
    p = ProxyValidSchedule()
    p.main()