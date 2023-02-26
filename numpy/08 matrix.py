# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-numpy-8/, https://datascienceschool.net/, https://ko.wikipedia.org/wiki/%EB%B3%B5%EC%86%8C%EC%BC%A4%EB%A0%88
□ 기능: 행렬
□ 목적: 행렬 구조 복습
"""
#%%
# package
import numpy as np
#%%
# 배열과 행렬
# array
a = np.array([[10, 20, 30], [40, 50, 60]])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(a*b)

# matrix
c = np.array([[10, 20, 30], [40, 50, 60]]) # 2*3 행렬
d = np.array([[1, 2], [94, 95], [44, 65]]) # 3*2 행렬
mc = np.mat(c)
md = np.mat(d)

me = mc*md
print(mc*md) # 2*2 행렬
#%%
# 행렬구조 변환
a = np.array([[1, 2], [3, 4]])
d = np.array([[1, 3], [2, 4]])

b = np.array([[1-1j, 2-1j], [3, 4]])
c = np.array([[1, 3], [2, 4]])

ma = np.mat(a).T # 전치
md = np.mat(d).A # 행렬에서 배열로 변환

# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=fi1983&logNo=60150590775 : 공액복소수
mb = np.mat(b).H # 공액복소수의 전치
mc = np.mat(c).I # 곱의 역함수

print(ma)
print(mb)
print(mc)
print(md)
#%%
