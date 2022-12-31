# -*- coding: utf-8 -*-
"""
□ duplicated(), drop_duplicates()
"""
#%%
import pandas as pd
#%%
# dataframe 생성
d = {'이름': ['송혜교', '김태희','박서준', '송혜교'],'성별': ['남','여','남','여'], '국어점수': [70, 80, 50, 60], '수학점수': [80, 70, 55, 20]}
df = pd.DataFrame(data=d)
#%%
temp1 = df.duplicated(['이름'], keep='first') # 기본값, subset 생략가능
temp1 = df.duplicated(subset=['이름'], keep='first') # 기본값
temp2 = df.duplicated(subset=['이름'], keep='last')
temp3 = df.duplicated(subset=['이름'], keep=False)

temp_confirm = df[df.duplicated(['이름'], keep=False)] # 중복된 열 확인 ★

temp4 = df.drop_duplicates(subset=['이름'], keep='first')
temp5 = df.drop_duplicates(subset=['이름'], keep='last')
temp6 = df.drop_duplicates(subset=['이름'], keep=False)
temp6 = df.drop_duplicates(subset=['이름'], keep=False)
#%%
