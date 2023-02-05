# -*- coding: utf-8 -*-
"""
□ 참고 : https://rfriend.tistory.com/623
□ 기능: array to dictionary / enumerate를 활용

"""
#%%
import numpy as np
#%%
cls_weight = np.array([0.30, 0.50, 0.10, 0.03, 0.07])
cls_weight
#%%
cls_weight_dict_from_0 = dict(enumerate(cls_weight))
cls_weight_dict_from_0

cls_weight_dict_from_1 = dict(enumerate(cls_weight, 1))
cls_weight_dict_from_1


cls_weight_dict_3 = {}
for i, c_w in enumerate(cls_weight):
    cls_weight_dict_3[i] = c_w

cls_weight_dict_3_from_1 = {}
for i, c_w in enumerate(cls_weight):
    cls_weight_dict_3_from_1[i+1] = c_w
#%%
