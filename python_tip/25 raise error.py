# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-30/
□ 기능 : raise
□ 목적 : raise 기능 정리
"""
#%%
fruit = ["red", "blue", "green", "black", "yellow"]
print(fruit)

while True:
    index = input("색상 색인 값 선택: ")

    try:
        index = int(index)

        if index == 1:
            raise NameError

        else:
            print(fruit[index])

    except NameError:
        print("blue는 불가능합니다.")

    except IndexError:
        print("해당 색인은 호출할 수 없습니다.")

    except ValueError:
        print("소수점은 사용할 수 없습니다.")

    print("------------")
#%%
# 사용자 정의 오류 발생
class AdminError(Exception): # error 사용자 정의
    pass
#----------------------------------------------------
while True:

    admin = input("관리자 계정 입력: ")

    try:
        if admin != "grant":
            raise AdminError()
        else:
            print("관리자 계정입니다.")

    except AdminError:
        print("관리자 계정이 아닙니다.")

    print("------------")
#%%
