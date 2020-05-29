def Tri(n):                             #Recursive                         
     if(n<2):  
          return(0)
     elif(n==2):
          return(n-1)                   #n-1 will be equal to 1
     return(Tri(n-1)+Tri(n-2)+Tri(n-3))
     
