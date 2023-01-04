# -*- coding: utf-8 -*-
"""
ㅁ 참고 : https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.truncate.html
"""
#%%
import pandas as pd
import numpy as np
#%%
# dataframe 생성
df = pd.DataFrame({'A': ['a', 'b', 'c', 'd', 'e'],
                   'B': ['f', 'g', 'h', 'i', 'j'],
                   'C': ['k', 'l', 'm', 'n', 'o']},
                  index=[1, 2, 3, 4, 5])

df.truncate(before=2, after=4)
df.truncate(before="A", after="B", axis="columns")
df['A'].truncate(before=2, after=4)
#%%
dates = pd.date_range('2016-01-01', '2016-02-01', freq='s')
df1 = pd.DataFrame(index=dates, data={'A': 1})
df1.info()

df1.truncate(before=pd.Timestamp('2016-01-05'),after=pd.Timestamp('2016-01-10')).tail()
df1.truncate('2016-01-05', '2016-01-10').tail()
df1.loc['2016-01-05':'2016-01-10', :].tail()
#%%
