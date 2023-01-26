# -*- coding: utf-8 -*-
"""
□ 참고 : https://wikidocs.net/156736
□ 기능: sem (표준오차)
"""
#%%
import pandas as pd
import numpy as np
#%%
a = [1,1,1,1,1]
b = [1,2,3,4,5]
c = [20,40,60,80,100]
data = {"col1":a,"col2":b,"col3":c}
df = pd.DataFrame(data)
print(df)
#%%
print(df.sem())

# col1     0.000000
# col2     0.707107
# col3    14.142136
#%%
