a=[1,2,3,4,5]
def fun(a):
     for x in a:                        #O(n)
          for y in a:                   #O(n)
               print(x,y)
fun(a)                                  #O(n*n)=O(n^2)
