# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-25/
□ 기능 : read / write
□ 목적 : read / write 등 기능 정리
"""
#%%
"""
r : 읽기(default)
w : 쓰기
a : 내용 추가
t : 텍스트모드(default)
b : 이진 모드
"""
file = open("d:/textfile.txt", mode="r")
file.close()
#%%
# 파일 자동 닫기
with open("d:/textfile.txt") as file:

#%%
# 텍스트 파일 작성
with open("d:/textfile.txt", mode="w") as file:
    words = ["Python\n", "is\n", "fun\n"]

    file.write("START\n")
    file.writelines(words)
    file.write("END")
#%%
# 텍스트 파일 한 줄씩 읽기
with open("d:/textfile.txt", mode="r") as file:
    content = list()

    while True:
        sentence = file.readline()
        if sentence:
            content.append(sentence)
        else:
            break
    print(content)


with open("d:/textfile.txt", mode="r") as file:
    content = list()
    for f in file:
        content.append(f)
    print(content)
#%%
# 텍스트 파일 한번에 읽기
with open("d:/textfile.txt", mode="r") as file:
    lines = file.readlines()
    print(lines)

with open("d:/textfile.txt", mode="r") as file:
    lines = file.read()
    print(lines)
#%%
