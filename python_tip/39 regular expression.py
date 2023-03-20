# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-43/
□ 기능 : Regular Expression
□ 목적 : Regular Expression 기능 정리 및 복습
"""
#%%
import re
#%%
# findall
string = """
정규 표현식(Regular Expression)은 프로그래밍에서 사용하는 형식 언어입니다.
특정한 규칙을 가진 문자열을 검색, 분리, 치환하는 데 주로 활용되며, 특정한 패턴과 일치하는 텍스트를 입력값에서 찾아 반환합니다.
정규 표현식을 사용하지 않고 문자열에서 특정 패턴을 찾는 경우 매우 복잡한 코드를 작성해야 합니다.
하지만 정규 표현식을 활용할 경우 코드가 매우 간결해지며 유사한 문자까지 일치시켜 검색할 수 있습니다.
"""

pattern = re.compile(r"\((.*?)\)")
find = re.findall(pattern, string)
print(find)
#%%
# search
string = """
정규 표현식(Regular Expression)은 프로그래밍에서 사용하는 형식 언어입니다.
특정한 규칙을 가진 문자열을 검색, 분리, 치환하는 데 주로 활용되며, 특정한 패턴과 일치하는 텍스트를 입력값에서 찾아 반환합니다.
정규 표현식을 사용하지 않고 문자열에서 특정 패턴을 찾는 경우 매우 복잡한 코드를 작성해야 합니다.
하지만 정규 표현식을 활용할 경우 코드가 매우 간결해지며 유사한 문자까지 일치시켜 검색할 수 있습니다.
"""

pattern = re.compile(r"\((.*?)\)")
match = re.search(pattern, string)
print(match)
print(match.group(), match.start(0))
#%%