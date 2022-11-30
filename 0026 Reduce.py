# -*- coding: utf-8 -*-
"""
참고: # https://yensr.tistory.com/92, https://heytech.tistory.com/49,
       https://codingpractices.tistory.com/entry/Python3-%EC%B5%9C%EC%8B%A0%EB%B2%84%EC%A0%84-Reduce-%EC%82%AC%EC%9A%A9%EB%B2%95-lambda-%ED%91%9C%ED%98%84%EB%B2%95

■ redude의 활용
1. list에 담긴 객체를 연산
2. for문을 통해서 연산된 Dataframe이 담긴 list를 하나의 데이터프레임으로 병합 ★★★
"""
#----------------------------------
from functools import reduce
import pandas as pd
#----------------------------------
#%%
def Sum_value(x, y):
    return x + y

# 1. for문을 이용한 코드
target = list(range(1, 21))
result = 0
for value in target:
    result = Sum_value(result, value)
print(result) # 실행 결과: 210

# 3. reduce를 이용한 코드
target = list(range(1, 21))
print(reduce(Sum_value, target))  # 실행 결과: 210

# 3. reduce와 lambda를 이용한 코드
target = list(range(1, 21))
print(reduce(lambda x, y: x + y, target))  # 실행 결과: 210
#----------------------------------
# 데이터 프레임을 공통키로 merge ★★★
temp = [1,2,3,4,5]
reduce(lambda x, y: x+y,temp)

data1 = pd.DataFrame({'id':[10,20,30], 'korean':[98,24,95]})
data2 = pd.DataFrame({'id':[10,20,30], 'math':[54,84,20]})
data3 = pd.DataFrame({'id':[10,20,30], 'english':[85,22,48]})

data_list = [data1, data2, data3]
data0 = reduce(lambda x, y : pd.merge(x,y,on='id'), data_list)
data0.head()
#----------------------------------