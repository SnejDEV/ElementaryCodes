import math

def DC(a):                        #array
     if(len(a)==1):
          return(a)
     
     mid = math.floor(len(a)/2)
     left = a[0:mid]
     right = a[mid:]

     print(left)
     print(right)

     DC(left)
     DC(right)
