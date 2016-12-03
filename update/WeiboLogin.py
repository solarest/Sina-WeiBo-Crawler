# -*- coding:utf8 -*-

import WeiboUtils
import requests



class WeiboLogin:

    def __init__(self, ini_path):
        self.my_email = WeiboUtils.read_config(ini_path, "account", "Email")
        self.my_password = WeiboUtils.read_config(ini_path, "account", "Password")

    def cookies_fetcher(self):
        use_session = requests.session()
        login_url = "https://passport.weibo.cn/sso/login"
        login_data = {
            'username': self.my_email,
            'password': self.my_password,
            'entry': 'mweibo',
            'client_id': '',
            'savestate': '1',
            'ec': '',
        }

        login_headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2',
            'Connection': 'keep-alive',
            'Content-Length': '106',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) '
                          'AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25',
            'Host': 'passport.weibo.cn',
            'Origin': 'https://passport.weibo.cn',
            'Referer': 'https://passport.weibo.cn/signin/login'
        }

        use_session.post(login_url, headers=login_headers, data=login_data)
        return use_session


if __name__ == '__main__':
    login = WeiboLogin("account.ini")
    print login.cookies_fetcher()



