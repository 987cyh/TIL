# -*- coding: utf-8 -*-
"""
matplotilb에서 한글폰트 적용 및 마이너스기호 표현
1. 한글폰트 적용하기 위한 전처리 필요함(가상환경마다 해야함)
"""
#--------------------------------------------------------
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
#--------------------------------------------------------
# 한글폰트 설정하기 위한 전처리 / https://seong6496.tistory.com/95
mpl.matplotlib_fname() # matplotlibrc 파일을 메모장으로 열고 #font.family : NanumGothic
mpl.get_cachedir() # 캐시파일 삭제
#--------------------------------------------------------
# 한글폰트 적용
mpl.rc('font', family='NanumGothic')
print(plt.rcParams['font.family'])
# 음수(마이너스) 깨짐
mpl.rcParams['axes.unicode_minus'] = False
#--------------------------------------------------------
# 데이터준비
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 그래프 그리기
plt.plot(x, y1, label="sin") # sin그래프 정보 추가
plt.plot(x, y2, linestyle="--", label="cos") # cos그래프 정보 추가
plt.xlabel("x") # x축
plt.ylabel("y") # y축
plt.title("sin & cos 그래프") # 캔버스제목
plt.legend() # 범례
plt.show() # 그림 띄우기
#--------------------------------------------------------