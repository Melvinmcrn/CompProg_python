s = input().strip()

number = '01234567890123456789'
c_lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
c_upper = c_lower.upper()
code = number + c_lower + c_upper

count = 0
out = ''
step = -1
c_num = -1

for c in s:

    if step == -1:
        step = int(c)
    elif c_num == -1:
        c_num = int(c)
    else:
        count += 1
        
        if c not in code:
            out+=c
        else:
            out+=code[code.find(c)+step]

        if count==c_num:
            count = 0
            step = -1
            c_num = -1

print(out)
