n=int(input())
a=[0]
a=input().split()
a=list(map(int,a))

l=a[-1]

for x in range(n-2,-1,-1):
     if(a[x]>=l):
          a[x+1]=a[x]
          print(*a)
     elif(a[x]<=l):
          a[x+1]=l
          break
     #a[x+1] = a[x] if(a[x]>1) else (l if(a[x]<=l) else a[x+1])
if(a[0]==a[1]):
     a[0]=l
print(*a)



          

