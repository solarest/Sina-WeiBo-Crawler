# -*-coding:utf8-*-
from bs4 import BeautifulSoup



class WeiboParseBase():

    def get_soup_obj(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        return soup

    def soup_parse(self):
        pass



