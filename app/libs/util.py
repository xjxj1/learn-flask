# -*- coding: utf-8 -*-
# @Time    : 2019-11-06 15:33
# @Author  : wxl
# @Site    : 
# @File    : util.py
# @Software: PyCharm

def is_isbn_or_key(word):
    '''
    
    :param word: 
    :return: 
    '''
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'

    short_word = word.replace('-', '')
    if '-' in short_word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'key'
        
    return isbn_or_key