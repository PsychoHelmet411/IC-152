# # str='110100'

# # print(str.rfind("1"))
# # print()



# pissquan={23,45,23,67,88,90,108}
# a= list(map(lambda x:x*2 , pissquan ))
# print ( a )


# b=list(filter(lambda x:(x//5),[1,2,5,31,5.1]))
# print(b)


# c=list(zip(a,b))
# print(c)























# a=(x**2 for x in [1,2,3,4,5])
# for i in a :
#     print(i,sep=",",end=",")
'''
The function is taking in a argument "alpha" and defing a function having dependency on alpha and returning the function.
The returned function is stored in a variable and when it is called with a argument say "beta" it returns " alpha + beta "

The scope of a inside the fun sumb is enclosing scope 

'''
import math
def f(a):
    def g(b):
        return math.sin(a-b)
    return g


# cos=f(math.pi/2)
# inner=cos(math.pi/3)
# print(inner)
































def factorial(n):
    if n==1 :
        return 1    
    return n*factorial(n-1) 

# print(factorial(6))



def prefRevCapStr(a):
    
    if a.isupper() is False :
        storage=a
    if len(a)==1:
        return a+" -> "+storage
    b=a.upper()
    return b[-1]+prefRevCapStr(b[:-1]) 

# print(prefRevCapStr("Diwali-to-come"))



def prefRevCapStr(string):
    if not string:
        return " -> "
    
    return string[-1].upper()+prefRevCapStr(string[:-1])+string[-1]
# print(prefRevCapStr("Diwali-To-Come"))


def fibb(n):
    if n==0:
        return 1
    if n==1:
        return 3
    return fibb(n-1)+fibb(n-2)
    
# print(fibb(4))

def fibb2(n):
    lst=[1,3]
    if n==0:
        return 1
    if n==1:
        return 3
    for i in range(0,n-1):
        lst.append(lst[-1]+lst[-2])
    return lst[-1]

# print(fibb2(4))







    
    









