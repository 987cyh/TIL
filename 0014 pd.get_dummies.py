# -*- coding: utf-8 -*-
"""
pd.get_dummies()
"""
###############################################################
import numpy as np
import pandas as pd

df = pd.DataFrame({'계절':['봄', '여름', '가을', '겨울',np.nan]})

# 더미변수 생성: 결측값 제외 - dummy_na
df1 = pd.get_dummies(df['계절'])
# 더미변수 생성: 결측값 포함 -dummy_na
df2 = pd.get_dummies(df['계절'], dummy_na=True)
###############################################################