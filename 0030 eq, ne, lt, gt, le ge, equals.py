# -*- coding: utf-8 -*-
"""
이항 비교 메서드(binary comparison method)

A.eq(B) / A==B
A.ne(B) / A!=B
A.lt(B) / A<B
A.gt(B) / A>B
A.le(B) / A<=B
A.ge(B) / A>=B
"""
#----------------------------------
import pandas as pd
#----------------------------------
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['a','b','c'])

df.eq(5)
df == 5

df['b'].eq(5)
df['b'] == 5


df['b'].ne(5)
df['b'] != 5
#----------------------------------

