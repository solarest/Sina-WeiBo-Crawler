# -*- coding:utf8 -*-
import json
import urllib
from WeiboLogin import WeiboLogin

weibo_login = WeiboLogin("account.ini")


class WeiboResponse:

    def __init__(self, param, limit_page):
        self.session = weibo_login.cookies_fetcher()
        self.param = param
        self.limit_page = limit_page
        self.content_list = list()

    def realtime_search_response(self):
        seed_url = 'http://m.weibo.cn/container/getIndex'
        index = 0

        param = {
            'cardid': 'weibo_page',
            'containerid': urllib.quote('100103q='+self.param),
            'weibo_type': 'filter_realtime',
            'title': urllib.quote('实时-'+self.param),
        }

        while index < self.limit_page:
            param['page'] = 1
            res = self.session.get(seed_url, params=param)
            items = json.loads(res.content)['cards']
            self.content_list.extend(items)
            index += 1

        for item in self.content_list:
            if ('itemid' in item) and (item['itemid'] == 'mblog'):
                groups = item['card_group']
                for group in groups:
                    print group['mblog']['text']


if __name__ == '__main__':
    weibo_res = WeiboResponse("中国股市", 10)
    weibo_res.realtime_search_response()
