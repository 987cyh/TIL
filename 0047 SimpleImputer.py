# -*- coding: utf-8 -*-
"""
□ 참고:  https://wikidocs.net/153209
□ fillna: Currently only can fill with dict/Series column by column
"""
#%%
import numpy as np
import pandas as pd
#%%
# 데이터
col1 = [1.0,np.nan,3.5,4.5,5.4,np.nan]
col2 = [1.2,4.5,np.nan,8.5,16.0,32.0]
col3 = [6.2,5.2,np.nan,3.0,2.0,1.0]
data = {"col1":col1,"col2":col2,"col3":col3}
df = pd.DataFrame(data)

df.info()
#%%
# 결측값 처리
df1 = df.copy()
df1.fillna(df1.mean(), inplace=True)
df1 = df.copy()
df1.fillna(df1.mean(), inplace=True, axis=0) # axis=0 기본값
df1 = df.copy()
df1.fillna(df1.mean(), inplace=True, axis=1) # NotImplementedError: Currently only can fill with dict/Series column by column

df2 = df.copy()
df2['col1'].fillna(df2['col1'].mean(), inplace=True)
df2['col2'].fillna(df2['col2'].mean(), inplace=True)
df2['col3'].fillna(df2['col3'].mean(), inplace=True)

# 칼럼마다 동일하게, 결측치를 평균값으로 채울 경우에는 개별행마다 적용하지 않아도 결과가 같음 ★★★
from sklearn.impute import SimpleImputer # https://jerry-style.tistory.com/m/62

df3 = df.copy()
my_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
df3 = pd.DataFrame(my_imputer.fit_transform(df3))

df3 = df.copy()
my_imputer = SimpleImputer(missing_values=np.nan, strategy='mean',copy=False)
my_imputer.fit_transform(df3)
#%%
