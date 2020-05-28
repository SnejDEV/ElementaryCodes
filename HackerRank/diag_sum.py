a=[]
ne = int(input())
def accept():
    a=[]
    while(len(a)!=ne):
        a=(input().strip()).split(' ')
    return a
def sum():
    tot=[0,0]
    for x in range(0,ne):
        tot[0]+=int(a[x][x])
        tot[1]+=int(a[x][-(x+1)])
    return abs(tot[0]-tot[1]) 
        
for x in range(0,ne):
    a.append(accept())
print(sum())
