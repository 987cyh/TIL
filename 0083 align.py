# -*- coding: utf-8 -*-
"""
□ 참고 : https://wikidocs.net/153692
□ 기능: 객체 병합_결측제어 가능 (align)
"""
#%%
import pandas as pd
import numpy as np
#%%
n=np.NaN
col1 = ['col1','col2','col3']
row1 = ['row1','row2','row3']
data1 = [[1,2,3],[5,6,7],[9,n,11]]

col2 = ['col2','col3','col4']
row2 = ['row3','row4','row5']
data2 = [[10,11,12],[14,n,16],[18,19,20]]

df1 = pd.DataFrame(data1,row1,col1)
df2 = pd.DataFrame(data2,row2,col2)

print(df1)
print(df2)
#%%
# tuple형태로 반환
print(df1.align(df2,join='outer')[0])
print(df1.align(df2,join='outer')[1])

print(df1.align(df2,join='inner')[0])
print(df1.align(df2,join='inner')[1])

print(df1.align(df2,join='left')[0]) # df1만 사용
print(df1.align(df2,join='left')[1]) # df1만 사용

print(df1.align(df2,join='right')[0]) # df2만 사용
print(df1.align(df2,join='right')[1]) # df2만 사용
#%%
print(df1.align(df2,join='inner',axis=0)[0])
print(df1.align(df2,join='inner',axis=1)[0])
#%%
# fill_value
print(df1.align(df2,join='outer',fill_value='X')[0])
print(df1.align(df2,join='outer',fill_value='X')[1])

print(df1.align(df2,join='outer',method='ffill')[0])
print(df1.align(df2,join='outer',method='bfill')[1])

print(df1.align(df2,join='outer',method='bfill',limit=1)[1])

print(df1.align(df2,join='outer',method='ffill',fill_axis=0)[0])
print(df1.align(df2,join='outer',method='ffill',fill_axis=1)[0])
#%%
