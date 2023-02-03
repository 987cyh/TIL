# -*- coding: utf-8 -*-
"""
□ 참고 : https://rfriend.tistory.com/743
□ 기능: 변수 간의 거리 구하기

"""
#%%
from scipy.spatial import distance
import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    # x, y
    [3, 2], # ID 1
    [3, 3], # ID 2
    [5, 5], # ID 3
    [6, 7], # ID 4
])

plt.plot(X[:, 0], X[:, 1], 'o')
plt.show()
#%%
# pdist
X_pdist = distance.pdist(X, metric='euclidean')
X_pdist

# cdist
X_cdist = distance.cdist(X, X, metric='euclidean')
X_cdist

# Manhattan Distance
X_cdist_cityblock = distance.cdist(X, X, metric='cityblock')
X_cdist_cityblock
#%%
