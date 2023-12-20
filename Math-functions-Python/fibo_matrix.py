import time
def produit(A,B):
    m=[]
    i,j = 0 , 0
    while i < 2:
        j = 0
        T = []
        while j < 2:
            k = 0
            V = 0;
            while k < 2:
                V+=A[i][k]*B[k][j]
                k+=1
            T.append(V)
            j+=1
        m.append(T)
        i+=1
    return m
   
def SM(m,n):
    if n == 1:
        return m
    else:
        return produit(m,SM(m,n-1))
       
def pSM(m,n):
    if n == 1:
        return m
    else:
        if n % 2 == 1:
            return produit(m,pSM(produit(m,m),n//2))
        else:
            return pSM(produit(m,m),n//2)
           
def FibSM(n):
    return pSM([[1,1],[1,0]],n-1)[0][0]
   
def Fib(n):
    fib1 = 0
    fib2 = 1
    while n != 0:
        n-=1
        fib2 , fib1 = fib2 + fib1, fib2
    return fib1
   
start = time.perf_counter()
FibSM(500000)
print(time.perf_counter() - start)
middle = time.perf_counter()
Fib(500000)
print(time.perf_counter() - middle)
