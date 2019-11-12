def f(x):

    k = 0
    for i in range(1,2*x,2):
        k += i

    for j in range(k):
        if j%x==0:
            k += 2

    return k+3

#----------------------------------------------------------------
 
def f_inv(x):

    i=0
    while True:
        if f(i)==x:
            return i
        i+=1

#main============================================================
    
print(eval(input().strip()))
