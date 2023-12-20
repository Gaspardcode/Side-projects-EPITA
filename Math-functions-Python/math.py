def facto(n):
    """returns the factorial n"""
    res =1
    i=1
    while i < n + 1:
        res *=i
        i+=1
    return res

def Stirling2r(n,k):
    """ Stirling numbers of the second kind"""
    if k == 1:
        return 1
    if n == 1:
        if k == 0:
            return 0
        else:
            return 0
    else:
        return k*Stirling2r(n-1,k) + Stirling2r(n-1,k-1)

def Stirling1r(n,k):
    """ Stirling numbers of the first kind"""
    if k == 1:
        return facto(n-1)
    if n == 1:
        if k == 0:
            return 0
        else:
            return 0
    else:
        return (n-1)*Stirling1r(n-1,k) + Stirling1r(n-1,k-1)

def Showk(func,n):
    """ prints the Stirling's triangle given one of the kind"""
    i=0
    while i <= n:
        print("{} cycles {} : {}".format(n,i,func(n,i)))
        i+=1

Showk(Stirling2r,20)

import math
#=================================================================
def roots(a,b,c):
    """ gives the roots of 2nd degree polynom"""
    d = b*b - 4*a*c
    if d == 0:
        return [-b/2*a]
    if d > 0:
        return [(-b-math.sqrt(d))/2*a,(-b+math.sqrt(d))/2*a]
    else:
        z1,z2 = complex(-b,-math.sqrt(-d)), complex(-b,math.sqrt(-d)) 
        return [z1/2*a,z2/2*a]
a,b,c = 1,-4,13
#print(roots(a,b,c))

import matplotlib.pyplot as plt

def reel(max):
    """ I don't remember. Something about paying with complex numbers"""
    j = complex(math.sqrt(2)/2,math.sqrt(2)/2)
    L= []
    i = 0
    temp = 1
    while i <= max:
        if temp.imag == 0 and temp.real != 0:
            L.append(i)
        temp*= j
        i+=1
    return L

#print(reel(10))
#print(reel(20))
#========================================================================
def AmISquareSum(n):
    i = 0
    while i < n :
        j = 0
        temp = i*i
        while j < n:
            if j*j + temp == n :
                return [i,j]
            j+=1
        i+=1
    return [-1,-1]
    
#print(AmISquareSum(17900))

def courbeA(n):
    plt.clf()
    i = 0
    ordo = []
    absc = []
    while i < n:
        ordo.append(i)
        absc.append(i*i)
        i+= 1
    plt.plot(ordo,absc,'b')
    plt.show()

#courbeA(0)

def Inf(n):
    i = 0
    z = complex(2)
    m = complex(math.sqrt(3)/2,-1/2)
    L = []
    while i < n:
        if z.real == 0 and z.imag != 0:
            L.append(i)
        z*=m
        i+=1
    return L
    
print(Inf(50))

#========================================================================================================= OPTIMISATION RELATED ===================================================
import time

def Expo(n):
    i=0
    res = 1
    while i < n:
        res*= math.e
        i+=1
    return res
def fastExpo(n):
    res = 1
    exp = math.e
    while n > 0:
        if n % 2 == 1:
            res*= exp
        n//=2
        exp*=exp
    return res

def facto(n):
    res =1
    i=1
    while i < n +1:
        res *=i
        i+=1
    return res
    
def fastEx(x,n):
    res = 1
    exp = x
    while n > 0:
        if n % 2 == 1:
            res*= exp
        n//=2
        exp*=exp
    return res
    
def SeriesExp(n,p):
    res = 0
    i = 0
    while i < p:
        res += fastEx(n,i)/facto(i)
        i+=1
    return res
    

def Compare(x,y,n):
    i = 0
    print("    " + str(x) + " | " + str(y))
    print("---------------------------------")
    while i < n:
        print("    " + str(fastEx(x,i)) + " | " + str(fastEx(y,i)))
        i+=1


    
    
n = 1000
p = 20000

def plotCompare(p):
    """bench mark function """
    plt.clf()
    i = 0
    L1 = []
    L2 = []
    absc = []
    while i < p:
        start = time.perf_counter()
        Expo(i)
        medium = time.perf_counter()
        L1.append(medium - start)
        fastExpo
        end = time.perf_counter()
        L2.append(end - medium)
        absc.append(i)
        i+=1
    plt.plot(absc,L1,label="Expo")
    plt.plot(absc,L2,label = "FastExpo")
    plt.legend()
    plt.show()
    

def plotC(n,p):
    plt.clf()
    i = 0
    L1 = []
    L2 = []
    absc = []
    while i < p:
        start = time.perf_counter()
        n^p
        medium = time.perf_counter()
        L1.append(medium - start)
        fastEx(n,p)
        end = time.perf_counter()
        L2.append(end - medium)
        absc.append(i)
        i+=1
    plt.plot(absc,L1,label="Expo")
    plt.plot(absc,L2,label = "FastExpo")
    plt.legend()
    plt.show()
    
#plotC(n,p)
