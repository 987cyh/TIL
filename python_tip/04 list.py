# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-8/, https://datascienceschool.net/
□ 기능 : list
"""
#%%
# 이어 붙이기
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
d = a + [9]

print(c)
print(d)
#-----------------------------
# 반복
a = [1, 2, 3]

print(a * 2)
#-----------------------------
# 인덱싱

c = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(c[0])
print(c[1])
print(c[2])
print(c[-1])
print(c[0:1])
print(c[0:-1])
print(c[0:-1:2]) # 목록[start:end:interval]
#-----------------------------
# 포함
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

print(c)
#%%
