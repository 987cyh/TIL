# -*- coding: utf-8 -*-
"""
□ python version : 3.9.16
□ 설치 : pip install -U "ray[default]", conda install -c conda-forge modin, conda install botocore
□ 참고 : https://modin.readthedocs.io/
□ 기능 : modin
□ 목적 : modin vs pandas (geopandas는 미지원)
□ 활용방안 : 대용량 파일의 경우에는 modin으로 업무를 진행하는 것이 바람직함
"""
#%%
# package
import modin.pandas as pd
import pandas

import time
import ray
ray.init()
#%%
# This may take a few minutes to download
import urllib.request
s3_path = "https://modin-datasets.s3.amazonaws.com/testing/yellow_tripdata_2015-01.csv"
urllib.request.urlretrieve(s3_path, "taxi.csv")
#%%
"""read_csv"""
# pandas
start = time.time()
pandas_df = pandas.read_csv('yellow_tripdata_2015-01.csv', parse_dates=["tpep_pickup_datetime", "tpep_dropoff_datetime"], quoting=3)
end = time.time()
pandas_duration = end - start
print("Time to read with pandas: {} seconds".format(round(pandas_duration, 3)))
#--------------------------------------------------------------------------------
# modin
start = time.time()
modin_df = pd.read_csv('yellow_tripdata_2015-01.csv', parse_dates=["tpep_pickup_datetime", "tpep_dropoff_datetime"], quoting=3)
end = time.time()
modin_duration = end - start
print("Time to read with Modin: {} seconds".format(round(modin_duration, 3)))
print("Modin is {}x faster than pandas at `read_csv`!".format(round(pandas_duration / modin_duration, 2)))
#%%
"""concat"""
# pandas
start = time.time()

big_pandas_df = pandas.concat([pandas_df for _ in range(25)])

end = time.time()
pandas_duration = end - start
print("Time to concat with pandas: {} seconds".format(round(pandas_duration, 3)))
#--------------------------------------------------------------------------------
# modin
start = time.time()

big_modin_df = pd.concat([modin_df for _ in range(25)])

end = time.time()
modin_duration = end - start
print("Time to concat with Modin: {} seconds".format(round(modin_duration, 3)))

print("Modin is {}x faster than pandas at `concat`!".format(round(pandas_duration / modin_duration, 2)))
#%%
"""apply"""
# pandas
start = time.time()
rounded_trip_distance_pandas = big_pandas_df["trip_distance"].apply(round)

end = time.time()
pandas_duration = end - start
print("Time to apply with pandas: {} seconds".format(round(pandas_duration, 3)))
#--------------------------------------------------------------------------------
# modin
start = time.time()

rounded_trip_distance_modin = big_modin_df["trip_distance"].apply(round)

end = time.time()
modin_duration = end - start
print("Time to apply with Modin: {} seconds".format(round(modin_duration, 3)))
#%%