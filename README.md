## IP代理池

#### 项目介绍:

##### GetFreeProxy.py
从免费代理网站获取ip：

66ip.cn

http://www.xicidaili.com

www.kuaidaili.com

www.mimiip.com

##### ToolFunction.py

用于检测抓取到的IP是否正确：

正则表达式校验格式是否正确。

通过访问 http://httpbin.org/ip 查看返回状态码判断是否可用

##### Dbclient.py

封装了对**Redis数据库**的操作

##### ProxyManager.py

refresh：用于启动抓取IP的方法，所得到的数据在经过格式检验后存入数据库中

get：弹出一个IP

delete：删除一个IP

get_all：返回全部IP列表

##### ProxyRefreshSchedule.py

获得新代理，放入 raw_proxy_item。

多线程校验IP可用性。

将可用IP从 raw_proxy_item 放入 use_proxy_item 中。

##### ProxyValidSchedule.py

定时校验可用IP，保证IP池中IP活性。

如果可用IP不足，将自动启动获取方法，重新获取IP。

##### ProxyCheck.py

用于定时检验IP的方法

##### GetConfig.py

获取IP线程的相关设置信息（config.ini）


##### main.py

程序启动

#### 项目启动方式
先在 Dbclient.py 中配置数据库

运行 main.py 文件即可

获取的IP以及可用IP会保存到本地数据库中，其他程序可直接获取。

#### 其他

也可以尝试将该程序跑在云服务器上，直接调用api使用IP

速度是够用的。已经封装了几个方法，在 ProxyManager.py 中。

比如直接用Falsk，需要获取ip时直接：

xxx.xxx.xxx.xxx/get

项目还有很大改进，如果有时间将继续完善。

