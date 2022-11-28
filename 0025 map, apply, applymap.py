# -*- coding: utf-8 -*-
"""
참고: https://seong6496.tistory.com/236

■ map, apply, applymap의 구조이해
- apply(): 데이터프레임, 시리즈에 모두 적용 가능
- map(): 시리즈에만 적용가능
- applymap(): 데이터프레임에만 적용가능

"""
##############################
# map
import pandas as pd
x = pd.Series({'one':1,'two':2,'three':3})
y = pd.Series({1:'triangle',2:'square',3:'circle'})

x.map(y)
y.map(x)

y = pd.Series({1:'triangle',2:'square'})
x.map(y)

# map은 인덱스에 따라서 값을 전환하는 기능이니DataFrame에서는 사용할 수 없고 Series에서만 할 수 있음
##############################
# apply
import numpy as np

df = pd.DataFrame(np.arange(12).reshape(4,3),columns=['a','b','c'])
#column 합계
df.apply(lambda x:x.sum())
#row 합계
df.apply(lambda x:x.sum(),axis=1)

df['a+b'] = df.apply(lambda r:r.a+r.b,axis=1)
##############################
# applymap
df.applymap(lambda x:'%.2f'% x) # 모든 value
df.apply(lambda x: '%.2f'% x if x > 5 else x)
#############################