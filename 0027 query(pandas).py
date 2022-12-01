# -*- coding: utf-8 -*-
"""
참고: # https://m.blog.naver.com/wideeyed/221867273249

■ query 조건 필터링
"""
#----------------------------------
import pandas as pd
#----------------------------------
df = pd.DataFrame({'id':[10,20,30], 'korean':[98,24,95], 'math':[54,84,20], 'english':[85,22,48]})

# ① 비교 연산자( ==, >, >=, <, <=, != )
condition = 'korean !=98'
df.query(condition)

# ② in 연산자( in, ==, not in, != )
# in과 ==는 같고, not in과 !=는 같음
list = [10,20]

condition = 'id not in [10,20]'
condition = 'id not in list'
df.query(condition)

# ③ 논리 연산자(and, or, not)
condition = '(korean>=50) and (english<=50)'
df.query(condition)

# ④ 외부 변수(또는 함수) 참조 연산
num1 = 50
num2 = 40
condition = '(korean>=@num1) and (math<=@num2)'
df.query(condition)

# f-string
num1 = 50
num2 = 40
condition = f'(korean>={num1}) and (math<={num2})'
df.query(condition)

# ⑤ 외부 변수(또는 함수) 참조 연산 ★★
def my_max(x, y):
    return max(x,y)
condition = 'korean>=@my_max(1,50)'
df.query(condition)

# ⑥ 인덱스 검색 ★
condition = 'index<2'
df.query(condition)

# ⑦ 문자열 부분검색( str.contains, str.startswith, str.endswith ) ★
df1 = pd.DataFrame({"name": ["White bear", "Bear black", "Red bear"], "age": [25, 37, 29]})
condition = "name.str.contains('bear')" # 조건 안의 문자"",''
df1.query(condition)

condition = "name.str.contains('bear', case=False)" # 대소문자 미구분
df1.query(condition)
#----------------------------------