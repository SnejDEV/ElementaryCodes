ot={}
s=''
fs=[]

n = int(input())
for x in range(1,n+1):
     tex=input().split(' ')
     ot[x]=int(tex[0])+int(tex[1])
values=list(ot.values())
values.sort()

def check(a):
     global ot
     for y in range(1,n+1):
          if(ot[y]==a):
               ot[y]='gomma'
               return(y)

for x in values:
     s+=str(check(x))+' '

print(s)               
               
