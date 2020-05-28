a,l,size=[],[],0
n=int(input())
def accept():
    global a
    while(len(a)!=n):
        a=input().split(' ')
accept()

for x in range(0,n):
     a[x]=int(a[x])
for x in a:
     q=[]
     c=0
     for y in a:
          if(x-y==0):
               l.append(y)
          elif(x-y==1 and y<x):
               l.append(y)
               c=1
          elif(x-y==-1 and y>x):
               q.append(y)
     l.sort()
     if(c!=1):
          for z in q:
               if(abs(l[0]-z)==1):
                    l.append(z)
     size=len(l) if(len(l)>size) else size
     l=[]
print(size)
          
