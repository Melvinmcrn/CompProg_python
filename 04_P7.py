s=input().strip()
out=""
check=True

for c in '0123456789':
    if c not in s:
        check=False
        out+=c+" "

if check:
    print('No missing digits')
else:
    print(out.strip())
