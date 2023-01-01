# -*- coding: utf-8 -*-
"""
ㅁ 목적 : KNN 학습
ㅁ 참고: https://ysyblog.tistory.com/74
"""
#%%
import numpy as np
import pandas as pd
import matplotlib as mpl
import warnings
warnings.filterwarnings(action='ignore')
#%%
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
df = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
df['target'] = cancer['target']
df.head()
#%%
from sklearn.model_selection import train_test_split

X = df.drop(columns='target')
Y = df[['target']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size = 0.7, test_size = 0.3, random_state = 30, stratify=Y) # 데이터를 학습용과 검증용으로 분할

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc = scaler.fit_transform(X_test)
#%%
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

train_list = []
test_list = []

for k in range(1, 11):
    knn = KNeighborsClassifier(n_neighbors=k, n_jobs=-1)
    knn.fit(X_train_sc, Y_train)

    pred_train = knn.predict(X_train_sc)
    pred_test = knn.predict(X_test_sc)

    train_list.append(accuracy_score(Y_train,pred_train))
    test_list.append(accuracy_score(Y_test,pred_test))

dict1 = {'train_acc':train_list,'test_acc':test_list}
df_acc = pd.DataFrame(dict1).reset_index(drop=False)
df_acc.rename(columns={'index':'k'},inplace=True)
df_acc['k'] = df_acc['k'] + 1
#%%
# 그리드서치, 파이프라인
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

Pipeline = Pipeline([('scaler',StandardScaler()),
                     ('knn',KNeighborsClassifier())])

param_grid = {'knn__n_neighbors':range(1,11),
             'knn__p':[1,2]} # 1: 맨하탄, 2: 유클리디안

gs = GridSearchCV(Pipeline,param_grid=param_grid, cv=5, scoring = 'accuracy')
gs.fit(X_train,Y_train)
gs.best_score_
gs.best_params_ # {'knn__n_neighbors': 4, 'knn__p': 2}

best_model = gs.best_estimator_    # 최적모델
best_model.fit(X_train_sc,Y_train) # 학습

pred_train = best_model.predict(X_train_sc)
pred_test = best_model.predict(X_test_sc)

accuracy_score(Y_train,pred_train)
accuracy_score(Y_test,pred_test)

accuracy_score(Y_train,gs.predict(X_train_sc))
accuracy_score(Y_test,gs.predict(X_test_sc))
#%%
