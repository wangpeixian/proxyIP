"""
获取免费代理
"""
import re
import requests
from bs4 import BeautifulSoup
import pymysql
import time

"""
    66ip.cn
    data5u.com
    xicidaili.com
    goubanjia.com
    xdaili.cn
    kuaidaili.com
    cn-proxy.com
    proxy-list.org
    www.mimiip.com to do
"""


class GetFreeProxy():
    def __init__(self):
        pass

    @staticmethod
    def method_1(pages=2):
        """
        66ip.cn
        :return:
        """
        url = "http://www.66ip.cn/{}.html"

        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        header = {"User-Agent": user_agent}
        for page in range(1, pages):
            data = requests.get(url.format(page), headers=header)
            data.encoding = 'gb2312'
            data = data.text
            soup = BeautifulSoup(data, 'lxml')
            title = soup.select("#main > div > div:nth-of-type(1) > table tr")
            # print(title)
            ##main > div > div:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(1)
            for i in range(1, len(title)):
                ip = title[i].select("td:nth-of-type(1)")[0].get_text()
                port = title[i].select("td:nth-of-type(2)")[0].get_text()
                # print("{}:{}".format(ip, port))
                yield ("{}:{}".format(ip, port))

    @staticmethod
    def method_2(pages=2):
        """
        西刺
        http://www.xicidaili.com
        :return:
        """
        url = "http://www.xicidaili.com/nn/{}"

        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        header = {"User-Agent": user_agent}
        for page in range(1, pages):
            data = requests.get(url.format(str(page)), headers=header).text
            soup = BeautifulSoup(data, "lxml")

            title = soup.select(".odd")

            for i in title:
                ip = i.select("td:nth-of-type(2)")[0].get_text()
                port = i.select("td:nth-of-type(3)")[0].get_text()
                # proxy = "{}:{}".format(ip, port)
                yield ("{}:{}".format(ip, port))
                # print(proxy)

    @staticmethod
    def method_3(pages=2):
        """

        :return:
        """
        url = "https://www.kuaidaili.com/free/inha/{}/"

        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        header = {"User-Agent": user_agent}
        for page in range(1, pages):
            data = requests.get(url.format(str(page)), headers=header).text
            soup = BeautifulSoup(data, "lxml")

            title = soup.select("#list > table > tbody tr")

            for i in title:
                ip = i.select("td:nth-of-type(1)")[0].get_text()
                port = i.select("td:nth-of-type(2)")[0].get_text()
                # proxy = "{}:{}".format(ip, port)
                yield ("{}:{}".format(ip, port))
                # print(proxy)
                # print('')

    @staticmethod
    def method_4(pages=2):
        """
        http://www.mimiip.com/gngao/2
        :param pages:
        :return:
        """
        url = "http://www.mimiip.com/gngao/{}"
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        header = {"User-Agent": user_agent}
        for page in range(1, pages):
            data = requests.get(url.format(str(page)), headers=header).text
            soup = BeautifulSoup(data, "lxml")

            # #middle_wrapper > div > table > tbody > tr:nth-child(1)
            # #middle_wrapper > div > table > tbody
            title = soup.select("div table tr")

            for i in title:
                ip = i.select("td:nth-of-type(1)")
                port = i.select("td:nth-of-type(2)")
                if ip and port:
                    ip = ip[0].get_text()
                    port = port[0].get_text()
                    proxy = "{}:{}".format(ip, port)
                    yield ("{}:{}".format(ip, port))
                    # print(proxy)
                    # print("")

if __name__ == '__main__':
    gg = GetProxy()
    li = gg.method_1(3)

    for i in li:
        print(i)

