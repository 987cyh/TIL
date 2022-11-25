# -*- coding: utf-8 -*-
"""
참고: https://wayhome25.github.io/cs/2017/04/15/cs-16/

■ 데이터가 오름차순으로 정렬된 list에서 찾고자하는 값을 찾는 탐색 방법

"""
##############################
""" 바이너리 서치 구현 (python) """
# 바이너리 서치
# data 중에서 target 을 검색하여 index 값을 return 한다.
# 없으면 None을 return한다.

def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None

# 테스트용 코드
if __name__ == "__main__":
  li = [i**2 for i in range(11)]
  target = 9
  idx = binary_search(target, li)

  if idx:
      print(li[idx])
  else:
      print("찾으시는 타겟 {}가 없습니다".format(target))

##############################
# 재귀(recursion): 함수가 자기 자신을 호출하는 재귀(순환)
""" 바이너리 서치 재귀적 구현 (python)"""

# data는 오름차순으로 정렬된 리스트
def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search_recursion(target, start, end, data)

# 테스트용 코드
if __name__ == '__main__':
    li = [i*3 for i in range(11)]
    target = 6
    idx = binary_search_recursion(target, 0, 10, li)

    print(li)
    print(idx)
##############################