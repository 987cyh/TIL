# -*- coding: utf-8 -*-

import requests, json
from pandas import json_normalize
###############################################################
#%%
serviceKey = 'serviceKey'

# APT 분양정보 상세조회
url = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail?'
params ={'serviceKey': serviceKey, 'page': '1', 'perPage': '5000'}
data = requests.get(url, params=params).content
apt_info = json_normalize(json.loads(data)['data'])
apt_info.to_csv('apt_info.txt', sep='|', encoding='cp949', index=False)
###############################################################