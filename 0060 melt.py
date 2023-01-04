# -*- coding: utf-8 -*-
"""
ㅁ 참고 : https://wikidocs.net/154170
"""
#%%
import pandas as pd
import numpy as np
#%%
col = ['Country','Machine','Price','Brand']
data = [['Korea','TV',1000,'A'],
        ['Japan','TV',1300,'B'],
        ['Korea','PC',2000,'A'],
        ['Japan','PC',3000,'E']]
df = pd.DataFrame(data=data, columns=col)
#%%
print(df.melt(id_vars='Country',value_vars=['Machine','Price']))
print(df.melt(id_vars='Country',value_vars=['Machine','Price'],ignore_index=False))
print(df.melt(id_vars='Country',value_vars=['Machine','Price'],var_name='Category',value_name='val'))
#%%
col2 = [['Area','Area','Value','Value','Value'],['Country','City','Machine','Price','Brand']]
data2 =[['Korea','Seoul','TV',1000,'A'],
        ['Japan','Tokyo','TV',1300,'B'],
        ['Korea','Jeju','PC',2000,'A'],
        ['Japan','Kyoto','PC',3000,'E']]
df2=pd.DataFrame(data=data2, columns=col2)
print(df2)
#%%
print(df2.melt(id_vars=[('Area','City')],value_vars=[('Value','Price')]))
print(df2.melt(id_vars='City',value_vars='Price',col_level=1))
#%%
