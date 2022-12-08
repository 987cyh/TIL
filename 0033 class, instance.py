# -*- coding: utf-8 -*-
"""
참고: https://rekt77.tistory.com/97
□ class, instance 이해
"""
#--------------------------------------------------------
class Monster:
    def __init__(self, hp, atk, dfn):
        self.hp = hp
        self.atk = atk
        self.dfn = dfn

    def attack(self, target):
        target.ReduceHP(self.atk)

    def ReduceHP(self, atk):
        self.hp = self.hp - (atk - self.dfn)


if __name__ == "__main__":
    m1 = Monster(100, 20, 5)
    m2 = Monster(100, 10, 3)

    m2.attack(m1)
    print(m1.hp)
#--------------------------------------------------------