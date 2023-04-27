# -*- coding: utf-8 -*-
"""
□ 참고 : https://pycaret.gitbook.io/docs/, https://sthsb.tistory.com/31
        https://www.kaggle.com/code/frtgnn/pycaret-introduction-classification-regression
□ 기능 : pycaret_regression
□ 목적 : pycaret_regression 학습
"""
#%%
# package
from pycaret.regression import *
import numpy as np
import pandas as pd
#%%
# data load
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
sample = pd.read_csv('sample_submission.csv')
#%%
train.head()
train.info()

# data preprocessing
reg = setup(data=train,
             target='SalePrice',
             numeric_imputation='mean',
             categorical_features=['MSZoning','Exterior1st','Exterior2nd','KitchenQual','Functional','SaleType',
                                   'Street','LotShape','LandContour','LotConfig','LandSlope','Neighborhood',
                                   'Condition1','Condition2','BldgType','HouseStyle','RoofStyle','RoofMatl',
                                   'MasVnrType','ExterQual','ExterCond','Foundation','BsmtQual','BsmtCond',
                                   'BsmtExposure','BsmtFinType1','BsmtFinType2','Heating','HeatingQC','CentralAir',
                                   'Electrical','GarageType','GarageFinish','GarageQual','GarageCond','PavedDrive',
                                   'SaleCondition'],
             ignore_features=['Alley','PoolQC','MiscFeature','Fence','FireplaceQu','Utilities'],
             normalize=True,
            session_id=123
            )
#%%
# compare the model
best_models = compare_models()

# create CatBoostRegressor Model
catboost = create_model('catboost')

# tune model
tuned_catboost = tune_model(catboost)  # Fitting 10 folds for each of 10 candidates, totalling 100 fits

# Interpretation
interpret_model(tuned_catboost)

# Predictions
predictions = predict_model(tuned_catboost, data=test)
sample['SalePrice'] = predictions['predictions_label']
sample.head()

sample.to_csv('submission_house_price.csv', index=False)
#%%
