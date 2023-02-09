# -*- coding: utf-8 -*-
"""
□ 참고 : https://rfriend.tistory.com/513
□ 내용 : 선형회귀모형에 대한 각 관측치별 변수별 기여도(민감도) 분석
□ 목적 : 선형회귀모형에 대한 각 관측치별 변수별 기여도(민감도) 분석 학습 및 복습
"""
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('font', family='NanumGothic')
mpl.rcParams['axes.unicode_minus'] = False
#%%
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
abalone = pd.read_csv(url
                      , sep=','
                      , header=None
                      , names=['sex', 'length', 'diameter', 'height',
                               'whole_weight', 'shucked_weight', 'viscera_weight',
                               'shell_weight', 'rings']
                     , index_col=None)
#%%
# transformation of categorical variable to dummy variable
abalone['sex'].unique()
abalone['sex_m'] = np.where(abalone['sex'] == 'M', 1, 0)
abalone['sex_f'] = np.where(abalone['sex'] == 'F', 1, 0)

X = abalone[["sex_m", "sex_f", "length", "diameter", "height", "shell_weight", "rings"]]

import statsmodels.api as sm
X = sm.add_constant(X) # add a constant to model

# get y value
y = abalone["whole_weight"]
#%%
# train, test set split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1000)
#%%
# multivariate linear regression model
import statsmodels.api as sm

lin_reg = sm.OLS(y_train, X_train).fit()
lin_reg.summary()

# prediction
predicted = lin_reg.predict(X_test)

actual = y_test
act_pred_df = pd.DataFrame({'actual': actual, 'predicted': predicted, 'error': actual - predicted})
#%%
# Scatter Plot: Actual vs. Predicted

plt.plot(act_pred_df['actual'], act_pred_df['predicted'], 'o')
plt.xlabel('actual', fontsize=14)
plt.ylabel('predicted', fontsize=14)
plt.show()
#%%
# RMSE (Root Mean Squared Error)
from sklearn.metrics import mean_squared_error
from math import sqrt

rmse = sqrt(mean_squared_error(actual, predicted))
#%%
# get 1st observation's value as an example
X_i = X_test.iloc[0, :]

# all zeros matrix with shape of [col_num, col_num]
X_mat = np.zeros(shape=[X_i.shape[0], X_i.shape[0]])

# fill only 1 variable's value and leave '0' for the others
for i, j in enumerate(X_i):
    X_mat[i, i] = j
#%%
# sensitivity analysis
sensitivity_df = pd.DataFrame({'x': X_test.iloc[0, :], 'contribution_x': lin_reg.predict(X_mat)}).\
    sort_values(by='contribution_x', ascending=False)

# horizontal bar plot by column's contribution

sensitivity_df['contribution_x'].plot(kind='barh', figsize=(10, 5))
plt.title('Sensitivity Analysis', fontsize=16)
plt.xlabel('Contribution', fontsize=16)
plt.ylabel('Variable', fontsize=16)
plt.yticks(fontsize=14)
plt.show()
#%%
# result from sum of contribution analysis
sum(sensitivity_df['contribution_x'])

# result from linear regression model's prediction
lin_reg.predict(X_test.iloc[0, :].to_numpy())
#%%
# UDF for contribution(sensitivity) analysis per each variables
def sensitivity_analysis(model, X, idx, bar_plot_yn):
    pd.options.mode.chained_assignment = None

    # get one object's X values
    X_i = X.iloc[idx, :]

    # make a matrix with zeros with shape of [num_cols, num_cols]
    X_mat = np.zeros(shape=[X_i.shape[0], X_i.shape[0]])

    # fil X_mat with values from one by one columns, leaving the ohters zeros
    for i, j in enumerate(X_i):
        X_mat[i, i] = j

    # data frame with contribution of each X columns in descending order
    sensitivity_df = pd.DataFrame({'idx': idx, 'x': X_i, 'contribution_x': model.predict(X_mat)}).\
        sort_values(by='contribution_x', ascending=True)

    # if bar_plot_yn == True then display it
    col_n = X_i.shape[0]
    if bar_plot_yn == True:
        sensitivity_df['contribution_x'].plot(kind='barh', figsize=(10, 0.7 * col_n))
        plt.title('Sensitivity Analysis', fontsize=18)
        plt.xlabel('Contribution', fontsize=16)
        plt.ylabel('Variable', fontsize=16)
        plt.yticks(fontsize=14)
        plt.show()
    return sensitivity_df

# check UDF
sensitivity_df = sensitivity_analysis(model=lin_reg, X=X_test, idx=0, bar_plot_yn=True)

# without bar plot (bar_plot_yn=False)
sensitivity_df = sensitivity_analysis(model=lin_reg, X=X_test, idx=0, bar_plot_yn=False)
#%%
# calculate sensitivity of each columns of the first 10 objects using for loop

# blank DataFrame to save the sensitivity results together
sensitivity_df_all = pd.DataFrame()
to_idx = 10

for idx in range(0, to_idx):
    sensitivity_df_idx = sensitivity_analysis(model=lin_reg, X=X_test, idx=idx, bar_plot_yn=False)
    sensitivity_df_all = pd.concat([sensitivity_df_all, sensitivity_df_idx], axis=0)
    print("[STATUS]", idx + 1, "/", to_idx, "(", 100 * (idx + 1) / to_idx, "%) is completed...")
#%%
