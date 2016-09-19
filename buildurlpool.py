# -*- coding: utf-8 -*-

import MySQLdb
from public.classify import Classify
from pymongo import MongoClient
from DBUtils.PooledDB import PooledDB


def init_mysql():
    pool = PooledDB(MySQLdb, 5, host=classify['db_host'], user='test',
                    passwd='kongquewangchao', db=classify['db_name'], port=classify['db_port'],
                    charset='utf8')
    mysql_conn = pool.connection()
    return mysql_conn


def save_all(classify):
    mysql_conn = init_mysql()
    sql = 'select count(*) from %s' % classify['db_table']
    try:
        mysql_conn.ping()
    except:
        mysql_conn = init_mysql()
    cur = mysql_conn.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    if len(res) > 0:
        if len(res[0]) > 0:
            num = 1000
            content_count = res[0][0]
            page_count = content_count / num
            if content_count % num > 0:
                page_count += 1
            for one in xrange(page_count):
                if classify['name'] in ('kansogou', 'loldytt', 'm1905', 'weixin', 'toutiao'):
                    sql = 'select `id`,`title` from %s limit %s,%s' % (classify['db_table'], one * num, num)
                if classify['name'] in ('bttiantang',):
                    sql = 'select `id`,`names_chn` from %s limit %s,%s' % (classify['db_table'], one * num, num)
                if classify['name'] in ('ygdy8',):
                    sql = 'select `id`,`name` from %s limit %s,%s' % (classify['db_table'], one * num, num)
                print(sql)
                try:
                    mysql_conn.ping()
                except:
                    mysql_conn = init_mysql()
                cur = mysql_conn.cursor()
                cur.execute(sql)
                res = cur.fetchall()
                cur.close()
                if len(res) > 0:
                    # conn = MongoClient("47.88.1.153", 27017)
                    conn = MongoClient('mongodb://root:kongquewangchao@47.88.1.153:27017/')
                    db = conn.url_pool
                    # db.api.authenticate(u'root',u'kongquewangchao')
                    for two in res:
                        data = {}
                        id = two[0]
                        data['_id'] = id
                        data['title'] = two[1]
                        data['url'] = classify['detail'] % id
                        db[classify['name']].save(data)
                        print(data)
    # save_list(classify, mysql_conn)
    mysql_conn.close()


def save_list(classify, mysql_conn):
    if classify['name'] in ('kansogou', 'm1905', 'bttiantang'):
        sql = 'select `id`,`category` from %s' % (classify['db_cate_table'])
    if classify['name'] in ('loldytt', 'ygdy8'):
        sql = 'select `id`,`name` from %s' % (classify['db_cate_table'])
    if classify['name'] in ('weixin', 'toutiao'):
        sql = 'select `id`,`url_name` from %s' % (classify['db_cate_table'])
    print(sql)
    try:
        mysql_conn.ping()
    except:
        mysql_conn = init_mysql()
    cur = mysql_conn.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    if len(res) > 0:
        for three in res:
            data = {}
            data['_id'] = three[0]
            data['title'] = three[1]
            data['url'] = classify['list'] % three[1]
            # conn = MongoClient("47.88.1.153", 27017)
            conn = MongoClient('mongodb://root:kongquewangchao@47.88.1.153:27017/')
            db = conn.url_pool
            db[classify['name'] + '_list'].save(data)


if __name__ == '__main__':
    classifys = Classify.get_classify()
    for classify_code in classifys:
        classify = classifys[classify_code]
        print(classify)
        save_all(classify)
