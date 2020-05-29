def revS(a):                                      #O(n)
     if(len(a)==1):
          return(a[len(a)-1])
     return(a[len(a)-1]+revS(a[0:len(a)-1]))
     
