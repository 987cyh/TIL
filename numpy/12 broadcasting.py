# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-numpy-12/, https://datascienceschool.net/
□ 기능: broadcasting(브로드캐스팅) 기능
□ 목적: broadcasting(브로드캐스팅) 기능 학습
"""
#%%
# package
import numpy as np
#%%
array1 = np.array([1, 2, 3, 4]).reshape(2, 2)
array2 = np.array([1.5, 2.5])

add = array1 + array2

print(add)
#%%