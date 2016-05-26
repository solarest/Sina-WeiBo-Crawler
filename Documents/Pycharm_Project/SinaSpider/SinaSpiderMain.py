# -*-coding:utf8-*-


from SinaSpiderLogin.WeiboLogin import WeiboLogin
from SinaSpiderResponse.WeiboResponse import WeiboResponse
from SinaSpiderParse.WeiboContentParse import WeiboContentParse
from SinaSpiderUtil.WeiboUtil import WeiboUtil

login = WeiboLogin()
response = WeiboResponse()
parse = WeiboContentParse()
util = WeiboUtil()

mycookies = login.SinaWeibo_GetCookies()
uid_urls = []

colleges = util.ReadConfig("college", "Chengdu")
colleges_list = util.Str2List(colleges, ",")

for college in colleges_list:
    for index in range(1, 20):
        result_cont = response.Weibo_GetSearchResults(mycookies, college, index)
        uid_list = parse.weiboParse_Results(result_cont)
        util.Complete_uid_url(uid_list)
    print "已完成：",college
print uid_urls



