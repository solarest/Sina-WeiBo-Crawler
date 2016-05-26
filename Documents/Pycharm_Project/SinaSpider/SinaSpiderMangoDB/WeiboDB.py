# -*- coding:utf8 -*-
import ConfigParser
import pymongo
from SinaSpiderUtil.WeiboUtil import WeiboUtil


class WeiboDB():

    def __init__(self):
        Util = WeiboUtil()
        self.myhost = Util.ReadConfig("mangoDB", "host")
        self.myport = int(Util.ReadConfig("mangoDB", "port"))

    def db_connection(self, db_name):
        client = pymongo.MongoClient(host=self.myhost, port=self.myport)
        db_conn = client[db_name]
        return db_conn

    def db_collection(self, db_conn, collection_name):
        coll = db_conn[collection_name]
        return coll

    def db_insert(self, db_conn, collection_name, items):
        coll = db_conn[collection_name]
        information = items
        information_id = coll.insert(information)
        print information_id

    def db_search(self, db_conn, collection_name, key):
        pass

if __name__ == '__main__':
    post = [{"name": "aaa", "age": "25"}, {"name": "bbb", "age": "24"}]
    test = WeiboDB()
    db_conn = test.db_connection("SinaWeibo")
    test.db_insert(db_conn, "test", post)
