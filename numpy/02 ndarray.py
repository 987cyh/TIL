# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-numpy-2/, https://datascienceschool.net/
□ 기능: np.array
□ 목적: np.array 복습(배열 생성)
"""
#%%
# package
import numpy as np
#%%
# 1차원 배열
a = np.array([113, 252, 933], dtype=int)
b = np.array([991.91, 332.9992, 123.2153], dtype=float)
c = np.array([1, 1, 0], dtype=bool)

print(a)
print(b)
print(c)
print(a.dtype)
#%%
# 다차원 배열
a = np.array([[10, 20, 30], [40, 55, 66], [77, 88, 99]])                          # 2차원
b = np.array([[[10, 20], [30, 40]], [[55, 66], [77, 88]], [[9, 10], [11, 12]]])   # 3차원

print(a)
print(b)
print(a[0][1])
print(b[0][1][1])
#%%
# 배열의 속성(값) 반환(인덱싱)
a = np.array([[10, 20, 30], [40, 55, 66], [77, 88, 99]])                          # 2차원
b = np.array([[[10, 20], [30, 40]], [[55, 66], [77, 88]], [[9, 10], [11, 12]]])   # 3차원

print(a.ndim)   # 배열의 차원
print(a.shape)  # 배열의 모양(형태)
print(a.dtype)  # 배열의 자료형

print(np.ndim(b))
print(np.shape(b))
print(b.dtype)
#%%
