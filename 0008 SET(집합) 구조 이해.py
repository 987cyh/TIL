# -*- coding: utf-8 -*-
"""
1. 집합구조는 중복을 허용하지 않고, 순서가 존재하지 않아서 인덱싱이 불가능하다.
2. {}의 형태이지만 dict() 구조와 가장 큰 차이는 key값이 없다는 것
3. list의 구조에서 uniuqe가 작동하지 않아서, 중복객체를 제거하는 데 활용
4. subset 활용
"""
###############################################################
#%%
str1 = 'value' # 문자
list1 = ['m','a','n','i','g','e','r'] # 리스트

# 교집합
set(str1).intersection(set(list1))
set(str1)&(set(list1))

# 교집합
set(str1).union(set(list1))
set(str1)|(set(list1))

# 차집합
set(str1).difference(set(list1))
set(str1)-(set(list1))

# 원소 변경
temp = set(str1)
temp.add('＠')

temp.update('.,c,o,m') # 개별 원소
temp.update(['.,c,o,m']) #리스트 자체가 하나의 원소

temp.remove('＠')

# 원소 포함여부
'@' in temp

# issubset
set(str1).issubset(temp)
set(str1)<=(temp)

# issuperset
temp.issuperset(set(str1))
temp>=set(str1)
###############################################################