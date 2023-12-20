import numpy as np
#piNP = np.array([0.2,0.8])
#PNP = np.array([[3/10,7/10],[2/10,8/10]])

#========================================================================================================== Following stuff is related to matrix and markov chains
pi = [[1.,0.]]
P = [[2/10,8/10],[5/10,5/10]]

A = [[0.2,0.8]]
B = [[3/10,7/10],[2/10,8/10]]
def MaisonPower(n,A,B):
    """ returns matrix A times ( matrix B to the power n) """
    i = 0
    start = A
    while i < n:
        start = Mult(start,B)
        i+=1
    return start
    
def Mult(A,B):
    """ returns matrix A times matrix B"""
    n,m = len(A),len(B)
    n1,m1 = len(A[0]),len(B[0])
    i,j,k = 0,0,0
    res = []
    while i < n :
        #through rows of A
        temp = []
        while j < m1:
            #through columns of A
            temp.append(0)
            j+=1
        res.append(temp)
        i+=1
        j=0
    i,j = 0,0
    while i < n :
        #through rows of A
        while j < m1 :
            #through columns of A
            temp = 0
            while k < m:
                #through rows of B
                temp += A[i][k]*B[k][j]
                k+=1
            res[i][j] += temp
            k=0
            j+=1
        j=0
        i+=1
    return res
    

def Nthstate(n,pi,P):
    i = 0
    start = pi
    while i < n:
        start = start.dot(P)
        i+=1
    return start

M = [[1,1,1,1,1,0],[1,1,1,1,0,1],[1,1,0,1,1,1],[1,1,0,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
T = [[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,0,0,0,0,0]]


def prettyprint(A):
    """prints a matrix"""
    i,j = 0,0
    n,m = len(A),len(A[0])
    while i < n:
        print(A[i])
        i+=1
        
A = [[6/10,4/10],[2/10,8/10]]
B = [[1,-2,-3],[-3,2,9],[2,0,-3]]
n = 7
#prettyprint(MaisonPower(n,B,B))

#prettyprint(Mult(MaisonPower(0,T,T),M))
#prettyprint(MaisonPower(3,A,B))
 
#==================================================================================================================== Section about testing the limit of recursion
def TribonacciIT(n):
    u,v,w = 0,0,1
    i = 2
    if n == 0:
        return u
    if n == 1:
        return v
    if n == 2:
        return w
    while i <= n:
        z = u + v + w
        u,v,w = v,w,z
        i+=1
    return z
    

def TribonacciREC(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    else :
        return TribonacciREC(n-1) + TribonacciREC(n-2) + TribonacciREC(n-3)
n = 100

#print(TribonacciIT(n))
#print(TribonacciREC(n))

def Combi(n):
    L = [] 
    i = 0
    while i <= n:
        L.append(Tobin(i))
        i+=1
    return L
        
def Tobin(n):
    i = 0
    L = []
    while n > 0:
        L = [n%2] + L
        n //= 2
    return L
    
L = [[2,2,2],[2,2,2],[2,2,2]]
print(MaisonPower(3,L,L))
