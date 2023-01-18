# -*- coding: utf-8 -*-
"""
□ replace, str.replace 비교
→ replace는 텍스트가 정확하게 일치하여야만 변환되나, str.replace의 경우에는 일부만 같아도 변경을 실시함
"""
#%%
import pandas as pd
import numpy as np
#%%
# dataframe 생성
d = {'이름': ['이병헌', '김태희','박서준', '송혜교'],'성별': ['남','여','남','여'], '국어점수': [70, 80, 50, 60], '수학점수': [80, 70, 55, 20]}
df = pd.DataFrame(data=d)
#%%
df.replace({'이름': {'병헌': '이름'}},inplace=True) # 코드는 실행되나 변경되지 않음
df.replace({'이름': {'이병헌': '이이름'}},inplace=True)
df = pd.DataFrame(data=d)
df['이름'] = df['이름'].apply(lambda x: '이이름' if '이병헌' in x else x)

df = pd.DataFrame(data=d)
df['이름'] = df['이름'].str.replace('병헌', '이름') # 부분 변경
#%%
