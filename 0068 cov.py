# -*- coding: utf-8 -*-
"""
ㅁ 참고: https://wikidocs.net/156021
ㅁ 목적: 기초통계의 공분산 학습
"""
#%%
import pandas as pd
import numpy as np
#%%
col = ['X','Y']
data1 = [[-6,-3],[-4,-1],[-2,-3],[0,1],[2,2]]
data2 = [[7,-4],[4,-1],[2,0],[-1,3],[-4,9]]
data3 = [[3,-4],[3,-1],[3,0],[3,3],[3,9]]
df1 = pd.DataFrame(data=data1, columns=col)
df2 = pd.DataFrame(data=data2, columns=col)
df3 = pd.DataFrame(data=data3, columns=col)
#%%
df1.cov() # 양의 상관관계
df2.cov() # 음의 상관관계
df3.cov() # 서로 독립
#%%
