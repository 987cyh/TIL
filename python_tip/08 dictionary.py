# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-12/, https://datascienceschool.net/
□ 기능 : dictionary
"""
#%%
a = {"one": 1, "two": 2, "three": 3}
b = dict.fromkeys(["one", "two", "three"], "life is cool")

print(a)
print(b)
#%%
# get
a = {"one": 1, "two": 2, "three": 3}

print(a["one"])
print(a.get("two"))
print(a.get("four", "4")) # value를 반환만 할뿐, raw dict은 불변
#%%
# 추가
a = {"one": 1, "two": 2, "three": 3}

a["four"] = 4  # 사전.setdefault(key, value)
print(a["four"])

a.update({"five": 5, "six": 6}) # 사전.update({'key':'value', 'key':'value'})
print(a)
#%%
# 수정
a = {"one": 1, "two": 2, "three": 3}

a["three"] = "삼"
a.update(two="이")

print(a)
#%%
# 갱신(+결합)
a = {"one": 1, "two": 2, "three": 3}
b = {"one": 2, "five": 5, "six": 6}

a.update(b)

print(a)
print(b)
#%%
# 삭제
a = {"one": 1, "two": 2, "three": 3}

del a["one"] # a.pop("one")
a.popitem() # 마지막 요소를 삭제
print(a)

a.clear()
print(a)
#%%
# 성질
a = {"one": 1, "two": 2, "three": 3}

print(a.items())
print(a.keys())
print(a.values())
print("one" in a)
print("four" not in a)
#%%
# fromkeys
a = ('one', 'two', 'three')

b = dict.fromkeys(a)
print(b)

c = dict.fromkeys(a, 10)
print(c)
#%%



