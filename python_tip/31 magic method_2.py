# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-36/
□ 기능 : magic method
□ 목적 : magic method 기능 정리 및 복습
"""
#%%
# 산술 연산 정의
class CYH:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + int(other)

    def __radd__(self, other):
        return self.value + other

    def __iadd__(self, other):
        return self.value + abs(other)


instance = CYH(6)
add = instance + 9.880401
radd = 9.880401 + instance
instance += -9.880401

print(add)
print(radd)
print(instance)
#%%
# 단항 연산 정의
class CYH:
    def __init__(self, value):
        self.value = value

    def __pos__(self):
        return self.value + 30

    def __neg__(self):
        return self.value - 30

    def __abs__(self):
        return -abs(self.value)

    def __invert__(self):
        return ~self.value


instance = CYH(10)
print(+instance)
print(-instance)
print(abs(instance))
print(~instance)
#%%
# 형식 변환 정의
class CYH:
    def __init__(self, value):
        self.value = value

    def __index__(self):
        return 2


L = ["A", "B", "C", "D", "E"]
instance = CYH(100)
print(L[instance])
#%%
