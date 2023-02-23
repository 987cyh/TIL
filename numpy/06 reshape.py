# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-numpy-6/, https://datascienceschool.net/
□ 기능: reshape
□ 목적: reshape 복습
"""
#%%
# package
import numpy as np
#%%
# 2차원
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]])

print(a)
print(np.shape(a))

print(np.shape(a)[0])
print(np.shape(a)[1])

a.shape = (6,2) # 배열.shape = (행, 열)
print(a)
#%%
# 3차원
b = np.array([[[1, 2, 3], [4, 5, 6]],
              [[7, 8, 9], [10, 11, 12]],
              [[13, 14, 15], [16, 17, 18]]])

print(b)
print(np.shape(b))

print(np.shape(b)[0])
print(np.shape(b)[1])
print(np.shape(b)[2])

b.shape = (2, 3, 3) # 배열.shape= (페이지, 행, 열)
print(b)
#%%
