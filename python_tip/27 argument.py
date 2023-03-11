# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-32/
□ 기능 : argument [ *args(Tuple), **kwargs(Dictionary) ]
□ 목적 : argument [ *args(Tuple), **kwargs(Dictionary) ] 기능 정리 및 복습
"""
#%%
# *args(Tuple)
def func(*args):
    print("Type:", type(args))
    print("Lenght:", len(args))
    print(args)

func([1, 2], 3, 4, (5))
#%%
# **kwargs(Dictionary)
def func(**kwargs):
    print("Type:", type(kwargs))
    print("Lenght:", len(kwargs))
    print(kwargs)

func(a=1, b=2, c=3)
#%%
# *args(Tuple) + **kwargs(Dictionary)
def func(*data, **method):
    num = sum(data) * method["scale"]
    print(num, method["unit"] + "입니다.")

func(3, 4, 5, scale=10, unit="개")
#--------------------------------------------------
def func(*data, message, **method):
    print(message)

    num = sum(data) * method["scale"]
    print(num, method["unit"] + "입니다.")

func(3, 4, 5, message="계산된 값입니다.", scale=10, unit="개")
#--------------------------------------------------
def func(message1, message2, *data, **method):
    print(message1)
    print(message2)

    num = sum(data) * method["scale"]
    print(num, method["unit"] + "입니다.")

func("계산된 값입니다.", "값이 10배 커집니다.", 3, 4, 5, scale=10, unit="개")
#%%
