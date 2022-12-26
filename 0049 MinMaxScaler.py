# -*- coding: utf-8 -*-
"""

"""
#%%
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)  # UserWarning 제거
warnings.simplefilter(action='ignore', category=FutureWarning)  # UserWarning 제거
import pandas as pd
import numpy as np
#%%
from sklearn.datasets import load_boston
boston = load_boston() # 데이터세트를 로드
boston_df = pd.DataFrame(boston.data, columns = boston.feature_names) # 독립변수(boston.data)를 DataFrame에 저장
boston_df['MEDV'] = boston.target # 종속변수(boston.target)도 DataFrame에 추가

boston_df.head()
boston_df.info()
#%%
X = df[['TAX', 'AGE']]

from sklearn.preprocessing import MinMaxScaler
mns = MinMaxScaler(feature_range=(0,10)).fit(X)
df_mns = pd.DataFrame(mns.transform(X), columns=mns.get_feature_names_out())

mns1 = MinMaxScaler(feature_range=(0,10))
df_mns1 = pd.DataFrame(mns1.fit_transform(X), columns=mns1.get_feature_names_out())
df_mns1.head()
#%%
inverse_transformed_X = scaler.inverse_transform(df_mns1) # 원데이터로 복구
