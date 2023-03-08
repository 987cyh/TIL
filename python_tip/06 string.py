# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-10/, https://datascienceschool.net/
□ 기능 : string
"""
#%%
a = 'Study python'
b = "I'm a data scientist."
c = "I\'m a data scientist."
d = "data\nscientist"

print(a)
print(b)
print(c)
print(d)
#%%
a = "sci"
b = "ent"
c = "ist?!"

print(a + b)
print(a * 2)
print(a[-1])
print(b[0:1])
print(c[0:-1:2]) # 문자열[start:end:step]
#%%
# 정규표현식 및 조건문에 활용
a = "%d %f %e" % (10, 10, 10) # 정수 / 실수 / 지수
b = "%o %x" % (8, 16) # 8진법 / 16진법
c = "%c %s" % ("I", "I'm a data scientist") # 문자 / 문자열

print(a)
print(b)
print(c)
#%%
# PK와 같은 ID를 입력으로 받을 시에 활용함
a = "abcdefg"
b = "ABCDEFG"

print(a.upper())
print(a.lower())
#%%
# 공백제거
a = "   가   나   요   "

print(a.strip())
print(a.rstrip())
print(a.lstrip())

print(a.replace(' ',''))
#%%
# find vs index
a = "I'm a data scientist"
print(a.find('a'))
print(a.index('a'))
print(a.count('a'))

print(a.find('k')) # 없으면 -1 return
print(a.index('k')) # 없으면 ValueError
#%%
# 변환
a = "I'm a data scientist"
b = "_"
c =['가','나','다']

print(a.split())
print(a.replace("scientist", "scientist(junior)"))

print(b.startswith('/'))
print(b.join(a))

print('-'.join(c))
#%%



