# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-37/
□ 기능 : attribute
□ 목적 : attribute 기능 정리 및 복습
"""
#%%
# 속성 변경
class CYH:

    class_value = 0

    def __init__(self):
        self.instance_value = 0

    def set_class_value(self):
        CYH.class_value = 10

    def set_instance_value(self):
        self.class_value = 20

instance1 = CYH()
instance2 = CYH()

print("--클래스 속성 변경--")
instance1.set_class_value()
print(instance1.class_value, instance2.class_value)

print("--인스턴스 속성 변경--")
instance1.set_instance_value()
print(instance1.class_value, instance2.class_value)

print("--속성(Attribute) 출력--")
print(instance1.__dict__)
print(instance2.__dict__)
#%%
# __getattr__ : 존재하지 않는 속성 호출
class CYH:
    def __init__(self):
        self.value = 0

    def __getattr__(self, name):
        return name + "은 존재하지 않습니다."

instance = CYH()
print(instance.value)
print(instance.nothing)
#%%
# __getattribute__ : 속성 호출
class CYH:
    def __init__(self):
        self.value = 0

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)

        except AttributeError:
            value = "Empty"
            setattr(self, name, value)
            return value

instance = CYH()
print(instance.value)
print(instance.nothing)
#%%
# __setattr__ : 속성 할당
class CYH:
    def __init__(self):
        self.value = 0

    def __setattr__(self, name, value):
        return super().__setattr__(name, value * 2)

instance = CYH()
instance.value = 10
instance.nothing = 30
print(instance.value)
print(instance.nothing)
#%%
# __delattr__ : 속성 제거
class CYH:
    def __init__(self):
        self.value = 0

    def __delattr__(self, name):
        print("제거 :", name)
        return super().__delattr__(name)

instance = CYH()
del instance.value
#%%
# __slots__ : 속성 제한, __dir__ : 속성 보기
class CYH:

    __slots__ = ["value"]

    def __init__(self):
        self.value = 0

    def __dir__(self):
        return sorted(super().__dir__(), key=str.upper)

instance = CYH()
print(instance.__slots__)
print(instance.__dir__())
#%%