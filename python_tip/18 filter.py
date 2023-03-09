# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-21/, https://kibua20.tistory.com/194
□ 기능 : filter
□ 목적 : filter 기능 정리
"""
#%%
f = lambda x: x > 0
print(list(filter(f, range(-5, 5))))
#%%
def func(x):
    if x > 0:
        return x
    else:
        return x - 100

print(list(filter(func, range(-5, 5))))
