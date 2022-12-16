# -*- coding: utf-8 -*-
"""
□ 정규 표현식 (Regular Expression)
□ 참고: http://pythonstudy.xyz/python/article/401-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D-Regex
"""
#%%
import re
#%%
text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchobj = regex.search(text)
phonenumber = matchobj.group()
print(phonenumber)
#%%
text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
regex = re.compile("에러 1033")
mo = regex.search(text)
if mo != None:
print(mo.group())
#%%
text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
regex = re.compile("에러\s\d+")
mc = regex.findall(text)
print(mc)
# 출력: ['에러 1122', '에러 1033']
#%%
text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
matchobj = regex.search(text)
areaCode = matchobj.group(1)
num = matchobj.group(2)
fullNum = matchobj.group()
print(areaCode, num)  # 032 232-3245
#%%
text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
regex = re.compile(r'(?P<area>\d{3})-(?P<num>\d{3}-\d{4})')
matchobj = regex.search(text)
areaCode = matchobj.group("area")
num = matchobj.group("num")
print(areaCode, num)  # 032 232-3245
