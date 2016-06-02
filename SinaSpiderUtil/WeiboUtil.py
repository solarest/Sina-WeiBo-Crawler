# -*-coding:utf8-*-
import time
import ConfigParser


class WeiboUtil:

    def Str2List(self, mystr, sign):
        use_list = mystr.split(sign)
        return use_list

    def FormatTimeString(self, unformatTimeString, unformatTimeStyle):
        formatTime = time.strptime(unformatTimeString ,unformatTimeStyle)
        formatTimeString = time.strftime("%Y-%m-%d", formatTime)
        return formatTimeString

    #TODO: Solve encoding porblem!

    def DateFormat(self, mydate):
        if (mydate == u"今天" or mydate.find(u"分钟前") is not -1):
            use_date = time.strftime('%Y-%m-%d')
        elif (mydate.find(u"月") is not -1):
            use_date = self.FormatTimeString((time.strftime("%Y")+u"年"+mydate).encode('utf-8'),"%Y年%m月%d日")
        else:
            use_date = mydate
        try:
            use_date = use_date.decode('utf-8')
        except:
            pass
        return use_date

    @classmethod
    def Complete_uid_url(cls, uid_list):
        uid_urls = []
        for uid in uid_list:
            uid_url = "http://weibo.cn/"+uid
            uid_urls.append(uid_url)
        return uid_urls

    @classmethod
    def ReadConfig(cls, tag, key):
        config_info_path = "/Users/mac/Documents/Pycharm_Project/SinaWeiboSpider/info.ini"
        config = ConfigParser.ConfigParser()
        config.read(config_info_path)
        use_value = config.get(tag, key)
        return use_value

if __name__ == '__main__':
    test = WeiboUtil()
    college_List = WeiboUtil.ReadConfig("college", "Chengdu")
    lists = test.Str2List(college_List, ",")
    for i in lists:
        print i
