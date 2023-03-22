# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-45/, https://purplechip.tistory.com/36
# https://stackoverflow.com/questions/73013660/python-multiprocessing-not-working-on-windows
□ 기능 : multiprocessing
□ 목적 : multiprocessing 기능 정리 및 복습
"""
#%%
# Process
import os
import time
from multiprocessing import Process, freeze_support

def task(idx, count):
    print(f"PID : {os.getpid()}")
    logic = sum([i ** 2 for i in range(count)])
    return idx, logic

if __name__ == "__main__":
    freeze_support()

    job = [("첫 번째", 10 ** 7), ("두 번째", 10 ** 7), ("세 번째", 10 ** 7), ("네 번째", 10 ** 7)]

    start = time.time()

    process = []
    for idx, count in job:
        p = Process(target=task, args=(idx, count))
        p.start()
        process.append(p)

    for p in process:
        p.join()

    print(f"End Time : {time.time() - start}s")

    start = time.time()

    for idx, count in job:
        task(idx, count)

    print(f"End Time : {time.time() - start}s")
#%%
from multiprocessing import Pool, freeze_support
# Pool
def task(pairs):
    print(f"PID : {os.getpid()}")
    idx, count = pairs
    logic = sum([i ** 2 for i in range(count)])
    return idx, logic


if __name__ == "__main__":
    freeze_support()
    job = [("첫 번째", 10 ** 7), ("두 번째", 10 ** 7), ("세 번째", 10 ** 7), ("네 번째", 10 ** 7)]

    start = time.time()

    p = Pool(processes=2)
    result = p.map(task, job)

    print(result)
    print(f"End Time : {time.time() - start}s")

    start = time.time()

    result = [task(j) for j in job]

    print(result)
    print(f"End Time : {time.time() - start}s")
#%%
# Parallel
from joblib import Parallel, delayed


def task(idx, count):
    print(f"PID : {os.getpid()}")
    logic = sum([i ** 2 for i in range(count)])
    return idx, logic

job = [("첫 번째", 10 ** 7), ("두 번째", 10 ** 7), ("세 번째", 10 ** 7), ("네 번째", 10 ** 7)]

start = time.time()

result = Parallel(n_jobs=4)(delayed(task)(idx, count) for idx, count in job)

print(result)
print(f"End Time : {time.time() - start}s")

start = time.time()

result = [task(*j) for j in job]

print(result)
print(f"End Time : {time.time() - start}s")
#%%
