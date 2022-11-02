# -*- coding: utf-8 -*-
"""
Q. df의 칼럼안에 값을 원하는 항목으로 변환시, replace, lambda, list comprehesion의 연산속도 비교
→ replce와 list comprehesion은 dict을 활용하여 비교하였음

A. 0.5초 미만의 결과가 모두 도출(속도에서 큰차이가 없음), 이에 타인이 직관적으로 가장 이해하기 쉬운 replace가 가장 적합하다고 판단

replace 0.1007 sec
lambda 0.0867 sec
list comprehesion 0.4237 sec
"""
#####################################################
import pandas as pd
import time
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)
pd.set_option('mode.chained_assignment',  None)
#####################################################
import os
os.getcwd()
df = pd.read_excel('0001_df.xlsx')

ret_tmp = df.copy()
ret_tmp1 = df.copy()
ret_tmp2 = df.copy()
#####################################################
bank_dict = {'KEB하나':'하나', 'ＫＥＢ하나':'하나', 'ＫＢ국민':'국민', 'KB국민카드':'KB국민카드','국민은행':'국민', '우리은행':'우리','ＮＨ농협은행':'농협은행', '농협':'농협은행'}

start = time.time()
for key in bank_dict.keys():
    ret_tmp1['은행구분'] = [bank_dict[key] if x == key else x for x in ret_tmp1['은행구분']]
print(f"list comprehesion {time.time()-start:.4f} sec")

start2 = time.time()
ret_tmp['은행구분'] = ret_tmp['은행구분'].replace(bank_dict)
print(f"replace {time.time()-start2:.4f} sec")

start3 = time.time()
ret_tmp2['은행구분'] = ret_tmp2['은행구분'].apply(lambda x: '하나' if x == 'KEB하나' else '하나' if x == 'ＫＥＢ하나' else '국민' if x == 'ＫＢ국민' else '국민' if x == '국민은행' else '우리' if x == '우리은행' else '농협은행' if x == 'ＮＨ농협은행' else '농협은행' if x == '농협' else x)
print(f"lambda {time.time()-start3:.4f} sec")
#####################################################