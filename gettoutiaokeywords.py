# -*- coding: utf-8 -*-

import time
import requests
from lxml import etree
from public.headers import Headers
from pymongo import MongoClient


def get_urls():
    urls = ['/articles_news_society/']
    # 测试用
    # start_url = 'http://toutiao.com' + urls[0]
    start_url = 'http://toutiao.com' + urls.pop()
    headers = Headers.get_headers()
    req = requests.get(start_url, headers=headers, timeout=30)
    if req.status_code == 200:
        html = req.content
        selector = etree.HTML(html)
        urls_extend = selector.xpath('//a[@ga_event="feed_category"]/@href')
        urls.extend(urls_extend)
    return urls


def get_keywords(urls, words=[]):
    # 循环分类 社会 娱乐
    for url in urls:
        url = 'http://toutiao.com' + url
        headers = Headers.get_headers()
        req = requests.get(url, headers=headers, timeout=30)
        if req.status_code == 200:
            html = req.content
            selector = etree.HTML(html)
            words_url = selector.xpath('//ul[@class="comment-list clearfix"]/li/a/@href')
            words_extend = selector.xpath('//ul[@class="comment-list clearfix"]/li/a/text()')
            words.extend(words_extend)
            # 扩展 words
            words.extend(extend_words(words_url))
        print(len(words))
    return words


def extend_words(words_url):
    words = []
    for word_url in words_url:
        headers = Headers.get_headers()
        req = requests.get(word_url, headers=headers, timeout=30)
        if req.status_code == 200:
            html = req.content
            selector = etree.HTML(html)
            words_extend = selector.xpath('//ul[@class="comment-list clearfix"]/li/a/text()')
            words.extend(words_extend)
    return words


def save_keywords(words):
    clear_words = clean_words(words)
    conn = MongoClient('mongodb://root:kongquewangchao@47.88.1.153:27017/')
    db = conn.url_pool
    print(clear_words)
    db['keyword'].save({'_id':time.strftime('%Y%m%d'),'keyword':clear_words})


def clean_words(words):
    clear_words = []
    for word in words:
        clear_word = word.replace('\n', '').replace(' ', '')
        if clear_word != '':
            if clear_word not in clear_words:
                clear_words.append(clear_word)
    return clear_words


if __name__ == '__main__':
    print('start:'+time.strftime('%Y-%m-%d %H:%M:%S'))
    urls = get_urls()
    words = get_keywords(urls)
    save_keywords(words)
    print('game over:'+time.strftime('%Y-%m-%d %H:%M:%S'))
