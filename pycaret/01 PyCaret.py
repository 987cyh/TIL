# -*- coding: utf-8 -*-
"""
□ 참고 : https://pycaret.gitbook.io/docs/, https://sthsb.tistory.com/31
        https://www.kaggle.com/code/frtgnn/pycaret-introduction-classification-regression
□ 기능 : pycaret_classification
□ 목적 : pycaret_classification 학습
"""
#%%
# package
from pycaret.classification import *
import numpy as np
import pandas as pd
#%%
# data load
train = pd.read_csv('titanic_train.csv')
test = pd.read_csv('titanic_test.csv')
sub = pd.read_csv('titanic_gender_submission.csv')

train.head()
train.info()
train.isnull().sum()

# data preprocessing
clf1 = setup(
            data=train,
            target='Survived',
            numeric_imputation='mean',
            categorical_features=['Sex','Embarked'],
            ignore_features=['Name','Ticket','Cabin'],
            session_id=123,
            use_gpu=True
            )
#%%
# compare the model
best_models = compare_models()
"""
RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
                       criterion='gini', max_depth=None, max_features='sqrt',
                       max_leaf_nodes=None, max_samples=None,
                       min_impurity_decrease=0.0, min_samples_leaf=1,
                       min_samples_split=2, min_weight_fraction_leaf=0.0,
                       n_estimators=100, n_jobs=-1, oob_score=False,
                       random_state=123, verbose=0, warm_start=False)
"""
# create rf Model
rf = create_model('rf')

# tune model
tuned_rf = tune_model(rf)
"""
Original model was better than the tuned model, hence it will be returned. 
NOTE: The display metrics are for the tuned model (not the original one).

RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
                       criterion='gini', max_depth=None, max_features='sqrt',
                       max_leaf_nodes=None, max_samples=None,
                       min_impurity_decrease=0.0, min_samples_leaf=1,
                       min_samples_split=2, min_weight_fraction_leaf=0.0,
                       n_estimators=100, n_jobs=-1, oob_score=False,
                       random_state=123, verbose=0, warm_start=False)
"""
#%%
# Learning Curve
plot_model(estimator=tuned_rf, plot='learning')
# AUC Curve
plot_model(estimator=tuned_rf, plot='auc')
# Confusion Matrix
plot_model(estimator=tuned_rf, plot='confusion_matrix')
# Feature Importance
plot_model(estimator=tuned_rf, plot='feature')
#%%
# whole thing
evaluate_model(tuned_rf)

# Interpretation
interpret_model(tuned_rf)
# TypeError: This function only supports tree based models for binary classification: rf, catboost, xgboost, dt, et, lightgbm.

# Predictions
predict_model(tuned_rf, data=test)

predictions = predict_model(tuned_rf, data=test)
predictions.head()
#%%