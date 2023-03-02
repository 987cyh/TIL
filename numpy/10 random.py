# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-numpy-10/, https://datascienceschool.net/
□ 기능: 난수 발생
□ 목적: 난수 발생 학습
"""
#%%
# package
import numpy as np
#%%
np.random.seed(12345)

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.random.choice(a, 5, replace=False, p=[0, 0, 0, 0, 0.05, 0.05, 0.05, 0.05, 0.8])
c = np.random.choice(a, 5, replace=True, p=[0, 0, 0, 0, 0.05, 0.05, 0.05, 0.05, 0.8]) # 중복허용

print(b)
print(c)
#%%
np.random.seed(12345)

a = np.random.rand(2, 2)                              # 다차원
b = np.random.randn(2, 2)                             # 표준정규분포
c = np.random.randint(1,100, (2, 2), dtype=int)        # 범위 사이의 정수값 반환

print(a)
print(b)
print(c)
#%%
np.random.seed(12345)

a = np.random.random((2, 3))
b = np.random.sample((2, 3))

print(a)
print(b)
#%%
np.random.seed(12345)

a = np.random.uniform(1, 2, (2, 2))     # 균일한 분포의 무작위 배열
b = np.random.lognormal(3, 1, (2, 2))   # 로그 정규 분포의 무작위 배열
c = np.random.laplace(0, 1, (2, 2))     # 라플라스 분포의 무작위 배열

print(a)
print(b)
print(c)
#%%
