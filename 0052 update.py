# -*- coding: utf-8 -*-
#%%
import pandas as pd
import numpy as np
#%%
df1 = pd.DataFrame({'A':[1,2,3],'B':[np.nan,5,6]})
df2 = pd.DataFrame({'B':[24,np.nan,26],'C':[37,38,39]})

# df1의 Na를 포함 덮어씌우기가 진행, 5의 경우 df2의 값이 Na이므로 무시
df1.update(df2,overwrite=True)
# df1에서 Na인 값에 대해서만 업데이트
df1.update(df2,overwrite=False)
#df1에서 6인 값에 대해서만 업데이트
df1.update(df2,filter_func=lambda x: x==6)
#%%
