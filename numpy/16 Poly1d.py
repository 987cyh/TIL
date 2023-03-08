# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-numpy-16/, https://datascienceschool.net/
□ 기능 : poly1d(다항식)
□ 학습 : poly1d(다항식) 관련 기능 학습
"""
#%%
# package
import numpy as np
#%%
# 다항식 생성
equation1 = np.poly1d([1, 2], True, variable='a')
equation2 = np.poly1d([1, 2], True)
equation3 = np.poly1d([1, 2], False)

print(equation1)
print(equation2)
print(equation3)
#%%
# 다항식 속성
equation = np.poly1d([1, 2], True)
print(equation.c, equation.coef, equation.coefficients)
print(equation.o, equation.order)
print(equation.r, equation.roots)
print(equation.variable)
#%%
# 다항식 근 계산
p = np.poly1d([1, 10])
equation1 = np.roots(p)
equation2 = np.roots([1, 10])

print(equation1)
print(equation2)
#%%
# 다항식 계수 계산
p = np.poly1d([1, -6, 8])
equation1 = np.poly(p)
equation2 = np.poly([1, -6, 8])

print(equation1)
print(equation2)
#%%
# 다항식 계산
p = np.poly1d([1, -6, 8])
x = 5
equation1 = np.polyval(p, x)
equation2 = np.polyval([1, -6, 8], np.poly1d([x, x]))

print(equation1)
print(equation2)
#%%
# 다항식 사칙연산
p1 = np.poly([1, -1])
p2 = np.poly1d([1, 0, 1])
add = np.polyadd(p1, p2)

print(p1)
print(p2)
print(add)
#%%
# 다항식 적분
p = np.poly1d([3, 2, 1])
integral = np.polyint(p, m = 1, k = 99)

print(p)
print(integral)
#%%
다항식 미분
p = np.poly1d([3, 2, 1])
differential = np.polyder(p, m = 1)

print(p)
print(differential)
#%%