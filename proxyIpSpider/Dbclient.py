"""
数据库功能
"""

import pymysql

# 输入 table 名，数据库默认为 db=proxy
class DbClient(object):
    def __init__(self, dbname):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db="proxy",
            charset='utf8')
        self.cursor = self.conn.cursor()
        self.name = dbname

    # 改名
    def change_table(self, name):
        self.name = name

    # 获取一个
    def get(self):
        try:
            sql = "select proxy from {}".format(str(self.name))
            print(sql)
            self.cursor.execute(sql)
            data = self.cursor.execute(sql)
            if data == 0:
                raise Exception("获取IP失败")
                pass
            data = self.cursor.fetchone()
            self.cursor.execute("DELETE FROM {} WHERE (proxy='{}')".format(self.name, str(data[0])))
            print("删除" + data[0])
            return data[0]
        finally:
            # self.cursor.close()
            self.conn.commit()

    # 插入数据
    def put(self, proxy):
        try:
            # sql = "insert into proxyip VALUES {}".format(proxy)
            self.cursor.execute("insert into {} VALUES (NULL, '{}')".format(self.name, str(proxy)))
            print("插入" + proxy)
        finally:
            # self.cursor.close()
            self.conn.commit()

    def delete(self, proxy):
        try:
            self.cursor.execute("DELETE FROM {} WHERE (proxy='{}')".format(self.name, str(proxy)))
            print("成功删除" + proxy)
        finally:
            self.conn.commit()

    # 返回列表
    def get_all(self):
        try:
            print("************")
            sql = "select proxy from {}".format(str(self.name))
            # self.cursor.execute(sql)
            data = self.cursor.execute(sql)
            if data == 0:
                data = self.cursor.fetchall()
                return [i[0] for i in data]
        finally:
            # self.cursor.close()
            self.conn.commit()

    # 删除表中全部数据
    def del_all(self, name):
        try:
            sql = "DELETE FROM {}".format(str(name))
            self.cursor.execute(sql)
        finally:
            self.conn.commit()

    def close_db(self):
        self.conn.close()
        print("关闭数据表 " + self.name)

if __name__ == '__main__':
    gg = DbClient("raw_proxy_queue")
    b = "9299.313.3.8338"
    # print(gg.get())
    # gg.pop("134.249.182.98:7777")
    gg.put("9299.313.3.8338")
    gg.change_table("useful_proxy_queue")
    gg.put(b)
    a = gg.get_all()
    print(a)
    # a = gg.get_all()
    # print(a)
    # print(b in a)

    gg.close_db()

