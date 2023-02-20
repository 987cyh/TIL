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
# ones
a = np.ones((2,2), dtype=int)
b = [100, 200, 300, 400, 500]
c = np.ones_like(b, dtype=int)

print(a)
print(b)
print(c)
#%%
# zeros
a = np.zeros((2,2), dtype=int)
b = [100, 200, 300, 400, 500]
c = np.zeros_like(b, dtype=int)

print(a)
print(b)
print(c)
#%%
# empty
a = np.empty((2,2), dtype=int)
b = [100, 200, 300, 400, 500]
c = np.empty_like(b, dtype=int)

print(a)
print(b)
print(c)
#%%
# 대각행렬
a = np.identity(4, dtype=int)
b = np.eye(4, 4, k=1, dtype=int)
c = np.eye(4, 4, k=-1, dtype=int)

print(a)
print(b)
print(c)
#%%
