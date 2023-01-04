# -*- coding: utf-8 -*-
"""
□ zip의 이해
□  참고 : https://steadiness-193.tistory.com/266
"""
#%%
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)  # UserWarning 제거
warnings.simplefilter(action='ignore', category=FutureWarning)  # UserWarning 제거
import pandas as pd
import numpy as np
import seaborn as sns
#%%
sns.get_dataset_names()
df = sns.load_dataset('titanic')
df.info()
df.dtypes.value_counts()
#%%
for idx,type1 in zip(df.dtypes.index,df.dtypes):
    print(idx,type1)
#%%
# 데이터 타입별로 칼럼 추출
list_col_int = [idx for idx, type1 in zip(df.dtypes.index,df.dtypes) if type1 == 'int64']
list_col_float = [idx for idx, type1 in zip(df.dtypes.index,df.dtypes) if type1 == 'float64']
list_col_object = [idx for idx, type1 in zip(df.dtypes.index,df.dtypes) if type1 == 'object']
list_col_category = [idx for idx, type1 in zip(df.dtypes.index,df.dtypes) if type1 == 'category']

list_col_num = [idx for idx, type1 in zip(df.dtypes.index,df.dtypes) if type1 in ('int64','float64')] # 숫자형
list_col_not_num = [col for col in df.columns if col not in list_col_num] # 비숫자형
#%%
a = [1,2,3,4,5]
b = [6,7,8,9,0]
temp = list(zip(a,b))

c='happy'
d='honey'
list(zip(c,d))


e='sad'
f='sight'
list(zip(e,f))

for k, j in zip(c,d):
    print(k, j)
#%%
r,t = zip(*temp) # unzip , 튜플 형태로 반환 ★

r = list(r)

temp1 = list(zip(a,b))
temp2 = dict(zip(a,b))
#%%
