def F(n):

    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n%3 == 0 and n > 0:
        temp1 = F(n//3)
        return 5 * temp1 ** 3 + 3 * (-1) ** n * temp1
    if n%3 == 1 and n > 0:
        temp1 = F((n-1)//3 + 1)
        temp2 = F((n-1)//3)
        return temp1 ** 3 + 3 * temp1 * temp2 ** 2 - temp2 ** 3
    if n%3 == 2 and n > 0:
        temp1 = F((n-2)//3 + 1)
        temp2 = F((n-2)//3)
        return temp1 ** 3 + 3 * temp1 ** 2 * temp2 + temp2 ** 3

#---------------------------------------------------------------
def x(m,n):

    if n == 0:
        return m
    if m == 0:
        return n
    if m >= 0 and n >= 0:
        return x(m,n-1) + x(m-1,n)
    
#---------------------------------------------------------------
def p(n):
    
    if n%2 == 0 and n>1:
        return n + 2 * p(n-1) + p(n-2)
    if n%2 != 0 and n>1:
        return n + p(n-1) + 2 * p(n-2)
    if n <= 1:
        return n

#---------------------------------------------------------------
def z1(n):

    if n >= 10:
        temp = z2(n)
        return z1(temp) + temp

    return z2(n)
#---------------------------------------------------------------
def z2(n):

    if n >= 10:
        return n % 10 + z2(n//10)

    return n

#main===========================================================

exec(input().strip())
