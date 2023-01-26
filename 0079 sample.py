# -*- coding: utf-8 -*-
"""
□ 참고 : https://wikidocs.net/153182
□ 기능: sample
"""
#%%
import pandas as pd
import numpy as np
#%%
col  = ['col1','col2','col3']
row  = ['row1','row2','row3','row4','row5']
data = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
df = pd.DataFrame(data,row,col)
print(df)
#%%
print(df.sample(2))
print(df.sample(10,replace=True)) # 중복추출
print(df.sample(frac=0.4)) # 40%
#%%
s = pd.Series(data=[10,10,3,3,1],index=row) # 가중치 시리즈
print(s)

print(df.sample(2,weights=s))
#%%
print(df.sample(5,random_state=7)) # random_state
print(df.sample(3,ignore_index=True)) # ignore_index
#%%
