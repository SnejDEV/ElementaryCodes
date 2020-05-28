class Hash:
     def __init__(self,size):
          self.a=[None]*size

     def __str__(self):
          return(str(self.a))

     def __hash(self,key):
          hashC=0
          for x in range(0,len(key)):
               hashC = (hashC+ord(key[x])*x)%len(self.a)
          return hashC

     def set(self,key,val):
          address = self.__hash(key)
          if(self.a[address]==None):
               self.a[address] = []
          self.a[address].append([key,val])                      #storing data buckets at hash addresses
               
     def get(self,key):
          address = self.__hash(key)
          for x in self.a[address]:
               if(x[0]==key):
                    return x[1]

     def keys(self):
          keys_ = []
          for x in self.a:
               leng=len(x) if(x!=None) else 0
               if(x!=None):
                    keys_.append(x[0][0])
               if(leng>1):
                    for y in range(1,leng):
                         keys_.append(x[y][0])     
          return keys_

     def values(self):
          values_=[]
          for x in self.a:
               leng=len(x) if(x!=None) else 0
               if(x!=None):
                    values_.append(x[0][1])
               if(leng>1):
                    for y in range(1,leng):
                         keys_.append(x[y][1])     
          return values_

     def delete(self,key):
          address = self.__hash(key)
          self.a[address] = None
          
