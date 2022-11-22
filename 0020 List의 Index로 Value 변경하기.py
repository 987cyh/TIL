# -*- coding: utf-8 -*-
"""
■ 리스트 안에 인덱스 변경하기
한번에 원하는 값을 인덱스를 통해서 변경이 가능함
"""
##############################
def list_change(list, num1, num2):
    list[num1],list[num2] = list[num2],list[num1] # index의 value가 동시에 변경됨
    return list

name_list = ['철수','영희','갑이','바트','리사','영철']

list_change(name_list,0,3)
##############################