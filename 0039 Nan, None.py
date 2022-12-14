# -*- coding: utf-8 -*-
"""
참고 :https://daje0601.tistory.com/53
ㅁ NaN: Not a Number의 약자로 숫자 형태의 누락된 데이터, float
ㅁ None: 문자 형태의 누락된 데이터, str

→ 차이와 의미를 한 번 살펴볼 필요가 있음
"""
#%%
import math
import numpy as np
import pandas as pd
#%%
print(np.NaN == np.NaN)  # False
print(np.NaN == None)  # False
print(np.NaN is None)  # False
print(None == None)  # True
print(None is None)  # True

print(math.isnan(np.NaN))  # True
print(np.isnan(np.NaN))  # True
print(pd.isna(np.NaN))  # True