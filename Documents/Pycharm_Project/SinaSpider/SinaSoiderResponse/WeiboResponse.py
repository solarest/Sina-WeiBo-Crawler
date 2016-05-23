# -*- coding:utf8 -*-
import requests
from SinaSpiderLogin.WeiboLogin import WeiboLogin


class WeiboResponse():

    def Weibo_GetCont(self, myCookies, target_url):
        weibo_cont = requests.get(target_url, cookies=myCookies).content
        return weibo_cont

    def Weibo_GetSearchResults(self, myCookies, college_name):
        search_param = {
            'keyword': college_name,
            'suser': '找人',
        }
        result_cont = requests.post("http://weibo.cn/search/", data=search_param, cookies=myCookies).content
        return result_cont

if __name__ == '__main__':
    WeiboLogin = WeiboLogin()
    WeiboResponse = WeiboResponse()
    myCookies = WeiboLogin.SinaWeibo_GetCookies()
    print WeiboResponse.Weibo_GetSearchResults(myCookies, "西华大学")
