# -*- coding: utf-8 -*-

"""
■ MNUM의 변경을 통해서, 이번달과 지난달의 고시변경내역 검토
"""

###############################################################
#%%
import geopandas as gpd
import pandas as pd
import numpy
import fiona
import six
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)
pd.set_option('mode.chained_assignment',  None)
###############################################################
#%%
# 이번달 this_month, 지난달 that_month 데이터 로드
this_month = gpd.read_file('AL_00_D129_20221105.zip', encoding='cp949')
that_month = gpd.read_file('AL_00_D129_20221001.zip', encoding='cp949')
###############################################################
# 변경된 경관지구 개수 확인하기

# 이번달에만 있음
print("이번달 경관지구 변경개수: %s" %(len(set(this_month['A1'].unique()) - set(that_month['A1'].unique()))))
# 지난달에만 있음
print("지난달에만 존재하는 경관지구 개수: %s" %(len(set(that_month['A1'].unique()) - set(this_month['A1'].unique()))))
###############################################################
cake = 'cake'
cake.replace({'a':''})