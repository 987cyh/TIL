# -*- coding: utf-8 -*-
#%%
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)  # UserWarning 제거
warnings.simplefilter(action='ignore', category=FutureWarning)  # UserWarning 제거
import pandas as pd
import geopandas as gpd
import numpy as np
#%%
df = pd.read_csv('법정동코드 전체자료.txt',sep='\t',encoding='cp949')
df1 = df[df['폐지여부']=='존재']
df1['법정동코드'] = df1['법정동코드'].astype(str)
df1 = df1[df1['법정동코드'].str[-5:]=='00000']

temp1 = df1[df1['법정동명']!='세종특별자치시'].reset_index(drop=True)
temp1['dissolve_key'] = np.nan
for k in temp1.index:
    try:
        temp1['dissolve_key'][k] = temp1['법정동명'][k].split()[0] +' '+ temp1['법정동명'][k].split()[1]
    except:
        continue
temp1 = temp1[~temp1['dissolve_key'].isnull()]

# 특례시 목록
sp_list = ['경기도 고양시','경기도 성남시','경기도 수원시','경기도 안산시','경기도 안양시','경기도 용인시',
           '경상남도 창원시','경상북도 포항시','전라북도 전주시','충청남도 천안시','충청북도 청주시']
for j in sp_list:
    temp1.drop(index=temp1[temp1['법정동명']==j].index[0],inplace=True)

temp2 = df1[df1['법정동명']=='세종특별자치시']

df_fin = pd.concat([temp1,temp2]).reset_index(drop=True)
df_fin['dissolve_key'].fillna('세종특별자치시',inplace=True)
#%%
# 검토
len(df_fin['dissolve_key'].unique()) # 229

check = df_fin.drop_duplicates(['dissolve_key'])
check['check'] = check['dissolve_key'].apply(lambda x: x.split()[0])
print(check['check'].value_counts())

del df, df1, j, k, sp_list, temp1, temp2
#%%
