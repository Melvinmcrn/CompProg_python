def remove_symbol(s):

    symbol = '0123456789+-,./!'
    out = ''
    for c in s:
        if c in symbol:
            out += ' '
        else:
            out += c

    return out.lower()

#-----------------------------------------------------------
def str_to_unique_list(s):

    out = []
    for c in s.strip().split():
        if c not in out:
            out.append(c)

    return out

#-----------------------------------------------------------
def percent_in_list(template,test):

    count = 0
    for c in test:
        if c in template:
            count += 1

    return count * 100 / len(test)
#-----------------------------------------------------------
def main():
    good = input().strip()
    good = remove_symbol(good)
    good = str_to_unique_list(good)
    
    bad = input().strip()
    bad = remove_symbol(bad)
    bad = str_to_unique_list(bad)
    
    n = int(input())
    for i in range(n):
        test = input().strip()
        test = remove_symbol(test).lower()
        test = str_to_unique_list(test)

        good_p = percent_in_list(good,test)
        bad_p = percent_in_list(bad,test)

        print(test)
        print(good_p,bad_p)

#main=========================================================
exec(input().strip())
