# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:50:32 2024

@author: disha
"""
def Myeval(string):
    # print(string)
    lst=[]
    i=0
    while i in range(0, len(string)):
        if string[i] in ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']:
            start=i
            k=i
            while string[k] in ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']:
                end=k
                if i==(len(string)-1):
                    break
                k=k+1
            lst.append(int(string[start:end+1]))
            if i==(len(string)-1):
                break
            i=k
        else:
            i=i+1    
    # print(lst)
    return lst
# print(Myeval(input("enter the required numbers: ")))

def mean(lst2):
    result=0
    for element in lst2:
        result=result+element
    return result/(len(lst2))



def numedian(a) :
    a.sort()
    if len(a) & 1 :#odd
        median= a[int(((len(a)+1)/2) -1) ] 
        return median
    else:
        k= int((len(a)/2) -1)
        m = int(len(a)/2)
        
        return (a[k]+a[m])/2
    
def median(a):
    a.sort()
    if len(a) & 1 :#odd
        median= a[int(((len(a)+1)/2) -1) ] 
        return f"{median}"
    else:
        k= int((len(a)/2) -1)
        m = int(len(a)/2)
        
        return {f"{a[k]},{a[m]}":(a[k]+a[m])/2}
        







''' Q3
 lst=Myeval(input("give your list "))
    Svalues={}
    for elemnt in lst:
        a=0
        for n in lst:
            a=a+(n-elemnt)**2
        Svalues.update({elemnt:a})
    print(Svalues)    
    print(mean(lst))
    a=0
    for n in lst:
        a=a+(n-mean(lst))**2
    print(a)     
   '''

         
lst=Myeval(input("give a array: "))
Avalues={}
for element in lst:
    sigma=0
    for n in lst:
        sigma=sigma+abs(element-n)
    Avalues.update({element:sigma})
print(median(lst),numedian(lst))
print(Avalues)
k=0
for n in lst:
    k=k+abs(numedian(lst)-n)
print(k)
k=0
for n in lst:
    k=k+abs(9.2-n)
print(k)





def arraymean():
    sastiArray=[]
    a=Myeval(input("give your elements: "))
    b=int(input("no of rows? "))
    p=int(len(a)/b)
    if len(a)%b!= 0 :
        raise IndexError
    k=0
    for i in range(0,b):
            sastiArray.append(a[k:k+p])
            k=k+p
    Mean=[]
    for element in sastiArray:
        Mean.append(mean(element))
    return Mean



def rv(lst):
    mu=mean(lst)
    lst3=[]
    for element in lst:
        lst3.append(element-mu)
    return lst3 
def dot(lstA,lstB):
    dot=0
    for i in range(0,min(len(lstA),len(lstB))):
        dot=dot+lstA[i]*lstB[i]
    return dot
def vmod(lstA):
    res=0
    for element in lstA:
        res=res+element**2
    return res**(1/2)

def corrA():
    lstA=Myeval(input("give your first list"))
    lstB=Myeval(input("give your first list"))
    m=dot(rv(lstA),rv(lstB))
    k=(vmod(rv(lstA)))*(vmod(rv(lstB)))
    return m/k

def corrB():
    lstA=Myeval(input("give your first list"))
    lstB=Myeval(input("give your first list"))
    p=min(len(lstA),len(lstB))
    lstA=lstA[:p]
    lstB=lstB[:p]
    
    
    sigmaxi=mean(lstA)*len(lstA)
    sigmayi=mean(lstB)*len(lstB)
    sigmaxiyi=dot(lstA,lstB)
    sigmaxi2=vmod(lstA)**2
    sigmayi2=vmod(lstB)**2
    
    r=  ( p*sigmaxiyi - (sigmaxi)*(sigmayi)  )/(  ((p*(sigmaxi2) -(sigmaxi)**2)**(1/2))*((p*(sigmayi2) -(sigmayi)**2)**(1/2)))
    return r








































































