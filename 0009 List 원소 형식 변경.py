# -*- coding: utf-8 -*-

"""
TypeError: 'list' object is not callable의 발생원인, list=[]로 선언하여, list내장함수를 대체하여 오류발생하였음
"""
#%%
#####################################################
str = '12345'

# 문자를 list안에 쪼개서 담기
list_str = list(str)
list_str = [k for k in str]

# 문자를 list안에 쪼개서 담기(형식 int)
list_int = [int(k) for k in str]
list_int = list(map(int, list_str)) #리스트 원소 형식 변경
#####################################################