# -*- coding: utf-8 -*-
"""
□ 참고 : https://wikidocs.net/154749
ㅁ 기능: all, any
"""
#%%
import pandas as pd
import numpy as np
#%%
[N,T,F]=[pd.NA,True,False]
idx = ['row1','row2','row3','row4']
data = {'col1':[T,T,T,T], 'col2':[F,F,F,F],'col3':[F,T,T,T],'col4':[T,N,T,T],'col5':[T,T,'',T],'col6':[T,T,T,0]}
df = pd.DataFrame(data=data, index=idx)
print(df)
#%%
# 기본적인 사용법(all과 any 비교)
# all은 축의 값이 전부 True면 True를 반환, any는 하나라도 True면 True를 반환
# 0과 공백()은 False로, 결측값(pd.NA)은 True로 분류
print(df.all())
print(df.any())

print(df.all(axis=1))
print(df.any(axis=1))
#%%
# bool_only인수의 사용
# bool_only=True일 경우 모든 요소가 bool형식인 경우만 계산
print(df.any(axis=1))
print(df.all(bool_only=True))
#%%
# skipna인수의 사용
# skipna=True인 경우 결측치는 True로서 계산, skipna=False인 경우 결측치가 포함된 축이 계산에서 제외
print(df.all(skipna=True))
print(df.all(skipna=False))
#%%
