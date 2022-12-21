# -*- coding: utf-8 -*-
"""
□ 참고:  https://wikidocs.net/154693
□ idxmax, idxmin
"""
#%%
import numpy as np
import pandas as pd
#%%
n=np.NaN

idx =  ['row1','row2','row3']
col =  ['col1','col2','col3']
data = [[1,2,200],[100,5,6],[7,300,n]]
df = pd.DataFrame(data, idx, col)

print(df)
# axis=0인경우(기본값) 열에서 최대/최소 값에 해당되는 행을 출력
print(df.idxmax(axis=0))
print(df.idxmin(axis=0))

# axis=1인경우 행에서 최대/최소 값에 해당되는 열을 출력
print(df.idxmax(axis=1))
print(df.idxmin(axis=1))

# skipna인수의 사용
# skipna인수는 기본값이 True로 결측값이 포함된 행/열을 연산에서 무시, False일 경우 NaN를 출력
print(df.idxmax(axis=1,skipna=True))
print(df.idxmax(axis=1,skipna=False))
#%%
