# -*- coding: utf-8 -*-
"""
■ Shp을 Dissolve 또는 Explode 할때, geometry가 오류를 발생할 수 있음
1. 과거 지방자치단체 A시에서 geometry의 오류가 발생해서, 공간연산이 안되는 shp이 있었고 이를 수정해서 등재하였음
2. 현재 공간정보포털에서 제공하는 Shp중에서도 이러한 문제가 있음
→ 이는 문제는 Geopandas에서는 Buffer에 0을 주어 해결함
"""
##############################
import geopandas as gpd
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)
pd.set_option('mode.chained_assignment',  None)
###############################################################
#%%
# 코드 분류 엑셀자료 불러오기
df_class = pd.read_excel('용도지역지구구분코드 조회자료.xls')
df_class = df_class[df_class['코드값'].notna()]
###############################################################
#%%
# MNUM 코드 매칭 사용자 정의 함수
def mnum_code_matching(input):
    temp = gpd.read_file(input, encoding='cp949')
    temp = temp.set_crs(epsg=5174)
    temp.to_crs(epsg=4326, inplace=True)
    temp['CODE'] = temp['MNUM'].str[20:26]
    temp = temp.merge(df_class, how='left', left_on='CODE', right_on='코드값')
    temp.drop(['코드값','비고'], axis=1, inplace=True)
    temp.rename(columns={'코드값의미': 'CODENAME'}, inplace=True)
    temp.insert(len(temp.columns) - 1, 'geometry', temp.pop('geometry'))
    return temp
###############################################################
# geo dataframe
geo_df = mnum_code_matching('LSMD_CONT_UQ111_서울.zip')

geo_df['geometry'] = geo_df.buffer(0) #링 자기 교차 오류 제거
###############################################################