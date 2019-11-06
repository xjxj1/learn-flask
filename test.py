#

# @app.route("/")
# def index():
#     return '<h1> hello flask! </h1>'
#
# # 多路由地址绑定到同一个视图函数
# @app.route("/hi")
# @app.route("/hello")
# def say_hello():
#     return '<h1> hello flask!!!!!!! </h1>'
#
# # 动态URL
# @app.route("/greet",defaults={
#     'name': 'programmer'
# })
# @app.route("/greet/<name>")
# def greet(name):
#     return '<h1> hello %s </h1>' % name

# @app.route("/hello")
# def hello():
#     name = request.args.get('name', 'flask')
#     return '<h1> hello %s </h1>' % name
#
#
# @app.route("/goback/<int:year>")
# def goback(year):
#     return '<h1> welcome to  %s </h1>' % (2019 - year)
#
# @app.route("/color_choice/<any(red,blue,yellow):color>")
# def color_choice(color):
#     return "<h1>your favourite color is %s </h1>" % color

# @app.route('/watchlist')
# def watchlist():
#     return render_template('watchlist.html', user=user, movies=movies)


# @app.route('/hi')
# @app.route('/hello')
# def say_hello():
#     return '<h1> hello flask!!!!!!</h1>'
import json

from flask import Flask, render_template, jsonify
from flask import make_response
from util import is_isbn_or_key
from yushu import YuShuBook

app = Flask(__name__)


user = {
    'username': 'Grey Li',
    'bio': 'A boy who loves movies and music.',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]



@app.route('/watchlist')
def index():
    return render_template('test.html', user=user, movies=movies)


# @app.route('/hello')
# def hello():
#     # 探讨flask视图函数的返回
#
#
#     headers = {
#         'content-type': 'text/plain',
#         'location': 'http://www.baidu.com'
#
#     }
#     # response = make_response('<html></html>', 301)
#     # response.headers = headers
#     #
#     # return response
#     # 常用的方式
#     return '<html></html>', 301, headers

# app.add_url_rule('/hello', view_func=hello)

# 获取URL参数方式1
# 调用外部API
@app.route('/book/search/<q>/<page>')
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

