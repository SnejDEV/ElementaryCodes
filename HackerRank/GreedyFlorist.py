count=0
_sum=0

nk = input()
n,k=nk.split()
n,k=int(n),int(k)

p=input().split()
p=[int(p[x]) for x in range(0,n)]
p.sort(reverse=True)

pos=[0 for x in range(0,k)]
fp=[0 for x in range(0,k)]

for x in p:
     fp[count]+=(pos[count]+1)*x
     pos[count]=pos[count]+1
     count+=1
     if(count>=k):
          count=0

for x in fp:
     _sum+=x

print(_sum)
     
     
          
          
     
     
     
