# -*- coding: utf-8 -*-

"""
1. 나라장터 API의 파라미터가 변경될 수 있다는 사실
2. 2022년 상반기에 적용되던 파라미터가 2022년 하반기에 미적용되는 것을 알게됨(bidNtceNm)
"""
####################################
#%%
import pandas as pd
import json
import time
import os
import urllib.request
from pandas.io.json import json_normalize
import numpy as np
import configparser, json, sys
import requests
from urllib import parse
from tqdm import tqdm
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)  # UserWarning 제거
warnings.simplefilter(action='ignore', category=FutureWarning)  # UserWarning 제거
pd.set_option('mode.chained_assignment',  None) # 디스플레이 에러 대비
####################################
#%%
def country_market(start, end):
    url_base = "https://apis.data.go.kr/1230000/BidPublicInfoService03/getBidPblancListInfoServc?"
    ServiceKey = "ServiceKey"
    table = pd.DataFrame()
    page = 1
    while True:
        url_base_m= url_base + '&inqryBgnDt='+ start + '0000' + '&inqryEndDt=' + end + '2359' + \
                     '&pageNo=' + str(page) + '&numOfRows=999' + '&ServiceKey=' + ServiceKey + '&type=json' + '&inqryDiv=1'
        r = requests.get(url_base_m,verify=False).json()
        data = r['response']['body']['items']
        df = pd.DataFrame.from_dict(json_normalize(data), orient='columns')
        if len(df.index) == 0:
            break
        table = table.append(df)
        page += 1
        time.sleep(5)
    return table
####################################
#%%

df_month = pd.DataFrame({'month1':['0101','0201','0301','0401','0501','0601','0701','0801','0901','1001','1101','1201'],
                'month2':['0131','0228','0331','0430','0531','0630','0731','0831','0930','1031','1130','1231']})
df_year = ['2021','2022']

df_list = []
error_list = []

#%%
# Raw Data 호출
start = pd.Timestamp.now()

for k in df_year:
    for i in range(df_month.shape[0]):
        try:
            temp = country_market(k+df_month['month1'][i],k+df_month['month2'][i])
            df_list.append(temp)
        except:
            error_list.append(k+df_month['month1'][i])

print("Raw Data 호출시간: %s" % (pd.Timestamp.now() - start)) # Raw Data 호출시간: 0 days 01:01:44.025833
####################################