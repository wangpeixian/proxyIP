"""

"""
from threading import Thread
from queue import Queue

from ProxyManager import ProxyManager
from ToolFunction import validUsefulProxy

FAIL_COUNT = 1

class ProxyCheck(ProxyManager, Thread):
    def __init__(self, queue, item_dict):
        ProxyManager.__init__(self)
        Thread.__init__(self)
        self.queue = queue
        self.item_dict = item_dict

    def run(self):
        self.db.change_table(self.useful_proxy_queue)
        while self.queue.qsize():
            proxy = self.queue.get()
            count = self.item_dict
            if validUsefulProxy(proxy):
                self.db.put(proxy)
            else:
                self.db.delete(proxy)
            # 发送检索完毕的信号
            self.queue.task_done()



if __name__ == '__main__':
    pass
