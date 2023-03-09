# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-13/, https://datascienceschool.net/
□ 기능 : set : 중복 불가, 순서 무관
"""
#%%
a = {1, 2, 3}
b = {1, 3, 5, 7, 9}

print(a)
print(b)
#%%
# 원소 추가
a = {1, 2, 3}
b = {1, 3, 5, 7, 9}

a.add(4)
b.add(11)

print(a)
print(b)
#%%
# 원소 삭제()
a = {1, 2, 3}
b = {1, 3, 5, 7, 9}

a.discard(3)
b.discard(7)

print(a)
print(b)
#%%
# list to set
L = [k for k in range(1,10,2)]

a = set(L)
print(a)
#%%
# 합집합(union)
a = {1, 2, 3}
b = {1, 3, 5, 7, 9}

c = a | b
d = a.union(b)

print(c)
print(d)
#-------------------
# 교집합(intersection)
a = {1, 2, 3}
b = {1, 3, 5, 7, 9}

c = a & b
d = a.intersection(b)

print(c)
print(d)
#-------------------
# 차집합(difference of sets)
a = {1, 2, 3}
b = {1, 3, 5, 7, 9}

c = a - b
d = b - a

print(c)
print(d)
#%%
