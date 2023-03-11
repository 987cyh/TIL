# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-34/
□ 기능 : function annotations
□ 목적 : function annotations 기능 정리 및 복습
"""
#%%
def func(a: str, b: float = 3.5) -> int:
    return a + b

value = func(3)
print(value)
#%%
