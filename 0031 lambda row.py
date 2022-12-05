# -*- coding: utf-8 -*-
"""
참고: https://m.post.naver.com/viewer/postView.naver?volumeNo=26810356&memberNo=18071586

□ df.apply(lambda row: (함)수식, axis=0)
axis=0 즉 행 방향으로 (함)수식을 적용한다. 행방향으로 수식을 적용하기 위해서 람다 수식 내 row는 0,1,2 열(컬럼)의 데이터를 차례로 처리한다.
당연한 얘기지만, 반환되는 값은 df의 열(컬럼)의 숫자와 동일하다.

□ df.apply(lambda row: (함)수식, axis=1)
axis=1 즉 열 방향으로 (함)수식을 적용한다. 열 방향으로 수식을 적용하기 위해서 람다 수식 내 row는 0,1 행(로우)의 데이터를 차례로 처리한다.
당연한 얘기지만, 반환되는 값은 df의 행의 숫자와 동일하다.

□ df.apply(lambda row: sum(row), axis=0)는 df.sum(axis=0)과 동일하다.
□ df.apply(lambda row: sum(row), axis=1)는 df.sum(axis=1)과 동일하다.
"""
#----------------------------------
import pandas as pd
#----------------------------------
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['a','b','c'])

# axis=0: 행(columns), axis=1 열(row)
df.apply(lambda row: sum(row), axis=0)
df.sum(axis=0)

df.apply(lambda row: sum(row), axis=1)
df.sum(axis=1)
#----------------------------------
cols = ['a', 'b', 'c']
df['combined_key'] = df[cols].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
#----------------------------------
