# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-17/, https://datascienceschool.net/
□ 기능 : output
□ 목적 : output 기능 정리 / f-string
"""
#%%
# %표현식
a = 157.2

print ("정수형 출력 : %d" % a)
print ("실수형 출력 : %f" % a)
#%%
# 폭(들여쓰기) 설정
a = 10.0

print ("폭 설정 : %5d" % a)
print ("폭 설정 : %10d" % a)
#%%
# 소수점 표현 처리
a = 0.119825684

print ("정밀도 설정 : %.3f" % a)
print ("정밀도 설정 : %.5f" % a)
#%%
# %n.m를 입력하여 n 크기 만큼의 폭과 m 크기 만큼의 정밀도로 설정
a = 1234.56789

print ("폭&정밀도 설정 : %6.3f" % a)
print ("폭&정밀도 설정 : %13.5f" % a)
#%%
# format
a = 1
b = 2.0
c = "Python"
print("정수:{0}\n실수:{1}\n문자열:{2}".format(a,b,c))

L = ["1번", "2번", "3번"]
print ("L0 = {0[0]}\nL1 = {0[1]}".format(L))
#%%
""" f-string """
# f-string과 str
v = '송혜교'
print(f'{v}')
#------------------------------
# f-string과 리스트
n = [150, 250, 350]
print(f'list : {n[0]}, {n[1]}, {n[2]}')

for v in n:
    print(f'list with for : {v}')
#------------------------------
# f-string과 딕셔너리
d = {'성명': '송혜교', '성별': '남', '나이': 50}
result = f'my name {d["성명"]}, gender {d["성별"]}, age {d["나이"]}'
print(result)
#%%
