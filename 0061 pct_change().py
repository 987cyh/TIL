# -*- coding: utf-8 -*-
"""
ㅁ 총인구, 청년인구 등 인구 지표를 작성하기 위해, 성장률을 산정했으나 칼럼끼리의 연산
   df.T → pct_change() 를 잠시 고민했으나, 비효율적인 코드가 작성되어서 포기
"""
#%%
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)  # UserWarning 제거
warnings.simplefilter(action='ignore', category=FutureWarning)  # UserWarning 제거
import pandas as pd
import geopandas as gpd
import numpy as np
#%%
sale = pd.DataFrame(
    {'product': ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a',
                 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
     'year': [2018, 2018, 2018, 2018, 2019, 2019, 2019, 2019, 2020, 2020, 2020, 2020,
              2018, 2018, 2018, 2018, 2019, 2019, 2019, 2019, 2020, 2020, 2020, 2020],
     'quarter': [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4,
                 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],
     'sales': [5, 6, 6, 8, 10, 20, 30, 40, 12, 25, 38, 50,
               60, 65, 80, 95, 100, 125, 130, 140, 110, 130, 132, 144]})
sale.sort_values(by=['product', 'quarter', 'year'])

sale['sales_pct_change_by_1q'] = sale.sort_values(['year', 'quarter']).groupby(['product']).sales.pct_change()
sale['sales_pct_change_by_1y'] = sale.sort_values(['year', 'quarter']).groupby(['product'])['sales'].pct_change(periods=4)
#%%
