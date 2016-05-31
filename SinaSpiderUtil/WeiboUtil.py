# -*-coding:utf8-*-
import time
import ConfigParser

class WeiboUtil:

    def Str2List(self, mystr, sign):
        use_list = mystr.split(sign)
        return use_list

    def DateFormat(self, mydate):
        if (mydate == u"今天"):
            use_date = time.strftime('%m月%d日', time.localtime(time.time()))
        else:
            use_date = mydate
        return use_date

    def Complete_uid_url(self, uid_list):
        uid_urls = []
        # http://weibo.cn/1729488283
        for uid in uid_list:
            uid_url = "http://weibo.cn/"+uid
            uid_urls.append(uid_url)
        return uid_urls

    def ReadConfig(self, tag, key):
        config = ConfigParser.ConfigParser()
        config.read("/Users/mac/Documents/Pycharm_Project/SinaSpider/info.ini")
        use_value = config.get(tag, key)
        return use_value

if __name__ == '__main__':
    test = WeiboUtil()
    # str = u'1729488283,3274267813,2240453567,2125019675,2510406354,2407890974,2005770630,1787283172,2758527590,2419402205'
    # print test.Str2List(str, ",")

    # print test.DateFormat(u"今天")
    # print test.Complete_uid_url([u'1729488283'])

    college_List = test.ReadConfig("college", "Chengdu")
    lists = test.Str2List(college_List, ",")
    for i in lists:
        print i
