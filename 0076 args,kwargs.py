# -*- coding: utf-8 -*-
"""
□ 참고 : https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs
        https://codechacha.com/ko/python-difference-between-args-kwargs/, https://security-nanglam.tistory.com/427
ㅁ 기능: *args, **kwargs / Tuple, Dict(Key, Value)
        input으로 list, dict구조를 활용하여 def 작성하기 → 업무에 활용
"""
#%%
import pandas as pd
import numpy as np
#%%
string_list = ['A','B','C']
int_list = [1, 2, 3]
dictionary = dict(zip(string_list, int_list))
#%%
def print_everything(*args):
    for count, thing in enumerate(args):
    print('{0}. {1}'.format(count, thing))
print_everything('apple', 'banana', 'cabbage')

print_everything(*string_list)
print_everything(*int_list)

def table_things(**kwargs):
    for name, value in kwargs.items():
    print('{0} = {1}'.format(name, value))
table_things(apple = 'fruit', cabbage = 'vegetable')

table_things(**dictionary)
#%%
def myFun(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"key = {key}, value = {value}")

myFun('This', 'is', 'an example', arg1 ='Hello', arg2 ='World', arg3='Python')

myFun(*string_list,**dictionary)
myFun(*int_list,**dictionary)
#%%
