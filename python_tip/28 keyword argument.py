# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-33/
□ 기능 : keyword Argument
□ 목적 : keyword Argument 기능 정리 및 복습
"""
#%%
def func(name, *, value1, value2):
    total = value1 + value2
    print(name + "는", total, "입니다.")

func("Plus", value1=2, value2=3)
#%%
def func(name, *, value1, value2=3, value3):
    total = value1 + value2 + value3
    print(name + "는", total, "입니다.")


func("Plus", value3=2, value1=3)
#%%
