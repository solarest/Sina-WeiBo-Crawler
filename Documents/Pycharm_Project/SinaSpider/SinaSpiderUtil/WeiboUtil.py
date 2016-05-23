# -*-coding:utf8-*-
import time
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


if __name__ == '__main__':
    test = WeiboUtil()
    str = u'1729488283,3274267813,2240453567,2125019675,2510406354,2407890974,2005770630,1787283172,2758527590,2419402205'
    print test.Str2List(str, ",")

    print test.DateFormat("今天")


