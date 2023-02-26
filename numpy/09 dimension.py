# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-numpy-9/, https://datascienceschool.net/
        https://pybasall.tistory.com/129
□ 기능: 축의 개념(축의 추상화), 차원 축소 및 확장
□ 목적: 축의 개념(축의 추상화), 차원 축소 및 확장 학습 후 개념정리
"""
#%%
# package
import numpy as np
#%%
arr = np.array([1, 2, 3, 4])

# 축생성 : np.newaxis
print(arr)
print(arr[np.newaxis])
print(arr[:, np.newaxis])
#%%
arr = np.array([[1, 2],
                [3, 4]], dtype=int)
print(arr)

new_arr = arr[:, np.newaxis]
print(new_arr)
print(new_arr[1][0])
print(new_arr[1][0][1])
#%%
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

print(arr1[np.newaxis] * arr2)
print(arr1[:, np.newaxis] * arr2)
print("\n")
print(arr1[np.newaxis] + arr2)
print(arr1[:, np.newaxis] + arr2)
#%%
arr = np.array([[[1, 2],
                 [3, 4]],
                [[5, 6],
                 [7, 8]]])

expand_dims = np.reshape(arr, (1, 1, 2, 4))
reduction = np.reshape(arr, (4, -1))

print(arr)
print(expand_dims)
print(reduction)
#%%
