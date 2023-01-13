# -*- coding: utf-8 -*-
"""
ㅁ 참고: https://wikidocs.net/152928
ㅁ 목적: 임계값 적용
"""
#%%
import pandas as pd
import numpy as np
#%%
col  = ['col1','col2','col3']
row  = ['row1','row2','row3']
data = [[-7,3,9],
        [6,-8,1],
        [-3,0,-7]]
df = pd.DataFrame(data,row,col)
print(df)
#%%
# 열별(column) 임계값 적용
df1 = df.clip(-4,5)
print(df1)
df['col4'] = df['col1'].clip(-2,2)
#%%
# 시리즈를 활용한 '행별(row)' 임계값 적용
s = pd.Series(data=[1,2,3],index=row)
df2 = df.clip(-s,s,axis=0)
#%%
