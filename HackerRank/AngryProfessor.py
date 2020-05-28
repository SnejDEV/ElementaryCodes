t=int(input())
fAns=[]
while(t>0):
     count=0
     time=[]
     a=input()

     n,k=a.split()
     n=int(n)
     k=int(k)

     time=input().split(' ')

     for x in time:
          x=int(x)
          if(x<=0):
               count+=1
               
     ans = "NO" if(count>=k) else "YES"
     fAns.append(ans)
     t-=1

for x in fAns:
     print(x)
