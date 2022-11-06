# -*- coding: utf-8 -*-

"https://velog.io/@mttw2820/List-Comprehension-%EB%AC%B8%EB%B2%95-%EC%A0%95%EB%A6%AC 참고"

#####################################################
#%%
n = 5
# n개의 0으로 초기화된 리스트
result = [0 for i in range(n)]  # [0, 0, 0, 0, 0]
# 0 ~ n으로 초기화된 리스트
result = [i for i in range(n)]  # [0, 1, 2, 3, 4]
# array 리스트의 값을 그대로 복사
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [n for n in array]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#####################################################
#%%
# array의 제곱값을 구하는 리스트
result = [n * n for n in array]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 문자열 리스트의 각 문자열의 길이를 저장하는 리스트
str_array = ["List", "Comprehension", "python"]
result = [len(string) for string in str_array]  # [4, 13, 6]
# 5로 나눈 나머지를 저장하는 리스트 - 함수 사용
def mod_5(number):
    return number % 5
result = [mod_5(n) for n in array]  # [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
#####################################################
#%%
# 범위 내 짝수만 저장하는 리스트
result = [ n for n in range(10) if n%2 == 0 ]   # [0, 2, 4, 6, 8]
# 범위 내 홀수만 저장하는 리스트
result = [ n for n in range(10) if n%2 != 0 ]   # [1, 3, 5, 7, 9]
# 배열에서 양수만 저장하는 리스트
array = [ -1, 0, -4, 24, 5, -10, 2 ]
result = [ n for n in array if n > 0 ]          # [24, 5, 2]
#####################################################
#%%
# 3의 배수 중 홀수만 저장하는 리스트
result = [ n for n in range(50) if n%3 == 0 if n%2 != 0 ]
# [3, 9, 15, 21, 27, 33, 39, 45]
result = [ n for n in range(50) if n%3 == 0 and n%2 != 0 ]
# [3, 9, 15, 21, 27, 33, 39, 45]
#####################################################
#%%
# 양수는 그대로, 음수는 0으로 저장하는 리스트
array = [ -1, 0, -4, 24, 5, -10, 2 ]
result = [ n if n>0 else 0 for n in array ]    # [0, 0, 0, 24, 5, 0, 2]
# 짝수라면 'even', 홀수라면 'odd'를 저장하는 리스트
array = [0, 1, 2, 3]
result = [ 'even' if n%2== 0 else 'odd' for n in array ]
# ['even', 'odd', 'even', 'odd']
#####################################################
#%%
# 중첩 for문
pos = []
for i in range(1, 4) :
    for j in range(1, 3) :
        pos.append(i*j)

pos = [ i*i for i in range(1, 4) for j in range(1, 3) ]  # [1, 2, 2, 4, 3, 6]
#####################################################
#%%
# 중첩 list comprehension으로 2차원 배열 만들기
result = [ [ 0 for i in range(2) ] for j in range(3) ]   # [ [0, 0], [0, 0], [0, 0] ]
#####################################################