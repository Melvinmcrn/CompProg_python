def C(n,k):

    if k>0 and n>k:
        return C(n-1,k) + C(n-1,k-1)
    if k==0 or n==k:
        return 1

    return 0

#main==================================================

n=int(input())
k=int(input())
print(C(n,k))
