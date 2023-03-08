# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-8/, https://datascienceschool.net/
□ 기능 : list 형태 변형
"""
#%%
a = [k for k in range(1, 30, 3)]
b = ["a", "a", "b", "c", "xyz", [1, 2, 3]]

print(len(a))
print(min(a))
print(max(a))

print(b.index([1, 2, 3])) # 인덱스 번호 반환
print(b[-1]) # 값 반환

print(b.count("a"))
print("a" in b)
#%%
# 값 직접 변경(대입)
a = [k for k in range(1, 50, 3)]
a[1] = 999
print(a)
#%%
# 삽입 : list.insert(index, value) → 인덱스 앞에 삽입
a = [k for k in range(10)]

a.insert(0, -1)
print(a)
a.insert(-1, 10)
print(a)

# 삽입 : 목록.append(value) → 마지막에 삽입
a = [k for k in range(10)]
b = [10, 11]

a.extend(b)
print(a)
#%%
# 삭제 : del 목록[start, end] → start부터 end-1까지의 원소를 삭제
a = [k for k in range(10)]
del a[1:-1]
print(a)
#%%
# 슬라이싱
a = [k for k in range(10)]
print(a)

a = a[:3]
print(a[1:])
print(a)
#%%
# 정렬
a = [1, 0, 2, 4, 3, 7, 9, 5]
a.sort()
print(a)

a = [1, 0, 2, 4, 3, 7, 9, 5]
a.sort(reverse=True)
print(a)

a = [1, 0, 2, 4, 3, 7, 9, 5]
a = sorted(a, reverse=True)
print(a)
#%%
