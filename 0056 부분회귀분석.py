# -*- coding: utf-8 -*-
"""
□ 부분회귀분석의 이해(학습), 학습이외의 목적은 無
□ 참고: https://datascienceschool.net/03%20machine%20learning/04.05%20%EB%B6%80%EB%B6%84%ED%9A%8C%EA%B7%80.html
□ 회귀분석 내에서 각 독립변수가, 어떻게 종속변수에 영향을 미치는 가를 가시적으로 확인가능
"""
#%%
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)  # UserWarning 제거
warnings.simplefilter(action='ignore', category=FutureWarning)  # UserWarning 제거
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('font', family='NanumGothic')
mpl.rcParams['axes.unicode_minus'] = False # 음수(마이너스) 깨짐
#%%
import statsmodels.api as sm
from sklearn.datasets import load_boston

boston = load_boston()

dfX0 = pd.DataFrame(boston.data, columns=boston.feature_names)
dfX = sm.add_constant(dfX0)
dfy = pd.DataFrame(boston.target, columns=["MEDV"])
df = pd.concat([dfX, dfy], axis=1)

model_boston = sm.OLS(dfy, dfX)
result_boston = model_boston.fit()

sns.regplot(x="AGE", y="MEDV", data=df)
plt.show()
#%%
# 부분회귀 plot
# https://www.statsmodels.org/dev/generated/statsmodels.graphics.regressionplots.plot_partregress.html
others = list(set(df.columns).difference(set(["MEDV", "AGE"])))

p, resids = sm.graphics.plot_partregress("MEDV", "AGE", others, data=df, obs_labels=False, ret_coords=True)
plt.show()

#%%
fig = plt.figure(figsize=(8, 20))
sm.graphics.plot_partregress_grid(result_boston, fig=fig)
fig.suptitle("")
plt.show()
#%%
sm.graphics.plot_ccpr(result_boston, "AGE")
plt.show()
#%%
fig = plt.figure(figsize=(8, 15))
sm.graphics.plot_ccpr_grid(result_boston, fig=fig)
fig.suptitle("")
plt.show()
#%%
fig = sm.graphics.plot_regress_exog(result_boston, "AGE")
plt.tight_layout(pad=4, h_pad=0.5, w_pad=0.5)
plt.show()
#%%
