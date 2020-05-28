a,b,ans=int(input()),int(input()),""
ans="1 "+ans if(a==0 or a==1) else ans
a=9 if(a<9) else a
for x in range(a,b+1):
    num = str(x**2)

    l = len(str(x))
    l1=len(num)

    rp=int(num[l1-l:l1])
    lp=int(num[0:(l1-l)])

    if(lp+rp==int(x)):
        ans+=str(x)+" "
ans="INVALID RANGE" if(ans=="") else ans
print(ans)
    
