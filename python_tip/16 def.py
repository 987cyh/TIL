# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-20/, https://datascienceschool.net/
□ 기능 : def
□ 목적 : def 기능 정리
"""
#%%
def add(a, b):
    return a + b
def func(x, y, z):
    return x(y, z)

plus = add

print(plus(3, 4))
print(func(plus, 3, 4))
#%%
