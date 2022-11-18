# -*- coding: utf-8 -*-
"""
binning

소괄호 (): 초과, 미만
대괄호 []: 이상, 이하

(0,100] : 0초과 100이하
"""
###############################################################
import pandas as pd
df = pd.DataFrame([i for i in range(1, 500, 3)], columns=['value'])

bins = [0, 100, 200, 300, 400, 500]
labels = ['0~100','101~200','201~300','301~400','401~500']
df['bin'] = pd.cut(df['value'], bins=bins, labels=labels)

df['bin2'] = pd.qcut(df['value'], q=5)
###############################################################