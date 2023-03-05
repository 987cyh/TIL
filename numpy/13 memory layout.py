# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-numpy-13/, https://datascienceschool.net/, https://velog.io/@nylonmask/numpy
□ 기능: memory layout 기능
□ 목적: memory layout 기능 학습(C 언어 기반의 구조인 NUMPY가 PANDAS보다 적합한 이유)
□ 비고: 대량의 데이터를 학습 시킬 때, 활용 가능 할 것을 추측
"""
#%%
# package
import numpy as np
#%%
array = np.arange(10)

print(array)

arrayC = np.reshape(array, (2, -1), order='C') # C 언어
arrayF = np.reshape(array, (2, -1), order='F') # Fortan 언어

print(arrayC)
print(arrayF)
#%%