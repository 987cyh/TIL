# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-43/
□ 기능 : container method
□ 목적 : container method 기능 정리 및 복습
"""
#%%
import operator


class CYH(dict):

    _dict = {"A": 1, "B": 2, "C": 3}

    def __len__(self):
        print("length")
        return len(self._dict)

    def __length_hint__(self):
        print("length_hint")
        return operator.length_hint(self._dict)

    def __getitem__(self, key):
        try:
            return self._dict[key]
        except:
            return self.__missing__(key)

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __delitem__(self, key):
        del self._dict[key]

    def __missing__(self, key):
        return self._dict

    def __iter__(self):
        return iter(self._dict)

    def __reversed__(self):
        return dict(zip(self._dict.values(), self._dict.keys()))

    def __contains__(self, item):
        if item in self._dict:
            print("%s is contained in Key." % item)
            return True
        elif item in self._dict.values():
            print("%s is contained in Value." % item)
            return True
        else:
            print("%s is not contained in Key & Value." % item)
            return False


name = CYH()
print(operator.length_hint(name))
name["e"] = 5
print(name["D"])
print(reversed(name))
print(operator.contains(name, 1))
#%%
