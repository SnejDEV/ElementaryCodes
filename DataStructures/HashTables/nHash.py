class Hash:
     def __init__(self):
          self.a=[]

     def set(self,key,val):
          for x in range(0,len(self.a)):
               if(self.a[x][0]==key):
                    self.a[x][1]=val
                    return(None)
          key=[key]
          key.append(val)
          self.a.append(key)

     def get(self,key):
          for x in range(0,len(self.a)):
               if(self.a[x][0]==key):
                    return(self.a[x][1])

          


          
