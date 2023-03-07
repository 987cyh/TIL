# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-numpy-15/, https://datascienceschool.net/
□ 기능: append
□ 목적: append 복습(데이터 전처리에서 조건문으로 많이 활용하였음)
"""
#%%
# package
import numpy as np
#%%
import numpy as np

array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

whereDefault = np.where(array > 5)
whereArray = np.where(array > 5, np.max(array), array) # np.where(조건식, 참 값, 거짓 값)

whereAnd = np.where((array > 3) & (array < 7), 0, array)
whereOr = np.where((array < 3) | (array > 7), 0, array)

whereSum = np.where((np.sum(array, axis = 1) > 10).reshape(3, -1), array, 0)
whereSumOdd = np.where((np.sum(array, axis = 1) > 10).reshape(3, -1), np.where( array % 2 == 1, array, 0), 0)

print(array)
print(whereDefault)
print(array[whereDefault])
print(whereArray)

print(whereAnd)
print(whereOr)

print(whereSum)
print(whereSumOdd)
#%%