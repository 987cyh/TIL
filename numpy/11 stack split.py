# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-numpy-10/, https://datascienceschool.net/
□ 기능: 배열 구조 변경(병합, 분할)
□ 목적: 배열 구조 변경 학습
"""
#%%
# package
import numpy as np
#%%
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.hstack([a, b])  # horizontal
d = np.vstack([a, b])  # vertical

print(a)
print(b)
print(c)
print(d)
#%%
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.dstack([a, b])
d = np.stack([a, b], axis=2)
print(a)
print(b)
print("--------")
print(c)
print(d)
#%%
aa = np.array([[1, 2], [3, 4]])
bb = np.tile(a,4)

print(aa)
print(bb)
#%%
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.c_[a, b]
d = np.r_[a, b]

print(a)
print(b)

print(c)
print(d)
#%%
array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

a = np.hsplit(array, 2)
b = np.hsplit(array, (1, 3))
c = np.vsplit(array, 2)

print(a)
print(b)
print(c)
#%%
a = np.split(array, 2, axis=0)
b = np.split(array, 2, axis=1)

print(a)
print(b)
#%%
array = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ],
    [
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
])

a = np.dsplit(array, 2)

print(a)
#%%
