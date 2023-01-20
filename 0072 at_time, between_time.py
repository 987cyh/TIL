# -*- coding: utf-8 -*-
"""
□ 참고 : https://wikidocs.net/157587
ㅁ 기능: at_time, between_time
"""
#%%
import pandas as pd
import numpy as np
#%%
i = pd.date_range('2021-12-24', periods=48, freq='1H')
# 2021-12-24를 시작으로 48기간(간격 1H)의 데이터 생성.
df = pd.DataFrame({'col1':[k for k in range(0,48)]}, index=i)
print(df)
#%%
# at_time,
print(df.at_time('06:00'))
#%%
# between_time
print(df.between_time(start_time='03:00',end_time='06:00'))

# 03:00과 06:00이 제외됨.
print(df.between_time(start_time='03:00',end_time='06:00', include_start=False, include_end=False))

# start_time이 end_time보다 늦음
print(df.between_time(start_time='06:00',end_time='03:00')) #03:00 ~ 06:00을 제외한 시간이 출력됨.
#%%
