# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-29/
□ 기능 : enumerate
□ 목적 : enumerate 기능 정리
"""
#%%
# 단일 list
L1 = ["Life", "is", "cool"]

for i, datum in enumerate(L1):
    print(i, L1)
#%%
# zip함수를 통한 2개의 list 병합
# zip함수의 특성상 요소의 길이가 다르다면, 더 작은 길이를 갖는 반복 횟수로 설정
L2 = ["오늘", "하루도", "수고했어", "★"]
L3 = ["Life", "is", "cool"]

for i, (k, t) in enumerate(zip(L2, L3)):
    print(i, k, t)
#%%
