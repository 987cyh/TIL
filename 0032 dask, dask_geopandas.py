# -*- coding: utf-8 -*-
"""
□ dask,dask_geopandas를 활용한 메모리에 데이터 로드하기
1. 개별 원천 파일을 for문을 이용해서 파일을 하나씩 append로 누적 저장하는 방법을 전처리를 실시함
2. for문 내 dataframe에는 마지막 파일만 남아있고, 전체파일은 로컬에 저장되어 있어, DB에 업로드에 어려움이 발생
3. dask, dask_geopandas의 compute를 통해서, 병렬구조로 로드한 후 postgresql에 업로드 실시
"""
#--------------------------------------------------------
import geopandas as gpd
import pandas as pd
import dask_geopandas
from dask.diagnostics import ProgressBar
pbar = ProgressBar()
pbar.register()
from dask.distributed import Client
import dask.dataframe as dd
import dask.array as da
import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)
pd.set_option('mode.chained_assignment',  None)
gpd.options.use_pygeos = True
#--------------------------------------------------------
# 토지피복지도: 20GB, 100만 row 이상
path1 ='land_map.gpkg'
land_map = dask_geopandas.read_file(path1, npartitions=20)
land_map = land_map.compute(scheduler='processes', num_workers=10)
#---------------------------------
# 용도지역: 1.5GB, 70만 row 이상
path2 = 'city_ydgy.gpkg'
city_ydgy = dask_geopandas.read_file(path2, npartitions=20)
city_ydgy = city_ydgy.compute(scheduler='processes', num_workers=10)
#---------------------------------