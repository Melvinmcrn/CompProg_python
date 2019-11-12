def isSevenUp(x):

    if '7' in str(x) or x%7==0:
        return True
    else:
        return False

#-------------------------------------------------------------

def nextSevenUp(x):

    x+=1
    while True:
        if isSevenUp(x):
            return x
        x+=1

#-------------------------------------------------------------

def prevSevenUp(x):

    x-=1
    while True:
        if isSevenUp(x):
            return x
        x-=1

#main---------------------------------------------------------

f,x = input().strip().split()
x = int(x)

if   f == 'isSevenUp' :   print(isSevenUp(x))
elif f == 'nextSevenUp' : print(nextSevenUp(x))
elif f == 'prevSevenUp' : print(prevSevenUp(x))
