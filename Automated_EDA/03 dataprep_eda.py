# -*- coding: utf-8 -*-
"""
□ 참고 : https://docs.dataprep.ai/installation.html
□ 기능 : dataprep
□ 목적 : dataprep 학습(Automated EDA)
"""
#%%
# package
import numpy as np
import pandas as pd
from dataprep.eda import create_report
from dataprep.datasets import load_dataset
from dataprep.eda import plot_diff
#%%
# data load
train_df = pd.read_csv("titanic_train.csv")
test_df = pd.read_csv("titanic_test.csv")


# single data EDA
train_report = create_report(train_df)
train_report.save('dataprep_train_eda')
train_report.show_browser()

test_report = create_report(test_df)
test_report.save('dataprep_test_eda')
test_report.show_browser()

# More than one data EDA
plot_diff([train_df, test_df])
#%%