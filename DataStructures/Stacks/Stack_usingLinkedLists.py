class Node:

     def __init__(self,value):
          self.value = value
          self.next  = None

class Stack:

     def __init__(self):
          self.head = None
          self.tail = None
          self.length = 0

     def push(self,value):                    #append
          node = Node(value)

          if(self.length==0):
               self.head = node
               self.tail = node
          else:
               node.next = self.head
               self.head = node

          self.length += 1

     def pop(self):
          temp = self.head.value
          self.head = self.head.next
          self.length -= 1
          if(self.length==0):
               self.tail = None            #On popping vals @length = 0, the object despite being deleted at head node,
                                           #the tail node still has the the object, therefore we delete that node
          return(temp)

     def peek(self):
          return(self.head.value)
          
     
               
               

          
