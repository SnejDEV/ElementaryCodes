def sort(a):                                 #timeComplexity = O(n^2) and spaceComplexity = O(1)
     for x in range(0,len(a)-1):
          for y in range(0,(len(a)-1)-x):
               if(a[y]>a[y+1]):
                    a[y]=a[y]+a[y+1]
                    a[y+1]=a[y]-a[y+1]
                    a[y]=a[y]-a[y+1]
     return(a) 
