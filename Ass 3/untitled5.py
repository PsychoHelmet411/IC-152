# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:58:15 2024

@author: disha
"""
a=input("give ur no")
def myisdigit(a):
    a=a.strip()
    g=0
    if a[0] in "+-":
        g=g+1
    for i in range(g,len(a)):
        if a[i] in "0123456789":
            if i== len(a)-1:
                return True
        else:
            return False
print(myisdigit(a))        

        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        