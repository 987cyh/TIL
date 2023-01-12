# -*- coding: utf-8 -*-
"""
ㅁ 참고: https://wikidocs.net/155233
ㅁ 목적: 접미사/접두사 (suffix / prefix)
ㅁ 칼럼의 이름을 규칙적으로 변경시에 활용, 데이터프레임 인덱스를 일정하게 변경하는데 활요하는 것은 비효율적임
"""
#%%
import pandas as pd
import numpy as np
#%%
d = {'이름': ['이서연', '김민준'], '국어점수': [70, 80], '수학점수': [80, 70]}
df = pd.DataFrame(data=d)
print(df)

print(df.add_suffix('_열'))
print(df.add_prefix('열_'))

df1 = df['이름'].add_prefix('item_')
df1.index
df1 = df1.reset_index() # 인덱스 테스트

df2 = df['국어점수'].add_suffix('_money')
df2.index
df2 = df2.reset_index() # 인덱스 테스트
#%%
s = pd.Series([1, 2, 3, 4])
print(s.add_prefix('item_'))
#%%
