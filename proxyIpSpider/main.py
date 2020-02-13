"""
主函数
"""

from multiprocessing import Process
from ProxyValidSchedule import run as ValidRun
from ProxyRefreshSchedule import run as RefreshRun

def run():
    p_list = list()
    p3 = Process(target=RefreshRun, name="RefreshRun")
    p_list.append(p3)
    p2 = Process(target=ValidRun, name="ValidRun")
    p_list.append(p2)


    for p in p_list:
        p.start()
    for p in p_list:
        p.join()

if __name__ == '__main__':
    run()