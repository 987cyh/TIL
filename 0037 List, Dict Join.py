# -*- coding: utf-8 -*-
"""
□ list, dict구조에서 join()의 활용
→ join은 str에서만 적용
"""
#--------------------------------------------------------
# list
list_ex = ['가','나','다']
'-'.join(list_ex) # str만 join가능
list_ex2 = [1,2,3,4,5,6,7,8,9,10]
'-'.join(list_ex2) # TypeError: sequence item 0: expected str instance, int found

list_ex2 = list(map(str,list_ex2)) # str로 변경
'-'.join(list_ex2)

dict_ex = {'a':'apple','b':'bear','c':'car'}
'-'.join(dict_ex.keys())
'-'.join(dict_ex.values())
#--------------------------------------------------------