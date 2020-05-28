a=[]
ne = int(input())
def accept():
    global a
    while(len(a)!=ne):
        a=(input().strip()).split(' ')
    for x in range(0,3):a.append(0)
    for x in range(0,ne):
        if(int(a[x])>00):
            a[ne]=(a[ne]+1)
        elif(int(a[x])<0):
            a[ne+1]=(a[ne+1]+1)
        elif(int(a[x])==0):
            a[ne+2]=(a[ne+2]+1)
accept()
for x in range(0,3):
    print("{:.6f}".format(a[ne+x]/ne))
