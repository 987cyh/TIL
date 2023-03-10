# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-23/
□ 기능 : map
□ 목적 : map 기능 정리
"""
#%%
f = lambda x: x > 0
g = lambda x: x ** 2

print(list(map(f, range(-5, 5))))
print(list(map(g, range(5))))
#%%
# 데이터 형식 변경 ★
data = [-10.8, 52.5, 875.4, 85.4, 15.4]

f = map(int, data)

print(list(f))
#%%
def calc(x):
    return (x / 2) + 1

data = [-10.8, 52.5, 875.4, 85.4, 15.4]

f = map(calc, data)

print(list(f))
#%%
