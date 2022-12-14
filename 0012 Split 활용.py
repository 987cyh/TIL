# -*- coding: utf-8 -*-
"""
split을 활용하여, 모스부호 해석해보기
"""
###############################################################
morse = {
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}

def solution(letter):
    return ''.join([morse[i] for i in letter.split(' ')])

text = ".... . .-.. .-.. ---"
solution(text)
###############################################################