# -*- coding: utf-8 -*-
"""
□ 참고 : https://rfriend.tistory.com/680
□ 목적 : 칼럼순서 변경, 데이터 전처리 코드 재복습
"""
#%%
import numpy as np
import pandas as pd
#%%
# making the sample DataFrame
df = pd.DataFrame(np.arange(12).reshape(2, 6), columns=['x1', 'x2', 'x3', 'x4', 'x5', 'y'])
print(df)
#%%
# (1) reassigning the new order of columns
df2 = df[['y', 'x1', 'x2', 'x3', 'x4', 'x5']]
print(df2)
#%%
# (2) reassignning with a list of columns
col_list = df.columns.tolist()
print(col_list)

new_col_list = col_list[-1:] + col_list[:-1]
print(new_col_list)

df3 = df[new_col_list]
print(df3)
#%%
# (3) making columns list using concatenation and for-loop
new_col_list2 = ['y'] + ['x'+str(i+1) for i in range(5)]
print(new_col_list2)
print(df[new_col_list2])
#%%
# (4) reassignning the order using Positioning index
df4 = df.iloc[:, [5, 0, 1, 2, 3, 4]]
print(df4)
#%%
# (5) reassignning the column order using condition statement
df5 = df[['y'] + [col for col in df.columns if col != 'y']]
print(df5)
#%%
