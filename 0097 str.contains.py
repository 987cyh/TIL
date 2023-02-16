# -*- coding: utf-8 -*-
"""
□ 참고 : https://rfriend.tistory.com/740
□ 목적 : str.contains 기능 재복습(NA/NAN Values 파라미터 복습)
"""
#%%
import numpy as np
import pandas as pd
#%%
## creating a pandas DataFrame with strings, NaN, digit
df = pd.DataFrame({'id': [1, 2, 3, 4, 5, 6, 7], 'fruit': ['apple', 'PERSIMON', 'grapes', 'mango', 'peach and perl',np.NaN, '1004']})
print(df)
#%%
## pandas Series
s1 = df['fruit']
print(type(s1)) # padnas.Series
print(s1)
#%%
## returning a Series of Booleans using a literal pattern
s1.str.contains('pe')

 ## ValueError: Cannot mask with non-boolean array containing NA / NaN values
df[df['fruit'].str.contains('pe')]

## Specifying na to be False instead of NaN replaces NaN values with False.
df[df['fruit'].str.contains('pe', na=False)] # specifying NA to be False

## Specifying case sensitivity using case.
df[df['fruit'].str.contains('pe', na=False, case=False)]  # case = False

## returning any digit using regular expression
df[df['fruit'].str.contains('\\d' # returning any digit
    , regex=True # using regular expression
    , na=False)]

## Returning ‘apple’ or ‘mango’ or 'grapes'
## when either expression occurs in a string.
s1.str.contains(
    '|'.join(['ap', 'ma', 'gr']) # 'ap|ma|gr', ie. 'ap' or 'ma' or 'gr'
    , na=False, case=False)

## indexing data using a Series of Booleans
df[df['fruit'].str.contains(
    '|'.join(['ap', 'ma', 'gr'])
    , na=False
    , case=False)]
#%%
