l,s=[],0
def accept():
    a=[]
    while(len(a)!=5):
        a=input().split(' ')
    b=[int(x) for x in a]
    return b
b=accept()
for x in range(0,5):
    n=b[x]
    tempPos=0
    for y in range(x+1,5):
        if(b[y]<n):
            n=b[y]
            tempPos=y
            b[x]=b[x]+b[tempPos]
            b[tempPos]=b[x]-b[tempPos]
            b[x]=b[x]-b[tempPos]
for x in range(1,4):
    s+=b[x]
print("{} {}".format(s+b[0],s+b[4]))
    
