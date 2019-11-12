def p(n):

    if 0 <= n <= 2:
        return 1

    if n >= 3:
        return p(n-2) + p(n-3)

#----------------------------------------------------------------
def m(n):

    if n == 1 or n == 2:
        return 1

    temp = m(n-2)

    return m(temp) + m(n-temp)

#----------------------------------------------------------------
def e(n):

    if n == 2 or n == 3:
        return 1

    out = 0
    for k in range(1,n-1):

        if (k+1) == (n-k):
            temp = e(k+1)
            out += temp ** 2
        else:
            out += e(k+1) * e(n-k)

    return out

#----------------------------------------------------------------
def s(n,k):

    if n == 0:
        return 2

    temp = s(n-1,k)

    return ( temp ** 2 - temp + 1 ) % k

#----------------------------------------------------------------

exec(input().strip())
