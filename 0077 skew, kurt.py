# -*- coding: utf-8 -*-
"""
□ 참고 : https://wikidocs.net/156734
ㅁ 기능: skew(왜도), kurt(첨도)
"""
#%%
import pandas as pd
import numpy as np
#%%
a = [-5,-4,-3,-3,-2,-2,-1,-1,-1,0,0,0,0,0,1,1,1,2]
b = [-3,-2,-1,-1,-1,-1,0,0,0,0,0,0,1,1,1,1,2,3]
c = [-2,-1,-1,-1,0,0,0,0,0,1,1,1,2,2,3,3,4,5,]
data = {"col1":a,"col2":b,"col3":c}
df = pd.DataFrame(data)
#%%
# skew(왜도)
print(df.skew())
# col1   -0.615774 → '우'측으로 치우침 = 음수
# col2    0.000000 → 대칭으로 치우침
# col3    0.615774 → '좌'측으로 치우침 = 양수

# 데이터의 분포에 따른 최빈값, 중앙값, 평균값의 위치
df['col1'].mode()
df['col1'].median()
df['col1'].mean()

df['col2'].mode()
df['col2'].median()
df['col2'].mean()

df['col3'].mode()
df['col3'].median()
df['col3'].mean()
#%%
# kurt(첨도)
l = [-9,-5,-1,-1,0,0,0,0,0,1,1,5,9] # leptokurtic
m = np.random.normal(0,1,13) # mesokurtic
p = [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6] # Platykurtic
data = {"col1":l,"col2":m,"col3":p}
df = pd.DataFrame(data)
print(df)
print(df.kurt())
# col1    2.190460 → 뾰족 = 양수
# col2    0.495392 → 평균0, 표준편차1인 정규분포에 근접
# col3   -1.200000 → 뭉툭(둥굴) = 음수
#%%
