# -*- coding: utf-8 -*-
"""
□ 참고 : https://wikidocs.net/157754
ㅁ 기능: tz_convert, time index 변경
"""
#%%
import pandas as pd
import numpy as np
#%%
dr = pd.date_range(start='2021-12-29 09:00', freq='H', periods=4, tz='US/Eastern')
# date_range를 통해 기본 시간과 간격을 설정하고, tz인수를통해 timezone을 지정.
df=pd.DataFrame(index=dr, data={'Seoul':[0,0,0,0],'None':[0,0,0,0]})
print(df)
#%%
data1 = dr.tz_convert('Asia/Seoul')
# 지역/도시명 으로 표준시를 변경할 수 있습니다.
data2 = dr.tz_convert(None)
# None을 입력할 경우 시간대가 삭제됩니다.
df = pd.DataFrame(data={'Seoul':data1,'None':data2},index=dr)
print(df)
#%%
