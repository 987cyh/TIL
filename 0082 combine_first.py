# -*- coding: utf-8 -*-
"""
□ 참고 : https://wikidocs.net/153673
□ 기능: 다른 객체로 결측치 덮어쓰기 (combine_first)
"""
#%%
import pandas as pd
import numpy as np
#%%
n=np.NaN
col = ['col1','col2','col3']
row = ['row1','row2','row3']
data1 = [[n,n,1],
         [n,n,1],
         [1,1,1]]
data2 = [[2,2,2],
         [2,n,2],
         [2,1,2]]
df1 = pd.DataFrame(data1,row,col)
df2 = pd.DataFrame(data2,row,col)

print(df1)
print(df2)
#%%
print(df1.combine_first(df2))
#%%
