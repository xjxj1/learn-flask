# -*- coding: utf-8 -*-
# @Time    : 2019-11-07 16:40
# @Author  : wxl
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm


'''
在一个大的功能里面，我们可以用一个蓝图来注册模块里面的所有路由
'''

from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
from app.web import user