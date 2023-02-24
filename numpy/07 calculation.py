# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-numpy-7/, https://datascienceschool.net/
□ 기능: 연산 기능
□ 목적: ★★★ 연산 기능 복습, 추가적인 실습 및 연구가 필요함 ★★★
"""
#%%
# package
import numpy as np
#%%
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
b = np.ones(3, dtype = int)

print(a)
print(b)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
#%%
# 배열연산
print(np.cross(a, b)) # 벡터곱(cross product)
print(np.dot(a, b))   # 점곱(dot product)
#%%
# 심화연산
arr = np.array([-90, 0, np.radians(90)])

sin = np.sin(arr)
tanh = np.tanh(arr)
isclose = np.isclose(arr, -90)
gcd = np.gcd(arr.astype(int), 3)

print(sin)
print(tanh)
print(isclose)
print(gcd)
#%%
