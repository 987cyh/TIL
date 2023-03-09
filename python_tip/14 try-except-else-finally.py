# -*- coding: utf-8 -*-
"""
□ 참고 : https://wayhome25.github.io/python/2017/08/20/python-try-return-finally/
□ 기능 : try-except-else-finally
□ 목적 : try-except-else-finally 기능 정리
"""
#%%
"""
try : 실행코드
except : 예외처리 코드 
else : 예외처리할 오류가 없을때 실행되는 코드
finally : 오류 발생여부 상관 없이 무조건 실행되는 코드
"""
#----------------------------------------
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("0으로 나눌 수 없어요!")
        return False
    else:
        print("결과:", result)
        print("결과:", result)
        return True
    finally:
        print("나누기 연산을 종료합니다.")

divide(6, 0)
divide(6, 3)
divide(6, '3')
#%%
