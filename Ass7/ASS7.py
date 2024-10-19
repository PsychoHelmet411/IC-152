




#Q1
# main program:-
x = 6
# print("id(x) in main, 1st:", id(x),x)


# function definition:-
def doubleInput(x):
    print("id(x) in function: ", id(x),x)
    return x * 2

x = doubleInput(x)

# print("id(x) in main, 2nd:", id(x),x)






#Q2
# function definition:-
def squareInput(x):
    return x * x

x = squareInput(x)


# print("id(x) in main, 3rd:", id(x),x)
def sqr(r):
    sqrd=[]
    for i in range(0,r):
        a=int(input("input no: "))
        print(f"{i+1}Number")
        print(id(a)," no modification")
        a=squareInput(a)
        print(id(a)," after modification")
        sqrd.append(a)
        if i+1 in range(0,r):
            print("next number")
    return sqrd

# print(sqr(5))






#Q3
def Pythagorus(a,b=3):
    if a<0 & b<0:
        raise ValueError
    return a**2+b**2
# print( Pythagorus(24),Pythagorus(3,4) )




#Q4
def Lset(l):
    ls=[]
    for element in l:
        if element in ls:
            continue
        ls.append(element)
    return ls

l = [0, 2, 1, 2, 0, 5, 5, 0, 1, 3, 2, 0, 1, 2, 0]
# print(Lset(l))


def Lsort(l):
    emp=[]
    while l:
        greatest=0
        for element in l:
            if element>greatest:
                greatest=element
        emp.append(greatest)
        l.remove(greatest)
    return emp         

# print(Lsort(l))


data=[171, 174, 178, 181, 183, 183, 183, 184, 187, 188, 191, 196, 196, 199, 200, 200, 200, 202, 204, 204, 205, 206, 191, 191, 192, 193, 193, 193, 193, 194, 194, 195, 206, 211, 212, 213, 213, 216, 220, 221, 221, 227]

def Freqtab(l):
    k=l.copy()
    Mset=Lset(Lsort(l))
    freq={}
    for element in Mset:
        counter=0
        for j in k:
            if j==element:
                counter=counter+1
        freq[element]=counter
    print("|      Value     ||     frequency     |")
    # print(freq)
    for u,v in freq.items():
        print(f"|     {u}        ||       {v}         |")

# Freqtab([1,2,1,2,1])
def FD(l):
    shape={}
    k=Lsort(l)
    # print(k)
    max=k[0]
    min=k[-1]
    start=(int(min/10))*10
    end=int((max/10)+1)*10
    # print(start,end)
    for i in range(start,end,10):
        counter=0
        if i==end:
            for element in k:
                if element in range(i,i+11):
                    counter=counter+1



        else:
            for element in k:
                if element in range(i,i+10):
                    counter=counter+1
        shape[f"{i}-{i+10}"]=counter
    print("|     Class       ||    Frequency  |") 
    for u,v in shape.items():
        print(f"|     {u}     ||       {v}       |")


# FD(data)




#Q6
def Freqtab2(l):
    k=l.copy()
    Mset=Lset(Lsort(l))
    freq={}
    for element in Mset:
        counter=0
        for j in k:
            if j==element:
                counter=counter+1
        freq[element]=counter
    w=sum(freq.values())
    print("|      Value     ||     frequency     |")
    # print(freq)
    for u,v in freq.items():
        print(f"|     {u}        ||       {v/w}         |")

# Freqtab2([1,2,1,2,1])



def FD2(l):
    shape={}
    k=Lsort(l)
    # print(k)
    max=k[0]
    min=k[-1]
    start=(int(min/10))*10
    end=int((max/10)+1)*10
    # print(start,end)
    for i in range(start,end,10):
        counter=0
        if i==end:
            for element in k:
                if element in range(i,i+11):
                    counter=counter+1



        else:
            for element in k:
                if element in range(i,i+10):
                    counter=counter+1
        shape[f"{i}-{i+10}"]=counter
    n=sum(shape.values())
    
    
    
    print("|     Class       ||    Frequency  |") 
    for u,v in shape.items():
        print(f"|     {u}     ||       {v/n}       |")


# FD2(data)




































