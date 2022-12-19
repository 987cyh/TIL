# -*- coding: utf-8 -*-
"""
□ 단순회귀분석의 이해(학습), 학습이외의 목적은 無
□ 참고: https://inuplace.tistory.com/500, https://hleecaster.com/ml-multiple-linear-regression-example/, https://dprdmr.tistory.com/30
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
"""
종속변수: MEDV - 주택가격의 중앙값(천단위)
독립변수: RM - 평균방의 갯수
"""
from sklearn.datasets import load_boston
boston = load_boston() # 데이터세트를 로드
boston_df = pd.DataFrame(boston.data, columns = boston.feature_names) # 독립변수(boston.data)를 DataFrame에 저장
boston_df['MEDV'] = boston.target # 종속변수(boston.target)도 DataFrame에 추가
boston_df.head()
# 시각화
plt.scatter(boston_df['RM'], boston_df['MEDV'])  # 평균 방 개수와 주택가격의 산포도를 플로트(plot)
plt.title('Scatter Plot of RM vs MEDV')          # 그래프의 제목
plt.xlabel('Average number of rooms [RM]')       # x축의 라벨
plt.ylabel('Prices in $1000\'s [MEDV]')          # y축의 라벨
plt.grid()                                       # 그리드 선을 표시
plt.show()                                       # 그래프를 표시

print(boston_df[['RM','MEDV']].corr(method='pearson'))
#%%
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

X = boston_df[['RM']].values         # 독립변수（NumPy의 배열）
Y = boston_df['MEDV'].values         # 종속변수（Numpy의 배열）

lr.fit(X, Y)                         # 선형 모델의 가중치를 학습

print('coefficient = ', lr.coef_[0]) # 독립변수의 계수를 출력
print('intercept = ', lr.intercept_) # 절편을 출력
# 시각화
plt.scatter(X, Y, color = 'blue')           # 독립변수와 종속변수의 데이터 점의 산포도를 플로트
plt.plot(X, lr.predict(X), color = 'red')   # 회귀직선을 플로트
plt.title('Regression Line')                # 그래프의 제목
plt.xlabel('Average number of rooms [RM]')  # x축의 라벨
plt.ylabel('Prices in $1000\'s [MEDV]')     # y축의 라벨
plt.grid()                                  # 그리드선을 표시
plt.show()                                  # 그래프 표시
#%%
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size = 0.8, test_size = 0.2, random_state = 0) # 데이터를 학습용과 검증용으로 분할
lr = LinearRegression()
lr.fit(X_train, Y_train) # 선형 모델의 가중치를 학습

Y_pred = lr.predict(X_test) # 검증 데이터를 사용해 종속변수를 예측
# 시각화
plt.scatter(Y_pred, Y_pred - Y_test, color = 'blue')      # 잔차를 플로트
plt.hlines(y = 0, xmin = -10, xmax = 50, color = 'black') # x축에 따른 직선을 플로트
plt.title('Residual Plot')                                # 그래프의 제목
plt.xlabel('Predicted Values')                            # x축의 라벨
plt.ylabel('Residuals')                                   # y축의 라벨
plt.grid()                                                # 그리드 선을 표시
plt.show()                                                # 그래프를 표시
#%%
# MSE
from sklearn.metrics import mean_squared_error

Y_train_pred = lr.predict(X_train) # 학습데이터에 대한 종속변수를 예측
print('MSE train data: ', mean_squared_error(Y_train, Y_train_pred)) # 학습 데이터를 사용했을 때의 평균 제곱 오차를 출력

# Y_pred = lr.predict(X_test) # 검증 데이터를 사용해 종속변수를 예측
print('MSE test data: ', mean_squared_error(Y_test, Y_pred))         # 검증 데이터를 사용했을 때의 평균 제곱 오차를 출력
#%%
# R2
from sklearn.metrics import r2_score

print('r^2 train data: ', r2_score(Y_train, Y_train_pred))
print('r^2 test data: ', r2_score(Y_test, Y_pred))
#%%
