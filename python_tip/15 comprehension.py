# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-19/, https://datascienceschool.net/
□ 기능 : comprehension
□ 목적 : comprehension 기능 정리 → list comprehension + if 및 dictionary comprehension를 자주 활용함
"""
#%%
"""
간소화(Comprehension): 반복 가능한 객체(iterable)들을 축약한 형태으로 생성하는 방법
반복 가능한 객체(iterable) : 리스트(List), 튜플(Tuple), 집합(Set) 사전(Dict), 생성자(Generator) 등
"""
#%%
# list comprehension
L = [i ** 2 for i in range(10)]
print(L)

# list comprehension + if
L1 = [i ** 2 for i in range(10) if (i > 5)]
print(L1)

L2 = [i ** 2 for i in range(10) if (i > 5) and (i % 2 == 0)]
print(L2)

L3 = [i ** 2 if i < 5 else i for i in range(10)]
print(L3)
#%%
# multiple comprehension ★★★
L = [['a', 'b', 'c'], ['d', 'e', 'f']]

flatten = [j for i in L for j in i]  # L은 2차원 리스트로 구성되어 있어 1차원 리스트로 변환한다면 두 번의 반복문의 구성을 필요
print(flatten)

extend = [[j + j for j in i] for i in L]  # 차원을 그대로 유지한 상태로 값을 변경
print(extend)
#%%
# dictionary comprehension
text = "KIMCHULSHOO"

D = {i: text.count(i) for i in text}
print(D)

# 전처리 응용 예시
import pandas as pd
df = pd.DataFrame({'index':['송혜교','전지현','김태희'],0:[100,75,90],1:[75,25,30]})
df = df.set_index('index')

dict0 = {i+str(k):df[k][i] for i in df.index for k in df.columns}
df1 = pd.DataFrame([dict0])
#%%
# tuple comprehension
data = [0, 7, 6, 9, 2, 3]

T = tuple((i for i in data))
print(T)
#%%
# set comprehension
text = "KIMCHULSHOO"

S1 = set([i for i in text])  # list → set
print(S1)

S2 = {i for i in text}
print(S2)
#%%
