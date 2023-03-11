# -*- coding: utf-8 -*-
"""
□ 참고 : https://zzsza.github.io/mlops/2021/01/03/python-ray/
□ 기능 : ray
□ 목적 : ray 기능 정리
□ 활용방안 : 데이터 전처리 및 학습 데이터 생성(병렬), '기존의 멀티프로세싱 방법보다 코드로 구현하기 편리할 뿐더러 속도도 빠름'
"""
#%%
# package
import ray
import datetime
import numpy as np
import time

print(ray.__version__)
#%%
ray.init()

# Ray Task
@ray.remote
def print_current_datetime():
    time.sleep(0.3)
    current_datetime = datetime.datetime.now()
    print(current_datetime)
    return current_datetime

print_current_datetime.remote()
ray.get(print_current_datetime.remote())
#%%
# 동시에 8회 실행
futures = [print_current_datetime.remote() for i in range(8)]
print(futures)

# ray.get
ray.get(futures)
results = ray.get([print_current_datetime.remote() for i in range(8)])

ray.shutdown()
#%%
ray.init(num_cpus=8)

@ray.remote
def no_work(a):
    return

# 데이터를 그냥 사용하는 경우
start = time.time()
a = np.zeros((5000, 5000))
result_ids = [no_work.remote(a) for x in range(10)]
results = ray.get(result_ids)
print("duration =", time.time() - start)
# duration = 0.3409607410430908
#------------------------------------------------------------------
# 데이터를 ray.put()으로 저장한 후 사용하는 경우
start = time.time()
a_id = ray.put(np.zeros((5000, 5000)))
result_ids = [no_work.remote(a_id) for x in range(10)]
results = ray.get(result_ids)
print("duration =", time.time() - start)
# duration = 0.17802143096923828

ray.shutdown()
#%%