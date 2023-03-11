# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-31/
□ 기능 : thread
□ 목적 : thread 기능 정리 및 복습
"""
#%%
# 서브 쓰레드(Sub-Thread)
import threading

def first_task(data):
    for i in data:
        print("first_task :", i)

def second_task(data1, data2):
    for i, j in zip(data1, data2):
        print("second_task :", i, j)

task1 = threading.Thread(target=first_task, args=(range(5),))
task2 = threading.Thread(target=second_task, args=(range(5), range(5)))

print("START")
task1.start()
task2.start()
print("END")
#%%
# 데몬 쓰레드(Daemon-Thread)
def first_task(data):
    for i in data:
        print("first_task :", i)


def second_task(data1, data2):
    for i, j in zip(data1, data2):
        print("second_task :", i, j)


task1 = threading.Thread(target=first_task, args=(range(5000),))
task2 = threading.Thread(target=second_task, args=(range(5), range(5)))

task1.daemon = True
task2.daemon = True

print("START")
task1.start()
task2.start()
print("END")
#%%
