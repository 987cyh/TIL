# -*- coding: utf-8 -*-
"""
□ 회귀분석 예제
□ 참고: https://datascienceschool.net/03%20machine%20learning/04.01%20%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D%20%EC%98%88%EC%A0%9C.html
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
from sklearn.datasets import load_boston

boston = load_boston()
dfX = pd.DataFrame(boston.data, columns=boston.feature_names)
dfy = pd.DataFrame(boston.target, columns=["MEDV"])
df = pd.concat([dfX, dfy], axis=1)
df.info()
df.head()
sns.pairplot(df[["MEDV", "RM", "AGE", "CHAS"]])
plt.show()
#%%
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df["target"] = diabetes.target
df.tail()
sns.pairplot(df[["target", "bmi", "bp", "s1"]])
plt.show()
#%%
from sklearn.datasets import make_regression
"""
n_samples: 표본 데이터의 갯수
n_features: 독립변수의 수(차원)
bias: y절편
noise: 종속변수에 더해지는 잡음
coef: 선형모형의 계수 출력
random_state: 난수 발생용 시드값
"""
X, y, w = make_regression(n_samples=50, n_features=1, bias=100, noise=10, coef=True, random_state=0)

xx = np.linspace(-3, 3, 100)
y0 = w * xx + 100
plt.plot(xx, y0, "r-")
plt.scatter(X, y, s=100)
plt.xlabel("x")
plt.ylabel("y")
plt.title("make_regression 예제")
plt.show()
#%%
X, y, w = make_regression(n_samples=300, n_features=2, noise=10, coef=True, random_state=0)

plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap=mpl.cm.bone)
plt.xlabel("x1")
plt.ylabel("x2")
plt.axis("equal")
plt.title("두 독립변수가 서로 독립이고 둘 다 종속변수와 상관 관계가 있는 경우")
plt.show()
#%%
X, y, w = make_regression(n_samples=300, n_features=2, n_informative=1, noise=0, coef=True, random_state=0)

plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap=mpl.cm.bone)
plt.xlabel("x1")
plt.ylabel("x2")
plt.axis("equal")
plt.title("두 독립변수가 서로 독립이고 둘 중 하나만 종속변수와 상관 관계가 있는 경우")
plt.show()
#%%
X, y, w = make_regression(n_samples=300, n_features=2, effective_rank=1, noise=0, coef=True, random_state=0, tail_strength=0)

plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap=mpl.cm.bone)
plt.xlabel("x1")
plt.ylabel("x2")
plt.axis("equal")
plt.title("두 독립변수가 독립이 아닌 경우")
plt.show()
#%%
