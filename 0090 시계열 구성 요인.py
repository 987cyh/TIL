# -*- coding: utf-8 -*-
"""
□ 참고 : https://rfriend.tistory.com/509
□ 내용 : 시계열 구성 요인 4가지와 시계열 가법 모형
"""
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
#%%
dates = pd.date_range('2022-01-01', periods=48, freq='M')

# additive model: trend + cycle + seasonality + irregular factor
timestamp = np.arange(len(dates))
np.random.seed(2004)

trend_factor = timestamp*1.1
cycle_factor = 10*np.sin(np.linspace(0, 3.14*2, 48))
seasonal_factor = 7*np.sin(np.linspace(0, 3.14*8, 48))
irregular_factor = 2*np.random.randn(len(dates))

# df
df = pd.DataFrame({'timeseries': trend_factor + cycle_factor + seasonal_factor + irregular_factor,
                   'trend': trend_factor,
                   'cycle': cycle_factor,
                   'seasonal': seasonal_factor,
                   'irregular': irregular_factor},
                   index=dates)
#%%
# Time series plot
plt.figure(figsize=[10, 6])
df.timeseries.plot()
plt.title('Time Series (Additive Model)', fontsize=16)
plt.ylim(-12, 55)
plt.show()

# -- Trend factor
#timestamp = np.arange(len(dates))
#trend_factor = timestamp*1.1

plt.figure(figsize=[10, 6])
df.trend.plot()
plt.title('Trend Factor', fontsize=16)
plt.ylim(-12, 55)
plt.show()

# -- Cycle factor
#cycle_factor = 10*np.sin(np.linspace(0, 3.14*2, 48))

plt.figure(figsize=[10, 6])
df.cycle.plot()
plt.title('Cycle Factor', fontsize=16)
plt.ylim(-12, 55)
plt.show()

# -- Seasonal factor
#seasonal_factor = 7*np.sin(np.linspace(0, 3.14*8, 48))

plt.figure(figsize=[10, 6])
df.seasonal.plot()
plt.title('Seasonal Factor', fontsize=16)
plt.ylim(-12, 55)
plt.show()

# -- Irregular/ Random factor
#np.random.seed(2004)
#irregular_factor = 2*np.random.randn(len(dates))

plt.figure(figsize=[10, 6])
df.irregular.plot()
plt.title('Irregular Factor', fontsize=16)
plt.ylim(-12, 55)
plt.show()

# All in one: Time series = Trend factor + Cycle factor + Seasonal factor + Irregular factor

rcParams['figure.figsize'] = 12, 8
df.plot()
plt.ylim(-12, 55)
plt.show()
#%%
