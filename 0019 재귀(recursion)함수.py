# -*- coding: utf-8 -*-
"""
참고: https://seongonion.tistory.com/24

■ 재귀(recursion): 함수가 자기 자신을 호출하는 재귀(순환)
→ 개념과 원리는 이해하였으나, 현재 업무에 어떻게 활용을 해야하는가는 고민이 필요
→ 기존에 코드를 작성하는 습관을 크게 바꾸게 해줄 수 있는 방법임
"""
##############################
# 팩토리얼 반복문

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
##############################
# 팩토리얼 재귀함수

def recursive_factorial(n):
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)
##############################
print(factorial(5))
print(recursive_factorial(5))
"""
1. 재귀함수를 쓸 때 중요한 것은, '부분계산'을 잘 찾아내는 것이다.
2. 예를 들어, 5!은 사실 5 * 4! 이다. 그리고 4! 또한 4 * 3! 이다.
3 .이것을 활용한 코드가 n * recursive_factorial(n-1) 이 되는 것이다.
4. 여기서 n이 0이거나 1일 때, 팩토리얼 0!, 1! 의 값은 모두 1이므로, 해당 부분만 return 값을 1로 처리해주면 되겠다.
"""
##############################