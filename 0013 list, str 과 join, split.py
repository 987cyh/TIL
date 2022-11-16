# -*- coding: utf-8 -*-
"""
list, str 과 join, split
"""
###############################################################
list_a = ['큰', '가', '치', '빅', '밸', '류']

# 리스트를 구분자를 활용해서 단일 str로 만듬
text_string1 = "/".join(list_a)
text_string2 = "|".join(list_a)
text_string3 = "\n".join(list_a)

# 단일 str을 인덱스의 단위 및 구분자를 기준으로 리스트의 요소로 변환시켜줌
list_b = text_string1.split("/")

list_c = list(text_string1.replace('/',''))
###############################################################