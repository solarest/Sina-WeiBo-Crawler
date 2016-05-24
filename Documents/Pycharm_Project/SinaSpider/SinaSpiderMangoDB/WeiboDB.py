# -*- coding:utf8 -*-

import pymongo

class WeiboDB():

    def __init__(self):
        pass

    def db_connection(self):
        client = pymongo.MongoClient(host="127.0.0.1", port=27017)
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
    post = [{"name": "xiaoming", "age": "25"}, {"name": "xiaoqiang", "age": "24"}]
    test = WeiboDB()
    db = test.db_connection()
    my_collection = test.db_collection(db)
    test.db_insert(db, post)


