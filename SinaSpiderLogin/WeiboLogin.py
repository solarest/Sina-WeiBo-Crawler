# -*-coding:utf8-*-

import cookielib
import urllib
import urllib2


from SinaSpiderUtil.WeiboUtil import WeiboUtil

class WeiboLogin():

    def __init__(self):
        Util = WeiboUtil()
        self.myEmail = Util.ReadConfig("weibo_account", "Email")
        self.myPassword = Util.ReadConfig("weibo_account", "Password")

    def SinaWeibo_GetCookies(self):
        sso_url = "https://passport.weibo.cn/sso/login"
        login_data = urllib.urlencode([
            ('username', self.myEmail),
            ('password', self.myPassword),
            ('entry', 'mweibo'),
            ('client_id', ''),
            ('savestate', '1'),
            ('ec', ''),
        ])

        req = urllib2.Request(sso_url)
        req.add_header('Origin', 'https://passport.weibo.cn')
        req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
        req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
        weibo_cookies = cookielib.CookieJar()

        handler = urllib2.HTTPCookieProcessor(weibo_cookies)
        opener = urllib2.build_opener(handler)
        opener.open(req, data=login_data)
        for item in weibo_cookies:
            print item.name+"="+item.value
        return weibo_cookies

if __name__ == '__main__':
    test = WeiboLogin()
    myCookies = test.SinaWeibo_GetCookies()

