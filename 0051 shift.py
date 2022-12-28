# -*- coding: utf-8 -*-
#%%
import pandas as pd
pd.options.display.float_format = '{:.2f}'.format
#%%
df1 = pd.DataFrame([['2022-01-03', 1000],
                    ['2022-01-04', 1100],
                    ['2022-01-05', 1200],
                    ['2022-01-06', 1100],
                    ['2022-01-07', 1000],
                    ['2022-01-10', 1100]], columns=['date', 'price'])

df2 = df1.copy()
#%%
# shift 및 수식 활용
df1['shift_1'] = df1['price'].shift(1)
df1['등락'] = (df1['price'] - df1['shift_1']) / df1['shift_1']
df1.drop(columns='shift_1',inplace=True)
#%%
# diff / pct_change 활용
df2['등락1'] = df2['price'].diff(1)                  # 차이 값
df2['등락2']  = df2['price'].pct_change( 1)          # 차이 비율
#%%
