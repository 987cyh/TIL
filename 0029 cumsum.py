# -*- coding: utf-8 -*-
"""
누적합을 구하는 함수: cunsum
객체간의 비교 연산: A.eq(B) / A==B
"""
#----------------------------------
import pandas as pd
#----------------------------------
data = [['김철수', '팀장'],
        ['김영희', '팀원'],
        ['이철수', '팀장'],
        ['이영희', '팀원'],
        ['이선희', '팀원'],
        ['박철수', '팀장'],
        ['박영희', '팀원']]

df = pd.DataFrame(data, columns=['이름', '구분'])

df['조'] = df['구분'].eq('팀장').cumsum()
df['조1'] = (df['구분'] == '팀장').cumsum()
#----------------------------------

