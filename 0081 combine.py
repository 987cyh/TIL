# -*- coding: utf-8 -*-
"""
□ 참고 : https://wikidocs.net/153671
□ 기능: combine
"""
#%%
import pandas as pd
import numpy as np
#%%
n=np.NaN
col = ['col1','col2','col3']
row = ['row1','row2','row3']
data1 = [[1,3,4],
         [n,8,2],
         [2,6,7]]
data2 = [[7,2,3],
         [2,4,2],
         [3,1,5]]
df1 = pd.DataFrame(data1,row,col)
df2 = pd.DataFrame(data2,row,col)

print(df1)
print(df2)
#%%
# np.maximum
print(df1.combine(df2,np.maximum))
# np.minimum
print(df1.combine(df2,np.minimum))
#%%
# fill_value
print(df1.combine(df2,np.maximum,fill_value=9))
print(df1.combine(df2,np.minimum,fill_value=0))
#%%
# overwrite
col3 = ['col1','col2']
row3 = ['row1','row2']
data3 = [[1,2],
         [3,4]]
df3 = pd.DataFrame(data3, row3, col3)
print(df3)

print(df1.combine(df3, np.maximum,overwrite=False))
print(df1.combine(df3, np.maximum,overwrite=True))

print(df1.combine(df3, np.minimum,overwrite=False))
print(df1.combine(df3, np.minimum,overwrite=True))
#%%
