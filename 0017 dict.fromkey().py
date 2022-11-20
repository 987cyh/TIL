# -*- coding: utf-8 -*-
"""
dict.fromkey(), set()의 차이 → list 내 중복객체 제거시
"""
##############################
#%%
str = 'We are the world'
value = 'hi'
# str 내 중복된 문자은 삭제함(set과 유사하나, index 순서를 유지함)
list_key = list(dict.fromkeys(str,value).keys())
list_value = list(dict.fromkeys(str,value).values())

print(''.join(list_key))
print(''.join(list_value))
##############################
# key만 활용
test = {key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()}
# value를 key로 사용
test1 = {value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()}
# key와 value의 위치를 변경함
test2 = {value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()}
##############################
# dict, if문 활용
test3 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
test4 = {key: value for key, value in test3.items() if value >= 25}
##############################