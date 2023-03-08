# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-7/, https://datascienceschool.net/, https://blockdmask.tistory.com/529
□ 기능 : math
□ 목적 : math package 일부 리뷰
"""
#%%
from math import *
#%%
# 표현함수
a = 3.141592
b = -1.61254
ceil(a)   # 올림
floor(a)  # 내림
trunc(a)  # 절사
round(a,0) # 반올림

ceil(b)   # 올림
floor(b)  # 내림
trunc(b)  # 절사
round(b,0) # 반올림

print(pow(5, 2))
print(sqrt(5))
#%%
# 파이, 라디안
a = math.pi  # 원주율 파이 상수
b = math.radians(360)  # 360도를 라디안 표기법으로
c = math.degrees(2 * math.pi)  # 2파이 라디안을 degree 표기법으로

print(f"math.pi : {a}")
print(f"math.radians(360) : {b}")
print(f"math.degrees(2 * math.pi) : {c}")
#-------------------------------------------------------------
degrees = [0, 30, 45, 60, 90] # 0, π/6, π/4, π/3, π/2

print("degree\tsin(x)\tcos(x)\ttan(x)")
print("=" * 40)

for val in degrees:
    a = math.sin(math.pi * (val / 180))
    b = math.cos(math.pi * (val / 180))
    c = math.tan(math.pi * (val / 180))
    print(f"{val:2d}\t{a:.4f}\t{b:.4f}\t{c:.4f}")
#%%
# 로그함수
print(math.e)
print(math.log(math.e)) # log(x, base=e) 밑이 e 혹은 base 값인 로그, 기본값은 e인 자연로그

print(math.log(1))
print(math.log(10))
print(math.log10(100000))
print(math.log2(1024))
#%%
# 지수함수
print(math.exp(2))
print(math.exp(2) == math.e**2) # False
#%%
# 상수
print(e) # e
print(pi) # π
print(tau) # 원주율 τ
print(inf) # ∞
print(nan) # Not a Number
#%%