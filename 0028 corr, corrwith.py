# -*- coding: utf-8 -*-
"""
참고: https://wikidocs.net/157461

#----------------------------------
df.corr(method='pearson', min_periods=1)
method : {pearson / kendall / spearman} 적용할 상관계수 방식입니다.
min_periods : 유효한 결과를 얻기위한 최소 값의 수 입니다. (피어슨, 스피어먼만 사용가능) ★★★
#----------------------------------
df.corrwith(other, axis=0, drop=False, method='pearson')
other : 동일한 이름의 행/열을 비교할 다른 객체입니다.
axis : {0 : index / 1 : columns} 비교할 축 입니다. 기본적으로 0으로 인덱스끼리 비교합니다.
drop : 동일한 이름의 행/열이 없을경우 NaN을 출력하는데, 이를 출력하지 않을지 여부입니다.
method : {pearson / kendall / spearman} 적용할 상관계수 방식입니다.
#----------------------------------
"""
#----------------------------------
import pandas as pd
#----------------------------------
col1 = [1,2,3,4,5,6]
col2 = [1,4,2,8,16,32]
col3 = [6,5,4,3,2,1]
data = {"col1":col1,"col2":col2,"col3":col3}
df = pd.DataFrame(data)
print(df)
#----------------------------------
""" df.corr """
# 피어슨 상관계수
print(df.corr(method='pearson'))

# 켄달-타우 상관계수
print(df.corr(method='kendall'))

# 스피어먼 상관계수
print(df.corr(method='spearman'))
#----------------------------------
data1 = {"col1":[1,2,3,4,5,6],"col2":[1,4,2,8,16,32]}
data2 = {"col1":[6,5,4,3,2,1],"col3":[3,6,1,2,5,9]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
#----------------------------------
""" df.corrwith """
# 피어슨 상관계수
print(df1.corrwith(other = df2, method='pearson'))
print(df1.corrwith(other = df2, method='pearson', drop = True))

# 켄달-타우 상관계수
print(df1.corrwith(other = df2, method='kendall'))
print(df1.corrwith(other = df2, method='kendall', drop = True))

# 스피어먼 상관계수
print(df1.corrwith(other = df2, method='spearman'))
print(df1.corrwith(other = df2, method='spearman', drop = True))
#----------------------------------