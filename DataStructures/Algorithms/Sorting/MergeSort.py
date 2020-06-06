import math

def split(a):                              #array as input
     if(len(a)==1):
          return(a)
     
     mid = math.floor(len(a)/2)
     left = a[0:mid]
     right = a[mid:]
     
     return sort(split(left),split(right))

def sort(l,r):
     i = len(l)
     j = len(r)
     fa = []
     x=0
     y=0
     while(x<i and y<j):
          if(l[x]>r[y]):
               fa.append(r[y])
               y+=1
          elif(l[x]<r[y]):
               fa.append(l[x])
               x+=1 
          elif(l[x]==r[y]):
               fa.append(l[x])
               fa.append(r[y])
               x+=1
               y+=1
     while(x<i):
          fa.append(l[x])
          x+=1
     while(y<j):
          fa.append(r[y])
          y+=1
     return(fa)
