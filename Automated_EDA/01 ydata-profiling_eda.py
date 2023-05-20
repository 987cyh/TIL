# -*- coding: utf-8 -*-
"""
□ 참고 : https://ydata-profiling.ydata.ai/docs/master/index.html
□ 기능 : ydata-profiling
□ 목적 : ydata-profiling 학습(Automated EDA)
"""
#%%
# package
import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport, compare
#%%
# data load
train_df = pd.read_csv("titanic_train.csv")
test_df = pd.read_csv("titanic_test.csv")

# single data EDA
train_report = ProfileReport(train_df, title="Train")
train_report.to_file("ydata_train_eda.html")

test_report = ProfileReport(test_df, title="Test")
test_report.to_file("ydata_test_eda.html")

# More than one data EDA
comparison_report = compare([train_report, test_report])
statistics = comparison_report.get_description()
comparison_report.to_file("ydata_data_comparison_eda.html")
#%%