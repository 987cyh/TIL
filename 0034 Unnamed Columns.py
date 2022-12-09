# -*- coding: utf-8 -*-
"""
□ Unnamed Columns 처리
- 엑셀파일에서 셀병합 된 칼럼을 처리하기(MultiIndex → Index)

MultiIndex([('칼럼1', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2'),
            ('칼럼2', 'Unnamed: 1_level_1', 'Unnamed: 1_level_2'),
            ('칼럼3', 'Unnamed: 2_level_1', 'Unnamed: 2_level_2'),
            ('칼럼4', 'Unnamed: 3_level_1', 'Unnamed: 3_level_2')])

Index(['칼럼1', '칼럼2', '칼럼3', '칼럼4'], dtype='object')
"""
#--------------------------------------------------------
import pandas as pd

df = pd.read_excel('Unnamed col.xlsx', header=[0, 1, 2], dtype='str')
print(df.columns)

cols = list(map(lambda x: tuple(map(lambda y: '' if 'Unnamed' in y else y, x)), df.columns)) # Unnamed를 ''으로 변경
df.columns = list(map(lambda x: ''.join(x), cols)) # ''을 join으로 결합

print(df.columns)
#--------------------------------------------------------
