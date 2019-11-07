# -*- coding: utf-8 -*-
# @Time    : 2019-11-07 16:39
# @Author  : wxl
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm
from flask import Flask


def create_app():
    app = Flask(__name__)
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)