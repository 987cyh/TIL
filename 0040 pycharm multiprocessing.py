# -*- coding: utf-8 -*-
"""
문제원인 : https://youtrack.jetbrains.com/issue/PY-50116
해결방안: https://stackoverflow.com/questions/74644040/pycharm-multiprocessing-error-what-can-i-do ★

→ PyCharm 2022.1.4: 실행모드에서는 정상적으로 작동, ipython에서는 오류가 발생함 ★★★
  vscode: ipython에서도 정상적으로 작동함
"""
#%%
from multiprocessing import Pool
def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))