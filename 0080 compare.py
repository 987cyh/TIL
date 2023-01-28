# -*- coding: utf-8 -*-
"""
□ 참고 : https://wikidocs.net/154558
□ 기능: compare
"""
#%%
import pandas as pd
import numpy as np
#%%
idx = ['row1','row2','row3','row4']
col = ['col1','col2','col3']
data1 = [['A',1,11],['B',2,12],['C',3,13],['D',4,14]]
data2 = [['X',1,11],['B','Y',12],['C',3,13],['D',4,'Z']]

df1 = pd.DataFrame(data1, idx, col)
print(df1)
df2 = pd.DataFrame(data2, idx, col)
print(df2)
#%%
print(df1.compare(df2))

# align_axis
print(df1.compare(other=df2, align_axis=0)) # multi index
print(df1.compare(other=df2, align_axis=1)) # multi columns

# keep_shape
print(df1.compare(other=df2, keep_shape=True))
print(df1.compare(other=df2, keep_shape=False))

# keep_equal
print(df1.compare(other=df2, keep_equal=True))
print(df1.compare(other=df2, keep_equal=False))
#%%
