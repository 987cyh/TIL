# -*- coding: utf-8 -*-
"""
□ 참고 : https://pypi.org/project/sweetviz/
□ 기능 : sweetviz
□ 목적 : sweetviz 학습(Automated EDA)
"""
#%%
# package
import numpy as np
import pandas as pd
import sweetviz as sv
#%%
# data load
train_df = pd.read_csv("titanic_train.csv")
test_df = pd.read_csv("titanic_test.csv")


# single data EDA
train_report = sv.analyze(train_df)
train_report.show_html('sweetviz_train_eda.html')

test_report = sv.analyze(test_df)
test_report.show_html('sweetviz_train_eda.html')

#%%
## comparision datasets
comparison_report = sv.compare(train_df, test_df)
comparison_report.show_html('sweetviz_train_eda.html')

comparison_report_y = sv.compare([train_df,"Train"], [test_df,"Test"], "Survived")
comparison_report_y.show_html('sweetviz_train_eda_y.html')
#%%