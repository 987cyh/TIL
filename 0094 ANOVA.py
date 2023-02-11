# -*- coding: utf-8 -*-
"""
□ 참고 : https://rfriend.tistory.com/638
□ 내용 : 표본크기가 다른 2개이상의 집단간 일원분산분석 : one-way ANOVA with different sized samples
□ 목적 : 일원분산분석 학습 및 복습, EDA
"""
#%%
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import stats

mpl.rc('font', family='NanumGothic')
mpl.rcParams['axes.unicode_minus'] = False
#%%
# 3 groups of dataset with different sized samples

np.random.seed(1988)

data1 = np.random.normal(0, 1, 30)
data2 = np.random.normal(0, 1, 40)
data3 = np.random.normal(10, 1, 50) # different mean

data123 = [data1, data2, data3]
#%%
# Kernel Density Estimate Plot

plt.rcParams['figure.figsize'] = [10, 6]

sns.kdeplot(data1)
sns.kdeplot(data2)
sns.kdeplot(data3)
plt.show()

# Boxplot
sns.boxplot(data=data123)
plt.xlabel("Group", fontsize=14)
plt.ylabel("Value", fontsize=14)
plt.show()
#%%
# ANOVA with different sized samples using scipy

stats.f_oneway(data1, data2, data3)

# returning f-statistic and p-value
f_val, p_val = stats.f_oneway(*data123)
print('f-statistic:', f_val)
print('p-vale:', p_val)
#%%
# if there is 'NAN', then returns 'NAN'
data1[0] = np.nan
print(data1)

# returns 'nan'
stats.f_oneway(data1, data2, data3)

# get rid of the missing values before applying ANOVA test
stats.f_oneway(data1[~np.isnan(data1)], data2, data3)
#%%
