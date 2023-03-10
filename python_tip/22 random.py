# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-26/
□ 기능 : random
□ 목적 : random 등 기능 정리
"""
#%%
# 난수 생성
import random

print(random.random())
print(random.uniform(10.5, 10.6))
print(random.randrange(10))
print(random.randrange(1, 10))
print(random.randint(5, 15))
#%%
# 리스트의 원소 값을 활용한 난수 발생
L = [1, 10, 100, 1000]

print(random.choice(L))
print(random.sample(L, 2))
random.shuffle(L)
print(L)
#%%
# 난수 상태 설정
random.seed(750)

state = random.getstate()
print(random.sample(range(100), k=5))
print(random.sample(range(100), k=5))
random.setstate(state)
print(random.sample(range(100), k=5))
#%%
