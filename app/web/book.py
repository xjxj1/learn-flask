# -*- coding: utf-8 -*-
# @Time    : 2019-11-07 15:18
# @Author  : wxl
# @Site    : 
# @File    : book.py
# @Software: PyCharm
from flask import jsonify
# 循环引用
# from test import app
from flask import Blueprint
from util import is_isbn_or_key
from yushu import YuShuBook

web = Blueprint('web', __name__)

@web.route('/book/search/<q>/<page>')
def search(q, page):
    '''

    :param q: 普通关键字 isbn
    :param page:
    :return:

    isbn13 --> 13个0到9的数字组成
    isbn10 --> 10个0到9的数字组成，含有一些 '-'
    '''
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    # dict 序列化
    return jsonify(result)
    # return json.dumps(result), 200, {'content-type': 'application/json'}
