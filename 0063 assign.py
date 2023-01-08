# -*- coding: utf-8 -*-
"""
ㅁ 참고 : https://wikidocs.net/154229
ㅁ assign, 열(칼럼) 할당의 핵심의 2개이상의 열을 부여할 때가 핵심
"""
#%%
import pandas as pd
import numpy as np
#%%
df = pd.DataFrame(index=['row1','row2','row3'],data={'col1':[1,2,3]})
print(df)

# 단일열(칼럼)
df1 = df.assign(col2=lambda x: x.col1+2)
df2 = df.assign(col3=df['col1']*(-2)) # df1['col3'] = df1['col1']*(-2)

# 2개이상의 열
df3 = df.assign(col2=lambda x: x.col1+2,col3=df['col1']*(-2)) # 코드 간결화 가능

# 기존열 덮어쓰기
df4 = df.assign(col1=[0,0,0])
#%%
