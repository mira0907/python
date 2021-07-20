# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 15:40:13 2021

@author: dkjua
"""

m=int(input('數學成績?'))
e=int(input('英文成績?'))
if m>=90 and e>=90:
    print('有獎')
elif m<60 and e<60:
    print('要處罰')
elif m<60 or e<60:
   print('要加油') 
