# -*- coding: utf-8 -*-
"""
참고 : https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html
errors의 parameter
ㅁ errors = 'ignore' -> 만약 숫자로 변경할 수 없는 데이터라면 숫자로 변경하지 않고 원본 데이터를 그대로 반환
ㅁ errors = 'coerce' -> 만약 숫자로 변경할 수 없는 데이터라면 기존 데이터를 지우고 NaN으로 설정하여 반환
ㅁ errors = 'raise' -> 만약 숫자로 변경할 수 없는 데이터라면 에러를 일으키며 코드를 중단
"""
#%%
import pandas as pd
#%%
t = pd.Series(['1.0', '2', -3])
print(t)
print(type(t))

t1 = pd.to_numeric(t)
print(t1)
print(type(t1))

# pd.to_numeric(숫자로 변경할 대상, errors='ignore/raise/coerce')
s = pd.Series(['apple', '1.0', '2', -3])
s1 = pd.to_numeric(s, errors='ignore') # 변경 불가능한 문자 존치 ★
print(s1)
print(type(s1))

s2 = pd.to_numeric(s, errors='coerce') # NaN으로 변경
print(s2)
print(type(s2))

s3 = pd.to_numeric(s, errors='raise') # error 발생 ★
print(s3)
print(type(s3))