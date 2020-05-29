'''def FibR(n):               #Recursive dev1 
   global a,b
   if(n==0):
      temp = a
      a,b=0,1
      return(temp)
   c=a
   a=b
   b=a+c
   return FibR(n-1)'''

def Fib(n):                      #Improvised Recursive
   if(n<2):
      return n                   #if the recursive n reaches 0 or 1
   return Fib(n-1)+Fib(n-2)      #For eg. if the series is 0,1,1,2      2 can be represented as the sum of 1(@ pos 2) and 1(@ pos 1)
