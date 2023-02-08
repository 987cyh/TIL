# -*- coding: utf-8 -*-
"""
□ 참고 : https://rfriend.tistory.com/510, https://mac-user-guide.tistory.com/14
□ 내용 : 시계열 분해
□ 목적 : 시계열 분해 학습
"""
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('font', family='NanumGothic')
mpl.rcParams['axes.unicode_minus'] = False
#%%
dates = pd.date_range('2022-01-01', periods=48, freq='M')

# additive model: trend + cycle + seasonality + irregular factor
timestamp = np.arange(len(dates))
trend_factor = timestamp*1.1
cycle_factor = 10*np.sin(np.linspace(0, 3.14*2, 48))
seasonal_factor = 7*np.sin(np.linspace(0, 3.14*8, 48))
np.random.seed(1500)
irregular_factor = 2*np.random.randn(len(dates))

# df
df = pd.DataFrame({'timeseries': trend_factor + cycle_factor + seasonal_factor + irregular_factor,
                   'trend': trend_factor,
                   'cycle': cycle_factor,
                   'trend_cycle': trend_factor + cycle_factor, # 추세+순환
                   'seasonal': seasonal_factor,
                   'irregular': irregular_factor},
                   index=dates)
#%%
from statsmodels.tsa.seasonal import seasonal_decompose

ts = df.timeseries
result = seasonal_decompose(ts, model='additive')

plt.rcParams['figure.figsize'] = [12, 8]
result.plot()
plt.show()
#%%
# ground truth & timeseries decompostion all together
# -- observed data
plt.figure(figsize=(12, 12))
plt.subplot(4,1,1)
result.observed.plot()
plt.grid(True)
plt.ylabel('Observed', fontsize=14)

# -- trend & cycle factor
plt.subplot(4,1,2)
result.trend.plot()        # from timeseries decomposition
df.trend_cycle.plot()     # ground truth
plt.grid(True)
plt.ylabel('Trend', fontsize=14)

# -- seasonal factor
plt.subplot(4,1,3)
result.seasonal.plot()  # from timeseries decomposition
df.seasonal.plot()        # ground truth
plt.grid(True)
plt.ylabel('Seasonality', fontsize=14)

# -- irregular factor (noise)
plt.subplot(4,1,4)
result.resid.plot()    # from timeseries decomposition
df.irregular.plot()    # ground truth
plt.grid(True)
plt.ylabel('Residual', fontsize=14)

plt.show()
#%%
