# -*- coding: utf-8 -*-

class Classify:
    @staticmethod
    def get_classify():
        classify = {
            'wen': {
                'name': 'weixin',
                'db_name': 'weixin_dev',
                'db_table': 'zmt_weixin_content',
                'db_cate_table': 'zmt_weixin_category',
                'db_host': '47.88.1.153',
                'db_port': 3306,
                'detail': 'http://www.yyrewen.com/detail/%s.html',
                'list': 'http://www.yyrewen.com/%s.html',
                'search': 'http://www.yyrewen.com/s/%s'
            },
            'too': {
                'name': 'toutiao',
                'db_name': 'zmt_dev',
                'db_table': 'zmt_content',
                'db_cate_table': 'zmt_category',
                'db_host': '47.88.1.153',
                'db_port': 3306,
                'detail': 'http://www.yredian.com/detail/%s.html',
                'list': 'http://www.yredian.com/%s.html',
                'search': 'http://www.yredian.com/s/%s'
            },
            'btg': {
                'name': 'bttiantang',
                'db_name': 'bttiantang',
                'db_table': 'bttiantang_content',
                'db_cate_table': 'bttiantang_category',
                'db_host': '47.88.1.153',
                'db_port': 3307,
                'detail': 'http://www.yourtub.net/dy/%s',
                'list': 'http://www.yourtub.net/fl/%s',
                'search': 'http://www.yourtub.net/s/%s'
            },
            'kau': {
                'name': 'kansogou',
                'db_name': 'kansogou',
                'db_table': 'kansogou_content',
                'db_cate_table': 'kansogou_category',
                'db_host': '47.88.1.153',
                'db_port': 3307,
                'detail': 'http://www.aiy.pub/m/%s',
                'list': 'http://www.aiy.pub/lb/%s',
                'search': 'http://www.aiy.pub/s/%s'
            },
            'lot': {
                'name': 'loldytt',
                'db_name': 'loldytt',
                'db_table': 'loldytt_content',
                'db_cate_table': 'loldytt_category',
                'db_host': '47.88.1.153',
                'db_port': 3307,
                'detail': 'http://www.yunbeicang.com/movie/%s',
                'list': 'http://www.yunbeicang.com/cate/%s',
                'search': 'http://www.yunbeicang.com/s/%s'
            },
            'm15': {
                'name': 'm1905',
                'db_name': 'm1905',
                'db_table': 'm1905_content',
                'db_cate_table': 'm1905_category',
                'db_host': '47.88.1.153',
                'db_port': 3307,
                'detail': 'http://www.ixy.pub/film/%s',
                'list': 'http://www.ixy.pub/fc/%s',
                'search': 'http://www.ixy.pub/s/%s'
            },
            'yg8': {
                'name': 'ygdy8',
                'db_name': 'ygdy8',
                'db_table': 'ygdy8_content',
                'db_cate_table': 'ygdy8_category',
                'db_host': '47.88.1.153',
                'db_port': 3307,
                'detail': 'http://www.ccu.pub/movies/%s',
                'list': 'http://www.ccu.pub/category/%s',
                'search': 'http://www.ccu.pub/s/%s'
            }
        }
        return classify

    @staticmethod
    def get_classify_other():
        classify = {
            'magetweb': {
                'name': 'magetweb',
                'search': 'http://www.magetweb.com/s/%s'
            },
            'macatch': {
                'name': 'macatch',
                'search': 'http://www.macatch.com/s/%s'
            },
            'btstar': {
                'name': 'btstar',
                'search': 'http://www.btstar.org/s/%s'
            },
            'btmart': {
                'name': 'btmart',
                'search': 'http://www.btmart.net/s/%s'
            },
            'btyaya': {
                'name': 'btyaya',
                'search': 'http://www.btyaya.com/s/%s/'
            },
            '7kz': {
                'name': '7kz',
                'search': 'http://www.7kz.club/s/%s/'
            }
        }
        return classify
