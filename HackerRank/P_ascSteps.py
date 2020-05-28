n=int(input())
for r in range(1,n+1):          
    s=""
    a = n-r
    for x in range(0,a):
        s+=" "
    for x in range(0,r):
        s+="#"
    print(s)
