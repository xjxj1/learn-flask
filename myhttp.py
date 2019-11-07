# -*- coding: utf-8 -*-
# @Time    : 2019-11-06 16:23
# @Author  : wxl
# @Site    : 
# @File    : myhttp.py
# @Software: PyCharm

import requests

class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        '''
            一定要优化此类代码，思路有三
            1. 简单的if...else... 可以使用三元表达式
            2. 用非常规的判断来替代大部分的情况
            3. 逻辑重复的代码抽象成函数
        '''
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text