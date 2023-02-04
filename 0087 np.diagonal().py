# -*- coding: utf-8 -*-
"""
□ 참고 : https://rfriend.tistory.com/742
□ 기능: 주대각성분

"""
#%%
from scipy.spatial import distance
import numpy as np
import matplotlib.pyplot as plt
#%%
# 주대각성분 산출: np.diagonal()
arr = np.arange(9).reshape(3, 3)

np.diagonal(arr)
arr.diagonal()
#%%
# Horizontal flip(수평)
np.fliplr(arr) # flip from left to right
np.fliplr(arr).diagonal()

# Vertical flip(수직)
np.flipud(arr) # flip from up to down
np.flipud(arr).diagonal()
#%%
# 주대각성분 채우기
np.fill_diagonal(arr, val=999)
#%%
# 0행렬 작성 후 원하는 원소로 대각행렬 만들기
arr2 = np.zeros([3, 3])
np.fill_diagonal(arr2, val=[1, 2, 3])
#%%
