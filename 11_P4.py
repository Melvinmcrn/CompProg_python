import numpy as np

def fib(n, k): 

   F = np.array([[0,1],[1,1]])

   if n == 0:
       return 0

    if n== 1:
        return F[0,1]

    return fib
   
   
n,k = [int(e) for e in input().split()]
print( fib(n,k) )
