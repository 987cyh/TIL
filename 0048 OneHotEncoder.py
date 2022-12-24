# -*- coding: utf-8 -*-
"""
□ 참고:  https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html
"""
#%%
import pandas as pd

df = pd.DataFrame({
    "Food": ["Cake"] * 25 + ["Pizza"] * 25 + ["Chicken"] * 30 + ["Sushi"] * 20,
    "Review": ["A"] * 30 + ["B"] * 20 + ["C"] * 10 + ["D"] * 40,
    "Application": ["Baemin"] * 30 + ["Yogiyo"] * 20 + ["Coupangeats"] * 10 + ["Ddangyo"] * 40})

df.info()

import sklearn
sklearn.__version__

from sklearn.preprocessing import OneHotEncoder

ohe1 = OneHotEncoder(sparse=False)
df_ohe1 = pd.DataFrame(ohe1.fit_transform(df), columns=ohe1.get_feature_names_out()) # fit_transform, get_feature_names_out
df_ohe1.head()

ohe2 = OneHotEncoder(sparse=False).fit(df) # fit
df_ohe2 = pd.DataFrame(ohe2.transform(df), columns=ohe2.get_feature_names_out()) # transform, get_feature_names_out
df_ohe2.head()
#%%
