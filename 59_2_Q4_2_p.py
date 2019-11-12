def S(n,k): 

    if n>k>0:
        return S(n-1,k-1) - (n-1) * S(n-1,k)
    if n>0 and k==0:
        return 0
    if n==k:
        return 1
    
def L(x,y,i,j):       

    if i==-1 or j==-1:
        return 0
    if x[i]==y[j]:
        return 1 + L(x,y,i-1,j-1)
    if x[i] != y[j]:
        return max( L(x,y,i-1,j), L(x,y,i,j-1) )
    
def P(n,k):   # Time out alert !!!

    if n > k and k%2 != 0:
        return P(n,k+3) - 5
    if n > k and k%2 == 0:
        temp = P(n,k+1)
        return 2 + temp + (temp % 789)
    if n<=k:
        return k
    
def Hanoi(n,L,M,R):   
    if n==1 :
        print(1,L,'->',R)
    else:
        Hanoi(n-1,L,R,M)
        print(n,L,'->',R)
        Hanoi(n-1,M,L,R)
    
def extract_sign(t):
    sign = ''
    if t[0]=='-':
        t = t[1:]
        sign = 'lop-'
    return sign,t
def split_by_point(t):
    k = t.find('.')
    d = ''
    if k >= 0:
        d = t[k+1:]
        t = t[:k]
    return t,d
def remove_comma(t):
    return t.replace(',','')

def split_by_million(t):
    tm = ''
    if len(t) > 6 :
        tm = t[:-6]
        t = t[-6:]
    return tm,t
def digit_to_text(d):
    digits = 'soon nuengsong sam  see  ha   hok  jed  pad  kao  '
    return digits[d*5:d*5+5].strip()
def pos_to_text(p):
    pos = '    sip roeypun muensaenlarn'
    return pos[p*4:p*4+4].strip() 
def number_to_text(t):
    out = ''
    for p in range(len(t)):
        d = t[len(t)-p-1]
        if d == '0' : continue
        tmp = digit_to_text(int(d)) + '-' + pos_to_text(p)
        if p == 0 :
            out = tmp
        else:
            out = tmp + '-' + out
    out = out[:-1]
    if out[-5:] == '-soon' : out = out[:-5]
    out = out.replace('song-sip', 'yee-sip')
    out = out.replace('nueng-sip', 'sip')
    out = out.replace('sip-nueng', 'sip-ed')
    return out
def combine(moreM, lessM):
    out = lessM
    if   moreM == '' and lessM == '' : out = 'soon'
    elif moreM != '' and lessM == '' : out = moreM + '-larn' 
    elif moreM != '' and lessM != '' : out = moreM + '-larn-' + lessM 
    return out
def num2th(num):
    sign,num     = extract_sign(num)
    leftJ,rightJ = split_by_point(num)
    leftJ        = remove_comma(leftJ)
    moreM,lessM  = split_by_million(leftJ)
    tLessM       = number_to_text(lessM)
    tMoreM       = number_to_text(moreM)
    out          = combine(tMoreM, tLessM)
    if rightJ != '' :
        out += '-jood'
        for d in rightJ:
            out += '-' + digit_to_text(int(d))
    print(sign + out)
   
exec(input().strip()) # do not remove this line
