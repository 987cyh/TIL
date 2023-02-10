# -*- coding: utf-8 -*-
"""
□ 참고 : https://rfriend.tistory.com/513
□ 내용 : 로지스틱회귀 모형에 대한 각 관측치별 변수별 기여도(민감도) 분석
□ 목적 : 로지스틱회귀 모형에 대한 각 관측치별 변수별 기여도(민감도) 분석 학습 및 복습
"""
#%%
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
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
#%%
X = sm.add_constant(X) # add a constant to model

# get y value
y = abalone["whole_weight"]
#%%
# make a y_category variable: if y is greater or equal to mean, then 1
y_cat = np.where(abalone["whole_weight"] >= np.mean(abalone["whole_weight"]), 1, 0)
y_cat[:20]

cat_class, counts = np.unique(y_cat, return_counts=True)
dict(zip(cat_class, counts))

# train, test set split
X_train, X_test, y_train, y_test = train_test_split(X, y_cat, test_size=0.2, random_state=2004)
#%%
# fitting logistic regression
logitreg = sm.Logit(y_train, X_train)
logitreg_fit = logitreg.fit()
print(logitreg_fit.summary())

# prediction
test_prob_logitreg = logitreg_fit.predict(X_test)
test_prob_logitreg.head()
#%%
# UDF for contribution(sensitivity) analysis per each variables
# task: "LinearReg" or "LogitReg"

def sensitivity_analysis_LinearReg_LogitReg(task, model, X, idx, bar_plot_yn):
    # get one object's X values
    X_i = X.iloc[idx, :]

    # make a matrix with zeros with shape of [num_cols, num_cols]
    X_mat = np.zeros(shape=[X_i.shape[0], X_i.shape[0]])

    # fil X_mat with values from one by one columns, leaving the ohters zeros
    for i, j in enumerate(X_i):
        X_mat[i, i] = j

    # data frame with contribution of each X columns in descending order
    sensitivity_df = pd.DataFrame({'idx': idx, 'task': task, 'x': X_i, 'contribution_x': model.predict(X_mat)})
    sensitivity_df = sensitivity_df.sort_values(by='contribution_x', ascending=True)

    # if bar_plot_yn == True then display it
    col_n = X_i.shape[0]
    if bar_plot_yn == True:
        sensitivity_df['contribution_x'].plot(kind='barh', figsize=(10, 0.7 * col_n))
        plt.title('Sensitivity Analysis', fontsize=18)
        plt.xlabel('Contribution', fontsize=16)
        plt.ylabel('Variable', fontsize=16)
        plt.yticks(fontsize=14)
        plt.show()
    return sensitivity_df.sort_values(by='contribution_x', ascending=False)
#%%
# apply sensitivity analysis function on 1st observation for Logistic Regression
sensitivity_analysis_LinearReg_LogitReg(task="LogitReg", model=logitreg_fit, X=X_test, idx=0, bar_plot_yn=True)
#%%
