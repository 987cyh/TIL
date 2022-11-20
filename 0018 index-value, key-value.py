# -*- coding: utf-8 -*-
"""
★ list 안에 중복되는 value의 index만 추출할 경우에는 filter 또는 dict을 활용

list: index-value
dict: key-value
"""
##############################
""" list """
list_a = ['AA','BB','BB','BB','CC']

# index를 통해서 value를 반환
value1 = list_a[3]

# value를 통해서 index를 반환, But 중복이 있을시 첫번째 index를 반환 ★
index1 = list_a.index("BB")
index1_1 = [list_a.index(k) for k in list_a if k == 'BB']

# filter 활용하면 dict과 같은 효과 ★
index1_2 = list(filter(lambda x: list_a[x] == 'BB', range(len(list_a))))

##############################
""" dict """
dict_a = {index: num for index, num in enumerate(list_a)}

# key를 통해서 value를 반환
value2_1 = dict_a.get(1)
value2_2 = dict_a.get(2)
value2_3 = dict_a.get(3)

# value를 통해서 key를 반환 ★
key1 = [k for k, v in dict_a.items() if v == 'BB']
##############################