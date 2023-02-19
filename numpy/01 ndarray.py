# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-numpy-1/, https://datascienceschool.net/
□ 기능: np.array
□ 목적: np.array 복습
"""
#%%
# package
import numpy as np
#%%
# 배열 생성
a = [19, 28, 37, 46, 54]
b = np.array(a)
c = np.array([15, 33, 51])

print(a)
print(b)
print(c)
#%%
# 배열 복제
a = np.array([17, 42, 43, 84, 35])
b = a
c = a.copy()

b[0] = 99999

print(a)
print(b)
print(c)
#%%
# 배열 호출(슬라이싱)
a = [1, 2, 3, 4, 5]
b = np.array(a)
c = np.array([1, 3, 5])

print(b[2])
print(c[-1])
print(c[0:2])
#%%
# 배열 연산
a = [1, 2, 3, 4, 5]
b = np.array(a)
c = np.array([1, 3, 5])

print(a*2)
print(b*2)
print(c+3)
#%%
