# -*- coding: utf-8 -*-

import time
from flask import Flask, request, Response
import simplejson
from public.classify import Classify
from pymongo import MongoClient
import random
import jieba

app = Flask(__name__)
mongodb_host = '47.88.1.153'
# mongodb_host = '127.0.0.1'
key_word = []


@app.route('/')
def hello_world():
    print('hello world!')
    return 'hello world!'


@app.route('/geturls')
def get_urls():
    ret = {
        'code': 1002,
        'status': 'error',
        'data': {}
    }
    type = request.args.get('type')
    classify = request.args.get('from')
    need = request.args.get('need')
    if type != None and classify != None and need != None:
        classifys = Classify.get_classify()
        classifys_other = Classify.get_classify_other()
        if (type in ('inside', 'outside')) and ((classify in classifys) or (classify in classifys_other)):
            try:
                need = int(need)
            except:
                pass
            need_search = int(round(need * 0.7))
            need_detail = int(round(need * 0.2))
            need_list = int(round(need * 0.1))
            need_deal = need_detail + need_search + need_list
            if need_deal > need:
                need_search = need_search - (need_deal - need)
            data = {}
            clean_key_word()
            data['detail'] = get_detail(type, classify, need_detail, classifys, classifys_other)
            data['list'] = get_list(type, classify, need_list, classifys, classifys_other)
            # data['search'] = get_search_old(type, classify, need_search, classifys)
            data['search'] = get_search_new(type, classify, need_search, classifys, classifys_other)

            ret = {
                'code': 1001,
                'status': 'success',
                'data': data
            }
    resp = Response(simplejson.dumps(ret))
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


def get_search_new(type, classify, need_search, classifys, classifys_other):
    ret = []
    conn = MongoClient('mongodb://root:kongquewangchao@47.88.1.153:27017/')
    db = conn.url_pool

    # 获取普通关键词
    index_id = int(time.strftime('%Y%m%d'))
    while True:
        keywords = db.keyword.find_one({"_id": str(index_id)})
        if keywords != None:
            break
        index_id = index_id - 1
    need_words = random.sample(keywords['keyword'], need_search)
    # 获取电影关键词
    count = db.keyword_movie.count()
    need_movie_words = []
    if count == 0:
        need_movie_words = need_words
    else:
        res = db.keyword_movie.find().limit(need_search * 2).skip(random.randint(0, count - need_search * 2))
        for r in res:
            need_movie_words.append(r)

    classifys = dict(classifys.items() + classifys_other.items())
    print classifys
    if type == 'inside':
        if classifys[classify]['name'] not in (
                'bttiantang', 'kansogou', 'loldytt', 'm1905', 'ygdy8', 'magetweb', 'macatch', 'btstar', 'btmart',
                'btyaya', '7kz'):
            for need_word in need_words:
                url = classifys[classify]['search']
                ret.append({'url': url % need_word, 'title': need_word})
        else:
            for need_movie_word in need_movie_words:
                if len(ret) == need_search:
                    break
                other = random.sample(
                        [u' 迅雷下载', u' 在线观看', u' 电影', u' 电影完整版', u' 下载', u' 免费观看', u' 磁力链接', u' magnet', u' 电影天堂',
                         u' 在线播放', u' 字幕', u' 种子', u' 高清下载', u' 网盘', u' 中文字幕下载'], 1)[0]
                url = classifys[classify]['search']
                ret.append({'url': url % need_movie_word['keyword'], 'title': need_movie_word['keyword'] + other})
    else:
        classifys_deal = classifys.copy()
        classifys_deal.pop(classify)

        for need_word in need_words:
            one = classifys_deal.keys()[random.randint(0, len(classifys_deal) - 1)]
            url = classifys_deal[one]['search']
            other = ''
            if classifys_deal[one]['name'] in (
                    'bttiantang', 'kansogou', 'loldytt', 'm1905', 'ygdy8', 'magetweb', 'macatch', 'btstar', 'btmart',
                    'btyaya', '7kz'):
                need_word = random.sample(need_movie_words, 1)[0]['keyword']
                other = random.sample(
                        [u' 迅雷下载', u' 在线观看', u' 电影', u' 电影完整版', u' 下载', u' 免费观看', u' 磁力链接', u' magnet', u' 电影天堂',
                         u' 在线播放', u' 字幕', u' 种子', u' 高清下载', u' 网盘', u' 中文字幕下载'], 1)[0]
            ret.append({'url': url % need_word, 'title': need_word + other})
    print(ret)
    return ret


def get_search_old(type, classify, need_detail, classifys):
    ret = []
    if type == 'inside':
        for k in key_word:
            if need_detail <= 0:
                break
            url = classifys[classify]['search']
            ret.append({'url': url % k, 'title': k})
            need_detail = need_detail - 1
    else:
        classifys_deal = classifys.copy()
        classifys_deal.pop(classify)
        for k in key_word:
            if need_detail <= 0:
                break
            one = classifys_deal.keys()[random.randint(0, len(classifys_deal) - 1)]
            url = classifys_deal[one]['search']
            ret.append({'url': url % k, 'title': k})
            need_detail = need_detail - 1
    return ret


def get_detail(type, classify, need_detail, classifys, classifys_other):
    ret = []
    # conn = MongoClient(mongodb_host, 27017)
    conn = MongoClient('mongodb://root:kongquewangchao@47.88.1.153:27017/')
    db = conn.url_pool
    if type == 'inside':
        if classify in classifys:
            table_name = classifys[classify]['name']
            print(table_name)
            count = db[table_name].count()
            print(count)
            end_count = count - need_detail
            if end_count <= 0:
                end_count = count - 1
            res = db[table_name].find().limit(need_detail).skip(random.randint(0, end_count))
            for r in res:
                ret.append(r)
                # get_key_word(r['title'])
    else:
        classifys_deal = classifys.copy()
        if classify in classifys:
            classifys_deal.pop(classify)
        while True:
            if need_detail <= 0:
                break
            classifys_count = len(classifys_deal)
            one = classifys_deal.keys()[random.randint(0, classifys_count - 1)]
            table_name = classifys_deal[one]['db_name']
            count = db[table_name].count()
            if count == 0:
                continue
            res = db[table_name].find().limit(1).skip(random.randint(0, count - 1))
            for r in res:
                ret.append(r)
                # get_key_word(r['title'])
            need_detail = need_detail - 1
    return ret


def get_list(type, classify, need_list, classifys, classifys_other):
    print(classifys)
    ret = []
    # conn = MongoClient(mongodb_host, 27017)
    conn = MongoClient('mongodb://root:kongquewangchao@47.88.1.153:27017/')
    db = conn.url_pool
    if type == 'inside':
        if classify in classifys:
            table_name = classifys[classify]['name']
            count = db[table_name + '_list'].count()
            end_count = count - need_list
            if end_count <= 0:
                end_count = count - 1
            res = db[table_name + '_list'].find().limit(need_list).skip(random.randint(0, end_count))
            for r in res:
                ret.append(r)
    else:
        classifys_deal = classifys.copy()
        if classify in classifys:
            classifys_deal.pop(classify)
        while True:
            if need_list <= 0:
                break
            classifys_count = len(classifys_deal)
            one = classifys_deal.keys()[random.randint(0, classifys_count - 1)]
            table_name = classifys_deal[one]['db_name']
            count = db[table_name + '_list'].count()
            if count == 0:
                continue
            res = db[table_name + '_list'].find().limit(1).skip(random.randint(0, count - 1))
            for r in res:
                ret.append(r)
            need_list = need_list - 1
    return ret


def get_key_word(title):
    seg_list = jieba.cut(title)
    for s in seg_list:
        if len(s) >= 2:
            key_word.append(s)
    return key_word


# 此处有坑,关于python清空数组
def clean_key_word():
    del key_word[:]


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=3722, use_reloader=True, threaded=True)
