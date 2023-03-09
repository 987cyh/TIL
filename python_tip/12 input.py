# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-16/, https://datascienceschool.net/
□ 기능 : input
□ 목적 : input 기능 정리
"""
#%%
data = input("입력 : ")

answer = int(data) + 5
print(answer)
#%%
data = input("입력 (x,y,z) : ")  # 가, 나 , 다

L = data.split(',') # split은 str형식 가능, int 불가
x, y, z, = L[0], L[1], L[2]
print(x, y, z)

x, y, z = input("데이터 입력 (a,b,c) : ").split(',')
print(x, y, z)

data = '가, 나, 다'
x, y, z = data.split(',')
print(x, y, z)
#%%
