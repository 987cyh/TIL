# -*- coding: utf-8 -*-
"""
■ lambda의 구조이해
"""
##############################
def sum(a,b):
    return a+b

sum(10,30)

(lambda a,b: a+b)(10,30) #input을 끝에 괄호에 넣어서 사용
##############################
answer1 = (lambda x: True if (x > 0) else False)(1) #input을 끝에 괄호에 넣어서 사용
answer2 = (lambda x: True if (x > 0) else False)(-1) #input을 끝에 괄호에 넣어서 사용
##############################