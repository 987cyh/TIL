# -*- coding: utf-8 -*-
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

boston_df.head()
boston_df.info()
#%%
X = df[['TAX', 'AGE']]

from sklearn.preprocessing import StandardScaler
ss = StandardScaler().fit(X)
df_ss = pd.DataFrame(ss.transform(X), columns=ss.get_feature_names_out())
df_ss.head()

ss1 = StandardScaler()
df_ss1 = pd.DataFrame(ss1.fit_transform(X), columns=ss1.get_feature_names_out())
df_ss1.head()
#%%
inverse_transformed_X = scaler.inverse_transform(df_ss1) # 원데이터로 복구
