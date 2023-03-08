# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-10/, https://datascienceschool.net/
□ 기능 : tuple : 변경이 불가하고 순서를 중요시
"""
#%%
a = (100, 200, 300, 400, 500)
b = (600,)
c = tuple("123")
d = tuple([k for k in range(1, 30, 3)])

print(a)
print(b)
print(c)
print(d)
#%%
a = (100, 200, 300, 400, 500)

print(a[0:-1:2])
#%%
a = (100, 200, 300, 400 ,500)

print(len(a))
print(max(a))
print(min(a))
print(a.index(3))
print(a.count(1))
print(6 in a)
#%%