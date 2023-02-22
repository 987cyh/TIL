# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-numpy-4/, https://datascienceschool.net/
□ 기능: np.array
□ 목적: 등간격의 ndarray
"""
#%%
# package
import numpy as np
#%%
# arange
a = np.arange(0, 20, step=5)
b = np.arange(1, 30, step=5)
c = np.arange(0, 15, step=1)

print(a)
print(b)
print(c)
#%%
# linspace
a = np.linspace(0, 20, num=5, endpoint=True, retstep=True)
b = np.linspace(1, 30, num=5, endpoint=True, retstep=False)
c = np.linspace(0, 15, num=5, endpoint=False, retstep=False)

print(a)
print(b)
print(c)
#%%
# logspace
a = np.logspace(0, 20, num=5, endpoint=True, base=10.0)
b = np.logspace(1, 30, num=5, endpoint=True, base=5.0)
c = np.logspace(0, 15, num=5, endpoint=False, base=1.0)

print(a)
print(b)
print(c)
#%%
# ndarray to list
z = np.arange(0, 20, step=5)

print(list(z))
print(z.tolist())
#%%
