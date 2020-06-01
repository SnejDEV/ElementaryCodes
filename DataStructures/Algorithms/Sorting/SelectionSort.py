def SS(array):
     for x in range(0,len(array)-1):
          pos=x
          for y in range(x+1,len(array)):
               if(array[y]<array[x]):
                    pos = y
          if(pos!=x):
               array[x]=array[x]+array[pos]
               array[pos]=array[x]-array[pos]
               array[x]=array[x]-array[pos]
     return(array)
               
                    
          
