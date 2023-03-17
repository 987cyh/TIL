# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-41/
□ 기능 : iterator
□ 목적 : iterator 기능 정리 및 복습
"""
#%%
# iterator
import numpy as np

_str = iter("1234")
_tuple = iter((1, 2, 3, 4))
_list = iter([1, 2, 3, 4])
_dict = iter({"a": 1, "b": 2, "c": 3, "d": 4})
_set = iter({1, 2, 3, 4})
_array = iter(np.array([[1, 2], [3, 4]]))

print(next(_list))
print(next(_list))
print(next(_list))
#%%
_dict = iter({"a": 1, "b": 2, "c": 3, "d": 4})

print(next(_dict))

for i in _dict:
    print(i)
#%%
# itertools 모듈
from itertools import count

infinite = count()

print(next(infinite))

for i in infinite:
    print(i)
#%%
