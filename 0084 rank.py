# -*- coding: utf-8 -*-
"""
□ 참고 : https://wikidocs.net/151895
□ 기능: 순위 (rank)
"""
#%%
import pandas as pd
import numpy as np
data = [[5],[5],[pd.NA],[3],[-3.1],[5],[0.4],[6.7],[3]]
row = ['A★','B★','C','D☆','E','F★','G','H','I☆']
df = pd.DataFrame(data=data, index=row, columns=['Value'])
print(df)
#%%
"""
ㅁ method에 따른 차이 → 동순위 처리

average : D와 I의 경우 각각 3등 4등이기때문에 3.5 출력
min : A, B, F의 경우 각각 5등 6등 7등으로 가장 낮은등수인 5 출력
max : A, B, F의 경우 각각 5등 6등 7등으로 가장 높등수인 7 출력
first : 동점일경우 위에서부터 매김 D와 I 각각 3등 4등
dense : min처럼 동작하지만 등수가 순차적으로 증가
"""
df['average']=df['Value'].rank(method='average')
df['min']=df['Value'].rank(method='min')
df['max']=df['Value'].rank(method='max')
df['first']=df['Value'].rank(method='first')
df['dense']=df['Value'].rank(method='dense')
print(df)
#%%
"""
ㅁ na_option에 따른 차이 → NaN값의 처리

keep : Na요소에 NaN을 부여하여 그대로 둡니다.
top : Na에게 가장 높은 순위를 부여합니다. 1등이 된것을 볼 수 있습니다.
bottom : Na에게 가장 낮은 순위를 부여합니다. 9등이 된것을 볼 수 있습니다.
pct : True일 경우 백분위수로 표시합니다.
"""
df['keep']=df['Value'].rank(na_option='keep')
df['top']=df['Value'].rank(na_option='top')
df['bottom']=df['Value'].rank(na_option='bottom')
df['pct']=df['Value'].rank(pct=True)
print(df)
#%%
