# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-4/, https://datascienceschool.net/
□ 기능 : 기초 연산
□ 목적 : 기초 연산 정리(복소수 표현 상기)
"""
#%%
# 대입 연산
A = B = C = 3
a, b = 1, 2
C += 1

print(A, B, C, a, b)
#-----------------------------
# 실수 표현
A = float(3)
B = int(3.2)
C = 3.5

print(A, B, C)
#-----------------------------
# 복소수 표현 ★★★
a = complex(3, 2)
b = a.conjugate()
c = 3 + 2j

print(a)
print(b)
print(c)
#%%