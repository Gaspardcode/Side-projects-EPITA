import math
import random
import time

def MinMax(L,*args):
    if len(args) == 2:
        return args[0],args[1]
    else:
        i = 0
        n = len(L)
        mini = math.inf
        maxi = -math.inf
        while i < n:
            a = L[i]
            if a < mini:
                mini = a
            if a > maxi :
                maxi = a
            i+=1
        return mini,maxi
        
def Histo(L,delta,maxi):
    i = 0
    H = [0 for i in range(maxi+delta+1)]
    while i < n:
        H[L[i]+delta]+=1
        i+=1
    return H
    
def Load(H,maxi):
    i=0
    L=[]
    while i <= maxi:
        n = H[i]
        j = 0
        while j < n:
            L.append(i)
            j+=1
        i+=1
    return L

def TriD(L):
    mini, maxi = MinMax(L)
    H = Histo(L,mini,maxi)
    return Load(H,maxi)

n = 1000000
L = [n-i-1 for i in range(n)]
L1 = [3 for i in range(n//2)] + [2 for i in range(n//2)]
L2 = [random.randint(0,i) for i in range(n)]

start = time.perf_counter()
TriD(L)
medium = time.perf_counter()
print("TriD : " + str(medium - start))
L.sort()
end = time.perf_counter()
print("python sort : " + str(end - medium))
