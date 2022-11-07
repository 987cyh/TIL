# -*- coding: utf-8 -*-
"""
Q. iloc와 iat의 연산속도 비교

A. iat를 활용한 인덱싱이 속도의 효율성 측면에서 뛰어남, 이후 코드작성시에는 at, iat를 활용

iloc 9.1574 sec
iat 7.4710 sec
"""
#%%
import pandas as pd
import time
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)
pd.set_option('mode.chained_assignment',  None)
#####################################################
#%%
df = pd.read_excel('0001_df.xlsx')

# iloc
test = []
start = time.time()
for x in range(df.shape[0]):
    for y in range(df.shape[1]):
        test.append(df.iloc[x,y])
print(f"iloc {time.time()-start:.4f} sec")


# iat
test2 = []
start2 = time.time()
for x in range(df.shape[0]):
    for y in range(df.shape[1]):
        test2.append(df.iat[x,y])
print(f"iat {time.time()-start2:.4f} sec")
#####################################################