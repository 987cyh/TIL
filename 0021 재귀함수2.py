# -*- coding: utf-8 -*-
"""
참고: https://mannahjjang.tistory.com/17

■ 재귀, 꼬리재귀, while
- 재귀: 계산한 결과에다 더할 수를 기억 -> 재귀 호출의 횟수만큼 저장 공간을 사용 / 실행 논리를 직관적으로 표현 가능 BUT, 공간 효율이 떨어짐
- 꼬리재귀: 더 이상 기억해둘 것이 없음 (답을 누적) -> 공간이 필요 없음 (공간 절약)
- while: 꼬리 재귀 or while 루프같은 상향식은 공간 절약 가능
"""
##############################
# 재귀
def sumrange(m,n):
    if m <= n:
        return m + sumrange(m+1, n)
    else:
        return 0

# 꼬리재귀
def sumrange(m, n):
    def loop(m, total):
        if m <= n:
            return loop(m + 1, m + total)
        else:
            return total

    return loop(m, 0)

# while
def sumrange(m,n):
    total = 0

    while m <= n:
        total += m
        m += 1

    return total
##############################