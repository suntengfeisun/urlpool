# -*- coding: utf-8 -*-

from pymongo import MongoClient
import time
from pymongo import MongoClient
from public.classify import Classify
from pymongo import MongoClient
import random


# conn = MongoClient("47.88.1.153", 27017)
#
# db = conn.test
#
# data = {'id': 1, 'name': 'kaka', 'sex': 'male'}
# db.aaa.save(data)
# bbb = db.aaa.find({'id': 1})
#
# for b in bbb:
#     print(b)


# import random

# table_name = 'kansogou'
# conn = MongoClient("47.88.1.153", 27017)
# db = conn.url_pool
# need_detail = 10
# count = 1000
# res = db[table_name].find().limit(need_detail).skip(random.randint(1, count))
#
# for r in res:
#     print(r)


# print random.randint(0, 1)
#
# from pymongo import MongoClient
# import time
# import simplejson
#
#
# word={'_id':0,'keyword':[u'刘德华']}
# conn = MongoClient('mongodb://root:kongquewangchao@47.88.1.153:27017/')
# db = conn.url_pool
# db['keyword_'+time.strftime('%Y%m%d')].save(word)
# bbb =[]
# aaa = [u'\n                    \u793e\u4f1a\n                ']
# aaa.append(aaa[0].replace('\n',''))
# print aaa

# import time
# from pymongo import MongoClient
#
# conn = MongoClient('mongodb://root:kongquewangchao@47.88.1.153:27017/')
# db = conn.url_pool
# keywords = db.keyword.find_one({"_id" : time.strftime('%Y%m%d')},{'_id':0,'keyword':1})
# # print(keywords)
#
#
# bbb = random.sample(aaa['keyword'], 10)
#
# print bbb


# conn = MongoClient('mongodb://root:kongquewangchao@47.88.1.153:27017/')
# db = conn.url_pool
# keywords = db.keyword.find_one({"_id" : '20160824'})
# print(int(time.strftime('%Y%m%d'))-1)


# aaa = 'aaa1'
# dict1 = {'aaa':111,'bbb':222}
# dict2 = {'ccc':111,'ddd':222}
# print dict(dict1.items()+dict2.items())

# import random
# need_movie_words= ('bttiantang','kansogou','loldytt','m1905','ygdy8')
# print random.sample(need_movie_words, 1)

print random.sample(
                        [u'迅雷下载', u'在线观看', u'电影', u'电影完整版', u'下载', u'免费观看', u'磁力链接', u'magnet', u'电影天堂', u'在线播放', u'字幕',
                         u'种子', u'高清下载', u'网盘', u'中文字幕下载'], 1)