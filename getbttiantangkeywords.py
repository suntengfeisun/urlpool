# -*- coding: utf-8 -*-

import time
import requests
from lxml import etree
from public.headers import Headers
from pymongo import MongoClient
from public.mysqlpooldao import MysqlDao


def get_keywords():
    mysql_dao = MysqlDao()
    sql = 'select `names_chn`,`names_eng`,`names_nick`,`directors`,`writers`,`casts`FROM bttiantang_content'
    res = mysql_dao.execute(sql)
    return res


def save_keywords(words):
    n = 1
    for word in words:
        for w in word:
            ww = []
            if ',' in w:
                w_list = w.split(',')
                for w_l in w_list:
                    ww.append(w_l)
            else:
                ww.append(w)
            print(ww)
            for one in ww:
                one.replace(' ', '')
                if one != '':
                    conn = MongoClient('mongodb://root:kongquewangchao@47.88.1.153:27017/')
                    db = conn.url_pool
                    db['keyword_movie'].save({'_id': n, 'keyword': one})
                    n = n + 1


if __name__ == '__main__':
    print('start:' + time.strftime('%Y-%m-%d %H:%M:%S'))
    words = get_keywords()
    save_keywords(words)
