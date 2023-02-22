# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-numpy-5/, https://datascienceschool.net/
□ 기능: 슬라이싱
□ 목적: 슬라이싱 복습
"""
#%%
# package
import numpy as np
#%%
# arange
a = np.arange(1, 6, step=1)

print(a)
print(a[3:])
print(a[1:-1])

print(a[0])
print(a[3])
print(a[0:3:2]) # 간격 : 2
print(a[::-1])  # 역순
#%%
# 2차원 데이터프레임
b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

print(b)
print(b[:, 1:])
print(b[0:1,0:2])

c = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]])

print(c)
print(c[::2, ::2])
#%%
