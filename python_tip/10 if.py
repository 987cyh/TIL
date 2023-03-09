# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-14/, https://datascienceschool.net/
□ 기능 : if 조건문(분기)
□ 정리 : 수제 모듈을 작성 할 때, if 조건문이 많아지면 분기가 많아지고 이해하기 어려운 코드로 작성되어, 알고리즘 고민 필요
"""
#%%
a = 700
if a > 700:
    print("크다")
elif a == 700:
    print("같다")
else:
    print("작다")
#------------------------------------------
a = 100
b = 40

if (100 <= a < 130) and not (50 < a < 100):
    print("if-1 : 모두 조건에 만족")

if a < 50 or (b - 40) == 0:
    print("if-2 : 하나라도 만족")

if b > 0 or b > 0 and a < 50:
    print("if-3 : 조건 우선식")
#%%
# tuple을 활용한 조건문
a = 5
if a > 5:
    a = a*2
    print(a)
else:
    a = a-4
    print(a)

a = 5
b = (a-4, a*2)[a > 5]  # (거짓, 참)[조건]
print(b)
#%%
# dictionary를 활용한 조건문
a = 5
if a == 1:
    print("일")
elif a == 2:
    print("이")
elif a == 3:
    print("삼")
else:
    print("알 수 없음")

a = 5
data = {1 : "일", 2 : "이", 3 : "삼"}
b = data.get(a, "알 수 없음")  # 사전.get(key, 예외)
print(b)
#%%
# 삼항연산자(if 조건문 한줄 작성)
a = 10
if a > 10:
    a = a * 2
    print(a)
else:
    a = a - 4
    print(a)

a = 10
b = a * 2 if a > 10 else a - 4  # (참 값) if (조건) else (거짓 값)
print(b)
#%%
