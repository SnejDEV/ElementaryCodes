an=int(input())
a=input().split()
qn=input()
q=input().split()

a=list(map(int,a))
q=list(map(int,q))

sum_=0

for x in q:
     for y in range(0,an):
          a[y]+=x
          sum_+=abs(a[y])
     print(sum_)
     sum_=0
               
'''After learning dataStructures optimize ur cide to get full points'''
