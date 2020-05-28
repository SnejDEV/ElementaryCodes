class Node():
     def __init__(self,value):
          self.value = value
          self.next = None

class Queue:
     def __init__(self):
          self.head = None
          self.tail = None
          self.length = 0

     def enqueue(self,value):
          node = Node(value)
          if(self.length==0):
               self.head = node
               self.tail = node
          else:
               self.tail.next = node
               self.tail = node              #now that both self.tail.next and self.tail refer to same object, a change at any of them will cause CHANGE AT OBJECT,
                                             #THEREFORE AFFECTING BOTH VARIABLES
          self.length += 1

     def dequeue(self):
          temp = self.head.value
          self.head = self.head.next
          self.length -= 1
          if(self.length==0):
               self.tail = None
          return(temp)

     def peek(self):
          return(self.head.value)

     def isEmpty(self):
          if(self.tail==None):
               return(True)
          elif(self.tail!=None):
               return(False)
