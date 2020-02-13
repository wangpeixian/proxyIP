import time
from threading import Thread

from apscheduler.schedulers.blocking import BlockingScheduler

from ProxyManager import ProxyManager
from ToolFunction import verifyProxyFormat

class ProxyRefreshSchedule(ProxyManager):
    """
    定时刷新代理
    """
    def __init__(self):
        ProxyManager.__init__(self)

    def validProxy(self):
        """
        将 raw_proxy_item 中有效的 proxy 放入 use_proxy_item
        :return:
        """
        self.db.change_table(self.raw_proxy_queue)
        raw_proxy_item = self.db.get()
        remaining_proxies = self.get_all()

        if (raw_proxy_item not in remaining_proxies) and verifyProxyFormat(raw_proxy_item):
            self.db.change_table(self.useful_proxy_queue)
            self.db.put(raw_proxy_item)
            print("raw_proxy_item: ", raw_proxy_item)
        else:
            pass
        self.db.change_table(self.raw_proxy_queue)

def refreshPool():
    pp = ProxyRefreshSchedule()
    pp.validProxy()

def main(process_num=30):
    p = ProxyRefreshSchedule()
    # 获取新代理
    p.refresh()

    #检查新代理
    pl = []
    for num in range(process_num):
        proc = Thread(target=refreshPool, args=())
        pl.append(proc)

    for num in range(process_num):
        pl[num].start()

    for num in range(process_num):
        pl[num].join()

def run():
    main()
    sch = BlockingScheduler()
    sch.add_job(main, "interval", minutes=10)
    sch.start()

if __name__ == '__main__':
    main()


