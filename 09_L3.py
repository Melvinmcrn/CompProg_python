def extract_sign(t):
    
    sign = ''
    if t[0]=='-':
        t = t[1:]
        sign = 'lop-'

    return sign,t

#-----------------------------------------------------------------
 
def split_by_point(t):

    k = t.find('.')
    d = ''
    if k >= 0:
        d = t[k+1:]
        t = t[:k]

    return t,d 

#-----------------------------------------------------------------

def remove_comma(t):

    return t.replace(',' , '')

#-----------------------------------------------------------------
 
def split_by_million(t):

    tm = ''
    if len(t) > 6 :
        tm = t[:-6]
        t = t[-6:]

    return tm,t 

#-----------------------------------------------------------------

def digit_to_text(d):
    
    digits = 'soon nuengsong sam  see  ha   hok  jed  pad  kao  '
    return digits[d*5:d*5+5].strip() 

#-----------------------------------------------------------------

def pos_to_text(p):

    pos = '    sip roeypun muensaenlarn'
    return pos[p*4:p*4+4].strip()

#-----------------------------------------------------------------
 
def right_of_jood_to_text(t):

    out = ''
    for d in t:
        out += '-' + digit_to_text(int(d))

    return out 

#-----------------------------------------------------------------

def number_to_text(t):

    out=''
    i=0
    for c in t[-1::-1]:

        if c=='0':
            None
        elif i==0 and c=='1':
            out = '-' + 'ed'
        elif i==1 and c=='2':
            out = '-' + 'yee' + '-' + pos_to_text(i) + out
        elif i==1 and c=='1':
            out = '-' + pos_to_text(i) + out
        else:
            out = '-' + digit_to_text(int(c)) + '-' + pos_to_text(i) + out
            
        i+=1

    return out[1:]
        
    
#-----------------------------------------------------------------

def combine(moreM, lessM):

    if moreM!='' and lessM!='':
        return moreM + '-larn-' + lessM
    elif moreM!='' and lessM=='':
        return moreM + '-larn'
    elif moreM=='' and lessM!='':
        return lessM
    else:
        return 'soon'
    
#-----------------------------------------------------------------

def main():

    num          = input().strip()
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
            out += right_of_jood_to_text(d)

    print(sign + out) 

#-----------------------------------------------------------------

exec(input().strip()) 
 
 
