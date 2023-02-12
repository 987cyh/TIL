# -*- coding: utf-8 -*-
"""
□ 참고 : https://rfriend.tistory.com/639
□ 내용 : 여러 개의 숫자형 변수(one-way ANOVA for multiple numeric variables in pandas DataFrame) 별로 일원분산분석 검정(one-way ANOVA test)
□ 목적 : 일원분산분석 학습 및 복습, EDA
"""
#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import statsmodels.api as sm
from statsmodels.formula.api import ols
mpl.rc('font', family='NanumGothic')
mpl.rcParams['axes.unicode_minus'] = False
pd.options.mode.chained_assignment = None
#%%
## Creating sample dataset

# generate 90 IDs
id = np.arange(90) + 1

# Create 3 groups with 30 observations in each group.
from itertools import chain, repeat
grp = list(chain.from_iterable((repeat(number, 30) for number in [1, 2, 3]))) # https://rfriend.tistory.com/459 참고

# generate random numbers per each groups from normal distribution
np.random.seed(1004)

# for 'x1' from group 1, 2 and 3
x1_g1 = np.random.normal(0, 1, 30)
x1_g2 = np.random.normal(0, 1, 30)
x1_g3 = np.random.normal(0, 1, 30)

# for 'x2' from group 1, 2 and 3
x2_g1 = np.random.normal(10, 1, 30)
x2_g2 = np.random.normal(10, 1, 30)
x2_g3 = np.random.normal(10, 1, 30)

# for 'x3' from group 1, 2 and 3
x3_g1 = np.random.normal(30, 1, 30)
x3_g2 = np.random.normal(30, 1, 30)
x3_g3 = np.random.normal(50, 1, 30) # different mean

x4_g1 = np.random.normal(50, 1, 30)
x4_g2 = np.random.normal(50, 1, 30)
x4_g3 = np.random.normal(20, 1, 30) # different mean
#%%
# make a DataFrame with all together
df = pd.DataFrame({'id': id,
                   'grp': grp,
                   'x1': np.concatenate([x1_g1, x1_g2, x1_g3]),
                   'x2': np.concatenate([x2_g1, x2_g2, x2_g3]),
                   'x3': np.concatenate([x3_g1, x3_g2, x3_g3]),
                   'x4': np.concatenate([x4_g1, x4_g2, x4_g3])})

df.head()
df[df['grp'] == 3].head()
#%%
## Boxplot for 'x3' by 'grp'
plt.rcParams['figure.figsize'] = [10, 6]
sns.boxplot(x='grp', y='x3', data=df)
plt.show()
#%%
# ANOVA for x1 and grp

model = ols('x1 ~ grp', data=df).fit()
sm.stats.anova_lm(model, typ=1)
#%%
# make a multiindex for possible combinations of Xs and Group
num_col = ['x1','x2', 'x3', 'x4']
cat_col =  ['grp']
mult_idx = pd.MultiIndex.from_product([num_col, cat_col], names=['x', 'grp'])

print(mult_idx)
#%%
# ANOVA test for multiple combinations of X and Group
anova_tables = []
for x, grp in mult_idx:
    model = ols('{} ~ {}'.format(x, grp), data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=1)
    anova_tables.append(anova_table)

df_anova_tables = pd.concat(anova_tables, keys=mult_idx, axis=0)
df_anova_tables
#%%
## Getting values of 'x3' from ANOVA tables
df_anova_tables.loc[('x3', 'grp', 'grp')]
# F-statistic
df_anova_tables.loc[('x3', 'grp', 'grp')]['F']
# P-value
df_anova_tables.loc[('x3', 'grp', 'grp')]['PR(>F)']
#%%
# resetting index to columns
df_anova_tables_2 = df_anova_tables.reset_index().dropna()
df_anova_tables_2
#%%
