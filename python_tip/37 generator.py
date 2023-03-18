# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-42/
□ 기능 : generator
□ 목적 : generator 기능 정리 및 복습
"""
#%%
def generator():
    data = [0]

    print("First")
    data.append(1)
    yield data

    print("Second")
    data.append(2)
    yield data

    print("Third")


gen = generator()
print(next(gen))
print("———")
print(next(gen))
print("———")
print(next(gen, "END"))
print("———")
print(next(gen, "END"))
print("———")
#%%
def generator():
    value = [1, 2, 3, 4, 5]
    yield value

gen = generator()
print(list(gen))
#%%
def generator():
    value = [1, 2, 3, 4, 5]
    yield from value

gen = generator()
print(list(gen))
#%%
# Coroutine
from itertools import count


def coroutine():

    for c in count():
        value = yield c
        print("Value:{}, Count:{}".format(value, c))


cor = coroutine()
cor.send(None)
cor.send("A")
cor.send(200)
cor.send(50)
#%%
from itertools import count


def coroutine():

    for c in count():
        value = yield c
        print("next() - Value:{}, Count:{}".format(value, c))
        yield value
        print("send() - Value:{}, Count:{}".format(value, c))


cor = coroutine()
next(cor)
cor.send("A")
next(cor)
cor.send(200)
next(cor)
cor.send(50)
next(cor)
#%%
# throw
def coroutine():

    for c in count():
        try:
            value = yield c
            print("next() - Value:{}, Count:{}".format(value, c))
            yield value
            print("send() - Value:{}, Count:{}".format(value, c))
        except ValueError:
            print("Error", c)


cor = coroutine()
next(cor)
cor.send("A")
cor.throw(ValueError, "오류가 발생했습니다.")
cor.send(200)
cor.throw(ValueError, "오류가 발생했습니다.")
cor.throw(ValueError, "오류가 발생했습니다.")
#%%
def coroutine():

    for c in count():
        try:
            value = yield c
            print("next() - Value:{}, Count:{}".format(value, c))
            yield value
            print("send() - Value:{}, Count:{}".format(value, c))
        except ValueError:
            print("Error", c)


cor = coroutine()
next(cor)
cor.send("A")
cor.close()
print(next(cor, "END"))
#%%
