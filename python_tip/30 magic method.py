# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-35/
□ 기능 : magic method
□ 목적 : magic method 기능 정리 및 복습
"""
#%%
# 인스턴스(Instance) 정의
class CYH:
    def __new__(cls, *args, **kwargs):
        print("인스턴스 할당")
        return super(CYH, cls).__new__(cls)

    def __init__(self, site="987cyh"):
        print("인스턴스 초기화")
        self.site = site
        self.link = "github.com/" + site

    def __call__(self, protocol=True):
        print("인스턴스 호출")
        if protocol == True:
            return "https://" + self.link
        else:
            return "http://" + self.link

    def __del__(self):
        print("인스턴스 소멸")


instance = CYH()
print(instance.link)
print(instance(False))
del instance
#%%
# 인스턴스(Instance) 표현 방식
class CYH:
    def __init__(self, site="987cyh"):
        self.site = site
        self.link = "github.com/" + site

    def __repr__(self):
        return str({"site": self.site, "link": self.link})

    def __str__(self):
        return "CYH(site = " + self.site + ", link = " + self.link + ")"

    def __format__(self, format_spec):
        return format(self.link, format_spec)

    def __bytes__(self):
        return str.encode(self.link)


instance = CYH()
print(repr(instance))
print(str(instance))
print(format(instance, ">30"))
print(bytes(instance))
#%%