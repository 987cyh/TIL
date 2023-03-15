# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-39/
□ 기능 : special attributes
□ 목적 : special attributes 기능 정리 및 복습
"""
#%%
# special attributes
class CYH:
    """ CYH CLASS

    Callable types example.
    blah blah..

    To use:
    >>> instance = CYH(value)

    Args:
        value   : int

    Returns:
        null
    """

    def __init__(self, value: int):
        self.value = value

    def func(self) -> int:
        """func : Execute value * 100"""
        return self.value * 100


instance = CYH(777)

print(instance.__doc__)
print("---------")
print(instance.func.__doc__)
print("---------")
print(instance.func.__name__)
print(instance.func.__qualname__)
print(instance.func.__module__)
print(instance.func.__annotations__)
print(instance.__dict__)
#%%
