# -*- coding: utf-8 -*-
"""
□ np.where 조건문
"""
#%%
import pandas as pd
import numpy as np
#%%
df = pd.DataFrame({'a':[100,200,300,400,500], 'b':[10,20,30,40,50], 'c':[1,2,3,4,5]})
#%%
# np.where
df['np_where_a'] = np.where(df['a'] > 300, '300초과','300이하')
df['np_where_b'] = np.where(df['b'].isin([10, 30]), 'O', 'X')
df['np_where_c'] = np.where(df['c'] == 1, '대상', '비대상')
#%%
# loc
df.loc[df['a']> 300, ('loc_a')] = '300초과'
df['loc_a'] = df['loc_a'].fillna('300이하')

df.loc[df['b'].isin([10, 30]), ('loc_b')] = 'O'
df['loc_b'] = df['loc_b'].fillna('X')

df.loc[df['c'] == 1, ('loc_c')] = '대상'
df['loc_c'] = df['loc_c'].fillna('비대상')
#%%
