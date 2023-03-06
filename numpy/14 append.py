# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-numpy-14/, https://datascienceschool.net/
□ 기능: append
□ 목적: append 학습
"""
#%%
# package
import numpy as np
#%%
arr = np.array([
    [[1, 1],
     [2, 2]],
    [[3, 3],
     [4, 4]]
])
item = np.array([
    [5, 5],
    [6, 6]
])
print(arr.shape)
print(item.shape)
#%%
item_re = item.reshape(1, 2, 2)
print(item_re.shape)
print(arr.shape)

append = np.append(arr, item_re, axis=0) # 결과 = np.append(배열1, 배열2, 축)
print(append)
print(append.shape)
#%%
item_re1 = item.reshape(2, 2, 1)
print(item_re1.shape)
print(arr.shape)

append1= np.append(arr, item_re1, axis=-1) # 결과 = np.append(배열1, 배열2, 축) / axis=2
print(append1)
print(append.shape)
#%%
arr1 = np.empty((1, 2), dtype=int)

for i in range(5):
    item2 = np.array([[i, i]])
    arr1 = np.append(arr1, item2, axis=0)

arr1 = np.delete(arr1, [0, 0], axis=0)
print(arr1)
#%%