# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-24/
□ 기능 : zip
□ 목적 : zip 기능 정리
"""
#%%
# zip 함수 생성
a = "RISE"
b = [1, 2, 3]
c = ("일", "이", "삼")

print(list(zip(a, b, c)))
print(set(zip(a, b, c)))
print(dict(zip(a, b)))
#%%
# for 반복문
L1 = ["A", "B", "C", "D"]
L2 = ["가", "나", "다", "라"]
L3 = [k for k in range(4)]

for i, j, t in zip(L1, L2, L3):
    print(i, j, t)
#%%
# 언패킹(Unpacking) / 패킹(Packing)
numbers = [[1, 2, 3], [4, 5, 6]]

print(*numbers)
print(list(zip(*numbers)))
print(list(zip([1, 2, 3], [4, 5, 6])))
#%%
