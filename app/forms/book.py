# -*- coding: utf-8 -*-
# @Time    : 2019-11-08 09:50
# @Author  : wxl
# @Site    : 
# @File    : book.py
# @Software: PyCharm


from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange

class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)