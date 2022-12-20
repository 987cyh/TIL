# -*- coding: utf-8 -*-
"""
□ isin indexing
"""
#%%
import pandas as pd
import numpy as np
#%%
# dataframe 생성
d = {'이름': ['이병헌', '김태희','박서준', '송혜교'],'성별': ['남','여','남','여'], '국어점수': [70, 80, 50, 60], '수학점수': [80, 70, 55, 20]}
df = pd.DataFrame(data=d)
df['이름'].values

# 조건필터링
df_condition = df[(df['이름']=='이병헌')|(df['이름']=='박서준')]
df_str_contains = df[df['이름'].str.contains('이병헌|박서준')==True]
df_isin = df[df['이름'].isin(['이병헌','박서준'])]

# isin & indexing
df_isin2 = df[df.index.isin(df[df['성별'] == '남'].index.values)]

temp = df[df['성별'] == '여']
df_isin3 = df[df.index.isin(temp.index.values)]
#%%
