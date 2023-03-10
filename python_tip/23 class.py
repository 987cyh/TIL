# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-27/
□ 기능 : class, inheritance
□ 목적 : class, inheritance 기능 정리
"""
#%%
# 클래스(class)
class Human:
    def __init__(self):
        self.name = "알 수 없음"
        self.age = 70

    def man(self, name, age=40):
        self.name = name
        self.age = age

    def woman(self, name, age):
        self.name = name
        self.age = age

    def prt(self):
        print("이름은 " + self.name + "이고, 나이는 " + str(self.age))

#--------------------------------------------------------------------------
a = Human()
a.man("송혜교")

b = Human()
b.woman("김태희", 42)

c = Human()

a.prt()
b.prt()
print(vars(c))
#%%
# 상속(inheritance)
class Human:
    def __init__(self):
        self.name = "알 수 없음"
        self.age = 50

    def set_name(self, name):
        self.name = name
        print("Human Class")

    def set_age(self, age):
        self.age = age


class Man(Human):
    def set_name(self, name):
        if "XX" in name:
            self.name = name.replace("XX", " 모 씨")
            print("Man Class")

    def prt(self):
        print("이름은 " + self.name + "이고, 나이는 " + str(self.age))

#--------------------------------------------------------------------------
a = Man()
a.set_name("이XX")
a.prt()

a.set_name("전지현")
a.prt()
#%%