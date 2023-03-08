# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-5/, https://datascienceschool.net/
□ 기능 : 논리 연산
□ 목적 : 논리 연산(논리의 상수값을 활용하는 방법 상기)
"""
#%%
# 논리연산에서 T, F의 상수값
# False는 0, True는 1 → def로 분기문 만들 때, 반환값을 텍스트보다 0,1로 하는 것이 개발팀에서 편함
a = int(False)
b = float(True)

print(a)
print(b)
#%%
# 비교을 혼합한 논리연산(데이터 필터링 다중 조건)
x = True
a = (0>7) or (6>9)
b = (2>3) and (1>0)
c = not (1>0)
d = (4>3) and x

print(a)
print(b)
print(c)
print(d)
#%%
# 논리합
a = (7>3) or 0
b = (7<3) or 1 # 논리합(or)의 경우 앞의 조건이 참이면 뒤의 조건을 비교하지 않고 True를 반환
c = (7>3) and 2
d = (7<3) and 3

print(a)
print(b)
print(c)
print(d)
#%%
