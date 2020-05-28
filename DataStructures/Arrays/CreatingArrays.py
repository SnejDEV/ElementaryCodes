'''Create objects of the above class and use it'''
class Array:
     def __init__(self):
          self.length = 0
          self.data={}

     def __str__(self):
          return(str(self.data))

     def append(self,item):
          self.data[self.length] = item
          self.length+=1

     def get(self,index):
          return(self.data[index])

     def pop(self):
          self.new = self.data[self.length-1]
          del self.data[self.length-1]
          self.length-=1
          return(self.new)

     def shift(self,index):
           if(self.length==1):
                self.data.clear()
           else:
                for x in range(index,self.length-1):
                     self.data[index]=self.data[index+1]
                del self.data[self.length-1]
          
     def pop(self,index):                                   #O(n)
          self.shift(index)

          self.length-=1
          return(self.data)

     def insert(self,index,cv):                             #O(n)
          k=self.data[index]
          self.data[index]=cv

          for x in range(index+1,self.length+1):
               val = self.data[x] if(x!=self.length) else 0

               self.data[x]=k
               k=val
          self.length+=1
          
