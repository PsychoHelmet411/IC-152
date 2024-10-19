# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:09:11 2024
"""
def isperfect(a):
    RESULT=0
    for i in range(1,int(a/2)+1):
        if (a/i)-(a//i)==0 :
            RESULT=RESULT+i
    if RESULT==a:
        return True
    else:
        return False    

i=5
while i<(100000000):
    if isperfect(i) == True:
        print(i)
    i=i+1
    


























































