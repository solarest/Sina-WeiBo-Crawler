# -*- coding:utf8 -*-
import ConfigParser
import pymongo

class WeiboDB():

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read("/Users/mac/Documents/Pycharm_Project/SinaSpider/info.ini")
        self.myhost = config.get("mangoDB", "host")
        self.myport = int(config.get("mangoDB", "port"))

    def db_connection(self):
        client = pymongo.MongoClient(host=self.myhost, port=self.myport)
        db = client['SinaWeiboData']
        return db

    def db_collection(self, db):
        coll = db["SinaWeiboData"]
        return coll

    def db_insert(self, db, items):
        coll = db['SinaWeiboData']
        information = items
        information_id = coll.insert(information)
        print information_id

if __name__ == '__main__':
    post = [{"name": "aaa", "age": "25"}, {"bbb": "xiaoqiang", "age": "24"}]
    test = WeiboDB()
    db = test.db_connection()
    my_collection = test.db_collection(db)
    test.db_insert(db, post)


