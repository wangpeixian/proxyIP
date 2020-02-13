"""
功能函数
"""
import requests


def verifyProxyFormat(proxy):
    """
    检查代理格式
    :param proxy:
    :return:
    """
    import re
    verify_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"
    _proxy = re.findall(verify_regex, proxy)
    return True if len(_proxy) == 1 and _proxy[0] == proxy else False

def validUsefulProxy(proxy):
    """
    检验代理是否可用
    :param proxy:
    :return:
    """
    proxies = {"http": "http://{proxy}".format(proxy=proxy)}
    try:
        r = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=10, verify=False)
        if r.status_code == 200:
            return True
    except Exception as e:
        return False