# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-21/, https://kibua20.tistory.com/194
□ 기능 : lambda
□ 목적 : lambda 기능 정리 : 전처리시 columns 또는 row 기준으로 활용함
"""
#%%
f = lambda x, y: x + y

print(f(10, 20))
print(f([10, 20], [30, 40]))
print(f("SONG", "JUNKI"))
#------------------------------------
f = lambda x, y=3: x + y

print(f(1))
print(f(3, 3))
#------------------------------------
# 다중입력
f = lambda *x: max(x) * 2

print(f(1, 3, 7))
#------------------------------------
# 다중반환
f = [lambda x: x + 10, lambda x: x + 100, lambda x: x + 1000]

print(f[0](1))
print(f[1](1))
print(f[2](1))
#%%
# 최대/최소
L = [[90, 10, -1], [80, 20, -2], [70, 30, -3], [60, 40, -4]]

max1 = max(L, key=lambda x: x[0])
max2 = max(L, key=lambda x: x[1])
max3 = max(L, key=lambda x: x[2])

min1 = min(L, key=lambda x: x[0])
min2 = min(L, key=lambda x: x[1])
min3 = min(L, key=lambda x: x[2])

print(max1)
print(max2)
print(max3)

print(min1)
print(min2)
print(min3)
#%%
# 복합정렬
L = [[3, "d"], [5, "c"], [1, "a"], [0, "b"], [0, "a"]]
L1 = sorted(L, key=lambda x: -x[0])
L2 = sorted(L, key=lambda x: x[1])
L3 = sorted(L, key=lambda x: [x[0], x[1]])

print(L)
print(L1)
print(L2)
print(L3)
#%%
# sample
import pandas as pd
import numpy as np

data = {'A': [10, 20, 30],
        'B': [40, 50, 60],
        'C': [70, 80, 90]}
df = pd.DataFrame(data)

def add(a, b, c):
    return a + b + c
df['add'] = df.apply(lambda row: add(row['A'], row['B'], row['C']), axis=1)
df['add_1'] = df[['A', 'B', 'C']].apply(lambda x: sum(x.values), axis=1)

df['mean'] = df.apply(np.mean, axis=1)
df['mean_1'] = df[['A', 'B', 'C']].apply(lambda x: np.mean(x.values), axis=1)
df.loc['Sum'] = df.apply(np.sum, axis=0)
#-------------------------------------------------------------------------------------
data1 = {'A': ['가', '나', '다'],
         'B': [40, 50, 60],
         'C': [70, 80, 90]}
df1 = pd.DataFrame(data1)
df1['key'] = df1[['A', 'B', 'C']].apply(lambda x: '_'.join(x.values.astype(str)), axis=1)
#%%
