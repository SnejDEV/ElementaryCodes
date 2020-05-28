n = int(input())
a=input().split()
a=list(map(int,a))

for x in range(1,n):
     val = a[x]
     count=0
     
     for y in range(x-1,-1,-1):
          if(val>a[y] and count == 0):
               a[y+1]=val
               count = 1

          elif(val<=a[y]):
               a[y+1]=a[y]
               if(a[y]==a[y+1]):
                    a[y]=val
          if(y==0):
               print(*a)

                     
