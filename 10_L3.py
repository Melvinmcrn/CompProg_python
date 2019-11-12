def dhanoi(n,left,mid,right):

    if n==0:
        return

    dhanoi(n-1,left,mid,right)
    print(str(n)+'W',':',left,'->',mid)
    print(str(n)+'B',':',left,'->',mid)
    dhanoi(n-1,right,mid,left)
    print(str(n)+'B',':',mid,'->',right)
    print(str(n)+'W',':',mid,'->',right)
    dhanoi(n-1,left,mid,right)

#main========================================================

exec(input().strip())
