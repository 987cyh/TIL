# -*- coding: utf-8 -*-
"""
ㅁ 참고: https://blockdmask.tistory.com/536
ㅁ 목적: 학습

"""
#%%
import pandas as pd
import numpy as np
#%%
# 정수인지 확인
result1 = isinstance(100, int)
print(f'isinstance(100, int) : {result1}')
# 실수인지 확인
result2 = isinstance(100, float)
print(f'isinstance(100, float) : {result2}')
# 문자열인지 확인
result3 = isinstance('BlockDMask', str)
print(f'isinstance("BlockDMask", str) : {result3}')
# 리스트인지 확인
result4 = isinstance([1,2,3], list)
print(f'isinstance([1,2,3], list) : {result4}')

# 해당 클래스의 인스턴스인지 확인1
class School:
    pass
sc = School()
result5 = isinstance(sc, School)
print(f'isinstance(sc, School()) : {result5}')
# 해당 클래스의 인스턴스인지 확인2
class KimChi:
    pass
kc = KimChi()
result6 = isinstance(kc, School)
print(f'isinstance(kc, School) : {result6}')
#%%
# 정수, 실수, 문자열 중에 하나인가?
result1 = isinstance(100, (int, float, str))
print(f'isinstance(100, (int, float, str)) : {result1}')
# 정수, 실수, 리스트 중에 하나인가?
result2 = isinstance("blog", (int, float, list))
print(f'isinstance("blog", (int, float, list)) : {result2}')
#%%
# 부모 클래스
class Parent:
    pass
# 자식 클래스
class Child(Parent):
    pass
p = Parent()
c = Child()

# 각각 인스턴스인지 확인 (둘다 True)
result1 = isinstance(p, Parent)
result2 = isinstance(c, Child)
print(f'isinstance(부모 인스턴스, 부모 클래스) : {result1}')
print(f'isinstance(자식 인스턴스, 자식 클래스) : {result2}')
# 부모가 자식의 인스턴스인지 (False)
result3 = isinstance(p, Child)
print(f'isinstance(부모 인스턴스, 자식 클래스) : {result3}')
# 자식이 부모의 인스턴스인지 확인 (True)
result4 = isinstance(c, Parent)
print(f'isinstance(자식 인스턴스, 부모 클래스) : {result4}')
#%%
