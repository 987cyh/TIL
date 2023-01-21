# -*- coding: utf-8 -*-
"""
□ 참고 : https://wikidocs.net/157590
ㅁ 기능: first, last
"""
#%%
import pandas as pd
import numpy as np
#%%
i = pd.date_range('2020-05-08', periods=48, freq='3D')
df = pd.DataFrame({'col1':[k for k in range(0,48)]}, index=i)
print(df)
#%%
print(df.first('20D')) # 첫날짜 기준으로 20일간의 데이터를 필터링함. 20개 날짜의 출력이 아니라 20일동안.
print(df.last('20D')) # 마지막 날짜 기준으로 20일간의 데이터를 필터링.
#%%
