# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-38/
□ 기능 : property
□ 목적 : property 기능 정리 및 복습
"""
#%%
# Private & Property
class CYH:
    def __init__(self):
        self.__value = 0.123456789

    @property
    def value(self):
        return self.__value


instance = CYH()
print(instance.value)
#%%
# Getter & Setter & Deleter
class CYH:
    def __init__(self):
        self.__value = 0.123456789

    @property
    def value(self):
        pass

    @value.getter
    def value(self):
        print("GET")
        return self.__value

    @value.setter
    def value(self, value):
        print("SET")
        self.__value = value

    @value.deleter
    def value(self):
        print("DEL")
        del self.__value


instance = CYH()
instance.value = 750
print(instance.value)
del instance.value
#%%
