# -*- coding: utf-8 -*-

"""
Q. index칼럼을 index로 활용한 후, 인덱스와 칼럼명을 결합한 값을 새로운 칼럼으로 가지는 df를 만들어 달라는 요청
A. pivot, concat 등을 검토하였으나, dictionary comprehension을 통한 dict 작성후, dict을 DataFrame으로 변경하는 것이 최선이라고 판단
"""
###############################################################
#%%
import pandas as pd
df = pd.DataFrame({'index':['supplyArea','exclusiveArea','numHouseholds'],0:[59,74,100],1:[84,115,300]})
df = df.set_index('index')

dict0 = {i+str(k):df[k][i] for i in df.index for k in df.columns}
df1 = pd.DataFrame([dict0])
###############################################################