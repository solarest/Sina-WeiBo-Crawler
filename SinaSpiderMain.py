# -*-coding:utf8-*-
import sys
sys.setrecursionlimit(1000000)
import threading

from SinaSpiderLogin.WeiboLogin import WeiboLogin
from SinaSpiderResponse.WeiboResponse import WeiboResponse
from SinaSpiderParse.WeiboContentParse import WeiboContentParse
from SinaSpiderUtil.WeiboUtil import WeiboUtil
from SinaSpiderMangoDB.WeiboDB import WeiboDB

config_util = WeiboUtil()
colleges = WeiboUtil.ReadConfig("college", "Chengdu")
colleges_list = config_util.Str2List(colleges, ",")
myhost = WeiboUtil.ReadConfig("mangoDB", "host")
myport = int(WeiboUtil.ReadConfig("mangoDB", "port"))
weibo_connection = WeiboUtil.ReadConfig("mangoDB", "weibo_connection")
weibo_collection = WeiboUtil.ReadConfig("mangoDB", "weibo_collection")

weibo_login = WeiboLogin()
weibo_response = WeiboResponse()
content_parser = WeiboContentParse()
my_cookies = weibo_login.SinaWeibo_GetCookies()
weibo_db = WeiboDB(myhost,myport)
mongo_conn = weibo_db.db_connection(weibo_connection)


class weibo_get_thread(threading.Thread):
    def __init__(self, cookies, college):
        threading.Thread.__init__(self)
        self.college = college
        self.thread_stop = False
        self.mycookies = cookies

    def college_user_get(self, index):
        try:
            user_result_cont = weibo_response.Weibo_GetSearchResults(self.mycookies, self.college, index)
            return user_result_cont
        except:
            try:
                user_result_cont = weibo_response.Weibo_GetSearchResults(self.mycookies, self.college, index)
                return user_result_cont
            except:
                return None

    def user_uid_get(self, index, user_result_cont):
        uid_list = content_parser.weiboParse_Results(user_result_cont)
        if uid_list is None:
            print("bad Results.")
            user_result_cont = self.college_user_get(index)
            if user_result_cont is None:
                return None
            uid_list = content_parser.weiboParse_Results(user_result_cont)
            if uid_list is None:
                print("bad Results second.")
        return uid_list

    def weibo_response_get(self, url):
        try:
            html_content = weibo_response.Weibo_GetCont(self.mycookies, url)
            return html_content
        except:
            try:
                html_content = weibo_response.Weibo_GetCont(self.mycookies, url)
                return html_content
            except:
                return None

    def college_weibo_get_content(self):
        for index in range(1, 50):

            user_result_cont = self.college_user_get(index)
            if user_result_cont is None:
                continue

            uid_list = self.user_uid_get(index,user_result_cont)
            if uid_list is None:
                continue

            url_list = WeiboUtil.Complete_uid_url(uid_list)
            for url in url_list:
                html_content = self.weibo_response_get(url)
                if html_content is None:
                    continue
                weibo_contents = content_parser.weiboParse_text(html_content)
                if weibo_contents is not None and len(weibo_contents) is not 0:
                    weibo_db.db_insert(mongo_conn, weibo_collection, weibo_contents)
        print "已完成：", self.college
        self.stop()

    def run(self):
        while self.thread_stop is False:
            self.college_weibo_get_content()

    def stop(self):
        self.thread_stop = True


if __name__ == '__main__':
    weibo_thread_list = []
    for college in colleges_list:
        weibo_thread = weibo_get_thread(my_cookies, college)
        weibo_thread.start()
        weibo_thread_list.append(weibo_thread)




