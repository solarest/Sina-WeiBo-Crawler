# -*- coding:utf8 -*-

from snownlp import SnowNLP
import jieba
from textblob import TextBlob


class WeiboAnalysis():

    def __init__(self):
        pass

    def mytokenizer(self, text):
        seg_list = jieba.cut(text, cut_all=True)
        result = " ".join(seg_list)
        return result

    def weibo_Sentiment(self, text):
        s = SnowNLP(text)
        sentiment_point = s.sentiments
        return sentiment_point

    def weibo_Sentiment_blob(self, text):
        blob = TextBlob(text)
        blob.noun_phrases


if __name__ == '__main__':
    test = WeiboAnalysis()
    # print test.mytokenizer(u"你们不要总想搞个大新闻")
    print test.weibo_Sentiment(u'今天天气真不错，好开心！！！')
