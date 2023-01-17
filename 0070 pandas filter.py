# -*- coding: utf-8 -*-
"""
ㅁ 참고: https://wikidocs.net/153179
ㅁ 목적: 특정 칼럼만 도출하기
→ df.columns에서 lambda와 any, if를 통해서 특정 칼럼을 도출하였으나, 필터를 활용하는 방식으로 변경예정
"""
#%%
import pandas as pd
import numpy as np
#%%
col  = ['alpha','beta','gamma','delta','epsilon']
row  = ['sigma','omega','lambda']
data = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
df = pd.DataFrame(data,row,col)
print(df)
#%%
# item 파라미터
print(df.filter(items=['alpha','delta'])) # 열(칼럼) 필터링
print(df.filter(items=['omega'],axis=0))  # 행(로우) 필터링
#%%
# like 파라미터
print(df.filter(like='ta'))
print(df.filter(like='ga',axis=0))
#%%
# 정규표현식
print(df.filter(regex='[mn]'))
print(df.filter(regex='^g'))
print(df.filter(regex='a$'))

print(df.filter(regex='^s',axis=0))
print(df.filter(regex='da$',axis=0))
#%%
