# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-15/, https://datascienceschool.net/
□ 기능 : for, while
□ 목적 : for, while 기능 정리
"""
#%%
# for
L = ["일","이","삼"]
T = (1, 2, 3)
S = "송혜교"
total = 0

for i in L:
    print(i)
for i in T:
    print(i)
for i in S:
    print(i)
for i in range(1,10):
    total += i
print(total)
#--------------------------------
# for - else
for i in range(5):
    print("i =", i)
else:
    print("FIN")

for j in range(5):
    if j == 2:
        break
    print("j =", j)
else:
    print("FIN")
#--------------------------------
# while
L = ["일", "이", "삼"]
T = (1, 2, 3)
S = "송혜교"
total = 0

i = 0
while i < len(L):
    print(L[i])
    i += 1

i = 0
while i < len(T):
    print(T[i])
    i += 1

i = 0
while i < len(S):
    print(S[i])
    i += 1

i = 0
while i < 10:
    total += i
    i += 1
print(total)
#%%
""" continue & break """
# for
for i in range(5):
    if i == 3:
        break
    print(i)
print("break")

for i in range(5):
    if i == 3:
        continue
    print(i)
print("continue")

# while
i = 0
while i < 5:
    i += 1
    if i == 3: break
    print(i)
print("break")

i = 0
while i < 5:
    i += 1
    if i == 3: continue
    print(i)
print("continue")
#%%
