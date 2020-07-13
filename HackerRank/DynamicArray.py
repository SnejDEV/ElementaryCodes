a=list(map(int,input().split()))

ns = a[0]
qu = a[1]
la = 0

l = [[] for x in range(0,ns)]

for x in range(0,qu):
    q = list(map(int,input().split()))
    if(q[0]==1):
        seq = l[int((q[1]^la)%ns)]           #pointer
        seq.append(q[2])
    elif(q[0]==2):
        seq = l[int((q[1]^la)%ns)]           #pointer
        la = seq[q[2]%len(seq)]
        print(la)
#    print(l) 
