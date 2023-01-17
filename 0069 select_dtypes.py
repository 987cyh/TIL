# -*- coding: utf-8 -*-
"""
ㅁ 참고: https://wikidocs.net/151224
ㅁ 목적: 칼럼 타입기반 선택
→ 지난번 zip구조로 특정 타입의 칼럼을 추출하는 방식을 활용하지 않고 편리하게 가능함, 꿀팁
"""
#%%
import pandas as pd
import numpy as np
#%%
col1 = [1, 2, 3, 4, 5]
col2 = ['one', 'two', 'three', 'four', 'five']
col3 = [1.5, 2.5, 3.5, 4.5, 5.5]
col4 = [True, False, False, True, True]
df = pd.DataFrame({"col1": col1, "col2": col2, "col3": col3, "col4": col4})
print(df)
print(df.dtypes)
#%%
result = df.select_dtypes(include=[float,bool]) # 특정 타입의 칼럼만 포함
print(result)

result2 = df.select_dtypes(exclude=['int64']) # 특정 타입의 칼럼만 제외
print(result2)

result3 = df.select_dtypes(include=[float,object], exclude=['int64']) # 타입 혼합 인덱싱
print(result3)
#%%
