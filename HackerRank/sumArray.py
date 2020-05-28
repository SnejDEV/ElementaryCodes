ne = int(input())
a,tot=[],0
while(len(a)!=ne):
    a=[]
    a=input().split(' ')
for x in a:
    tot+=int(x)
print(tot)
    
