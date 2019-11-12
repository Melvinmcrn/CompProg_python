num=int(input())
out=str(num)+" = "

if num==0:
    out+="0"

else:

    check_minus=False
    if num<0:
        out+='-'
        num*=-1
        check_minus=True
        
    for i in range(len(str(num)),0,-1):
        
        n_temp=(num%10**(i))//10**(i-1)
        if n_temp!=0:
            
            if i!=len(str(num)) and check_minus:
                out+='- '
            elif i!=len(str(num)) and not check_minus:
                out+='+ '
            
            out+=str(n_temp)+'*'+str(10**(i-1))+' '

print(out.strip())
