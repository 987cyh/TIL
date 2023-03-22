# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-45/
□ 기능 : Dispatch
□ 목적 : Dispatch 기능 정리 및 복습
"""
#%%
# Overloading
from multipledispatch import dispatch

@dispatch(int, int)
def add(x, y):
    return x + y

@dispatch(str, int)
def add(x, y):
    return f"{x} = {y}"

print(add(10, 90000))
print(add("f(x)", 5515151))
print(add("a", 5515151))
#%%
