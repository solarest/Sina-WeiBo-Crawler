# -*- coding:utf8 -*-
from bs4 import BeautifulSoup
from SinaSpiderLogin.WeiboLogin import WeiboLogin
from SinaSoiderResponse.WeiboResponse import WeiboResponse
from SinaSpiderUtil.WeiboUtil import WeiboUtil

class WeiboContentParse():

    def weiboParse_Results(self, html_content):
        myUtil = WeiboUtil()
        _soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        _result = _soup.find_all("input", attrs={"name": "uidList"})
        uid_list = _result[0]['value']
        uid_list = myUtil.Str2List(uid_list, ",")
        return uid_list

    def weiboParse_text(self, html_content):
        myUtil = WeiboUtil()
        weibo_content = []

        _soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        _result = _soup.find_all("div", class_="c")
        for index in _result:
            weibo_dict = {}
            publish_text = index.find("span", class_="ctt")
            publish_time = index.find("span", class_="ct")

            if(publish_text != None and publish_time != None):
                publish_text = publish_text.get_text()
                print publish_text
                publish_time = publish_time.get_text()
                time_info = myUtil.Str2List(publish_time, " ")
                publish_date = myUtil.DateFormat(time_info[0])
                print publish_date
                weibo_dict["publish_text"] = publish_text
                weibo_dict["publish_date"] = publish_date
                weibo_content.append(weibo_dict)

        return weibo_content

if __name__ == '__main__':
    WeiboLogin = WeiboLogin()
    myCookies = WeiboLogin.SinaWeibo_GetCookies()

    WeiboResponse = WeiboResponse()
    test = WeiboContentParse()

    # html_content = WeiboResponse.Weibo_GetSearchResults(myCookies, "")
    # print test.weiboParse_searchResults(html_content)

    html_content = WeiboResponse.Weibo_GetCont(myCookies, "http://weibo.cn/1729488283")
    print test.weiboParse_text(html_content)
