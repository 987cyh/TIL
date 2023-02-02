# -*- coding: utf-8 -*-
"""
□ 활용 : 데이터프레임 내 칼럼 추출후 전처리

□ 참고 : https://wikidocs.net/151224
□ 기능: dtype기반 열 선택 (select_dtypes)

df.dtypes
* include 및 exclude는 비어있거나 겹치면 안되며(에러발생), 스칼라나 list형태의 입력값이 가능합니다.
□ 자료형
1. 숫자형(numeric)은 np.number 또는 'number'
2. 문자형(str)은 'object'
3. 날짜,시간(datetimes)을 선택하려면 np.datetime64, 'datetime' 또는 'datetime64'
4. timedeltas는 np.timedelta64, 'timedelta' or 'timedelta64'
5. Pandas의 categorical 타입은 'category'
"""
#%%
import pandas as pd
import numpy as np
col1 = [1, 2, 3, 4, 5]
col2 = ['one', 'two', 'three', 'four', 'five']
col3 = [1.5, 2.5, 3.5, 4.5, 5.5]
col4 = [True, False, False, True, True]
df = pd.DataFrame({"col1": col1, "col2": col2, "col3": col3, "col4": col4})
print(df)
print(df.dtypes)
#%%
# include
result = df.select_dtypes(include=[float,bool])
print(result)

# exclude
result1 = df.select_dtypes(exclude=['int64'])
print(result1)

# include & exclude 혼합 사용
result2 = df.select_dtypes(include =[float,object], exclude=['int64'])
print(result2)
#%%
