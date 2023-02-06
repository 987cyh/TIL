# -*- coding: utf-8 -*-
"""
□ 참고 : https://rfriend.tistory.com/459
□ 기능 : iterable
□ 활용 : 순환구조에서 INPUT LIST의 조건을 원하는 대로 가공하는 데 사용함
"""
#%%
from itertools import chain, repeat
#%%
numbers = [1, 2, 3]
n = 3
n_list = [3, 5, 7]

# list 안에 list
list(repeat(numbers, n))

# 단일 list안에 원소로
list(chain.from_iterable(repeat(numbers, n)))

# list comprehension을 통해서 개별원소를 횟수만큼 반복
list(chain.from_iterable((repeat(number, n) for number in numbers)))

# zip을 활용하여, 특정 횟수만큼 특정원소를 반복
list(chain.from_iterable((repeat(number, n) for (number, n) in zip(numbers, n_list))))
#%%
