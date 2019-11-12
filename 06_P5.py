while True:
    
    s=input().strip().split()
    if s[0]=='-1':
        break
    print(int(s[0])/((int(s[1])/100)**2))
