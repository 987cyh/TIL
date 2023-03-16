# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-40/
□ 기능 : closure
□ 목적 : closure 기능 정리 및 복습
"""
#%%
# closure
def outer_func(x):

    total = x

    def inner_func(y):
        return total + y

    return inner_func


main = outer_func(1)
sub1 = main(2)
sub2 = main(3)
sub3 = main(4)
print(sub1, sub2, sub3)
#%%
# local variable : 지역변수 '참조'
def outer_func():
    value = 0

    def inner_func():
        value = 100

    inner_func()
    return value


func = outer_func()
print(func)
#------------------------------------------
def outer_func():
    value = 0

    def inner_func():
        nonlocal value
        value = 100

    inner_func()
    return value


func = outer_func()
print(func)
#%%
# local variable : 지역변수 '변경'
def outer_func():
    var = list()

    def inner_func(value):
        var.append(value)
        return var

    return inner_func


main = outer_func()
result = main({"A": 57})
print(result)
result = main({"B": 24})
print(result)
#%%
# free variable, cell
def outer_func():
    var = list()

    def inner_func(value):
        var.append(value)
        return var

    return inner_func


main = outer_func()
result = main({"A": 150})
result = main({"B": 37})
print(main.__closure__)
print(type(main.__closure__), len(main.__closure__))
print(main.__closure__[0].cell_contents)
#%%
